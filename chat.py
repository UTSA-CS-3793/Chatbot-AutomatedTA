import tensorflow as tf
import ujson as json
import numpy as np
from tqdm import tqdm
import os, sys

from model import Model
from util import get_record_parser, convert_tokens, evaluate, get_batch_dataset, get_dataset


def chat(config):
    print("WELL IT GOT HERE")
    # sys.exit(1)

    # load the saved pre-processed files
    # might get rid of this, but will have to preprocess the question inputed
    with open(config.word_emb_file, "r") as fh:
        word_mat = np.array(json.load(fh), dtype=np.float32)
    with open(config.char_emb_file, "r") as fh:
        char_mat = np.array(json.load(fh), dtype=np.float32)
    with open(config.test_eval_file, "r") as fh:
        eval_file = json.load(fh)
    with open(config.test_meta, "r") as fh:
        meta = json.load(fh)

    # total number of validation data?
    total = meta["total"]

    # don't think this next line is the model loading, just this is the model
    # loading phase or something
    print("Loading model...")
    # this looks like it's loading data
    test_batch = get_dataset(config.test_record_file, get_record_parser(
        config, is_test=True), config).make_one_shot_iterator()

    # create a model
    model = Model(config, test_batch, word_mat, char_mat, trainable=False)

    # tensorflow shit, should be irrelevant
    sess_config = tf.ConfigProto(allow_soft_placement=True)
    sess_config.gpu_options.allow_growth = True

    with tf.Session(config=sess_config) as sess:
        # global variables shit
        sess.run(tf.global_variables_initializer())

        # i think this is the laoding the weights part, could be that stuff
        # above though
        saver = tf.train.Saver()
        saver.restore(sess, tf.train.latest_checkpoint(config.save_dir))
        # and i think this is the saving the weights to the model part?
        sess.run(tf.assign(model.is_train, tf.constant(False, dtype=tf.bool)))

        losses = []
        answer_dict = {}
        remapped_dict = {}
        # actually get the losses and stuff (hence the tqdm)
        for step in tqdm(range(total // config.batch_size + 1)):
            # i think this is running the model\
            # qa_id is the id of the question
            # yp1 is the index in the context of that question where the answer starts
            # yp2 is the index in the context of that question wehre the answer ends
            # i think everytime you run these tf objects the parser get's called to move
            #   them along
            qa_id, loss, yp1, yp2 = sess.run(
                [model.qa_id, model.loss, model.yp1, model.yp2])

            # answer dict is a dictionary of the answers, by id given by qa_id
            # remapped_dict is the same but the id's are remapped to the original
            #   json id's (i think they changed them somewhere in pre processing)
            answer_dict_, remapped_dict_ = convert_tokens(
                eval_file, qa_id.tolist(), yp1.tolist(), yp2.tolist())

            # update statistics? or store them for later evaluation
            answer_dict.update(answer_dict_)
            remapped_dict.update(remapped_dict_)
            losses.append(loss)
            if step == 2:
                sys.exit(1)

        # loss and metrics
        loss = np.mean(losses)
        metrics = evaluate(eval_file, answer_dict)

        # save off the returned answers in a json, formatted as {id: answer}
        # question id i think
        print("CONFIG.ANSWER_FILE", config.answer_file)
        with open(config.answer_file, "w") as fh:
            json.dump(remapped_dict, fh)

        print("Exact Match: {}, F1: {}".format(
            metrics['exact_match'], metrics['f1']))

























# stop fuck

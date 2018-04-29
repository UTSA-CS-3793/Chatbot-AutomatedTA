from data_builder_indystdy import set_training_data, response
import tensorflow as tf
import tflearn

def train_data():
    train_x, train_y = set_training_data()
    
    # reset underlying graph data
    tf.reset_default_graph()
    # Build neural network
    net = tflearn.input_data(shape=[None, len(train_x[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
    net = tflearn.regression(net)
    
    # Define model and setup tensorboard
    global model
    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
    # Start training (apply gradient descent algorithm)
    model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
    model.save('model.tflearn')

if __name__ == '__main__':
    print('\n', 'Starting Data Collecting and Training...', '\n')
    train_data()
    while 1:
        text = input('Ask a question \n')
        if text == 'bye':
            break
        print('\n', response(text, model), '\n')

# ManPages


Finding topics to questions asked, to be able to feed a question on the MicroSoft R-NET model.


# Dependencies:

tflearn

nltk

ujson

anaconda

tensorflow

BeautifulSoup4 (bs4)


# Running
python init_qa_bot.py

## What doesn't work?

All the parts work seperately
	
	1) Automated data gathering from stackoverflow

	2) Training of model and prediction of topics of the questions
	
	3) Get context from stackoverflow, based on the topic and the question
	
	4) Trasnfer everything to json file
	
	5) Feed into R-NET model


What doesn't work is a direct method of inputing a single question and recieving a single answer.










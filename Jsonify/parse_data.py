from data import s

class Paragraph():

	def __init__(self, title):
		self.title = title
		self.contexts = []

	def add_context(self, context):
		self.contexts.append(context)

		


class Context():
	
	def __init__(self, text):
		self.text = text
		self.QandAs = []
	
	def add_QandA(self, qa):
		self.QandAs.append(qa)
	

class QandA():
	
	def __init__(self, q, a, start, idd):
		self.q = q
		self.a = a
		self.a_start = start
		self.id = idd


paragraphs_json = [[d["paragraphs"], d["title"]] for d in s["data"]]

paragraphs = []

for p, t in paragraphs_json: 
	par = Paragraph(t)
	for cqa in p:
		context = Context(cqa["context"])
		for qa in cqa["qas"]:
			qa = QandA(qa["question"], qa["answers"][0]["text"], qa["answers"][0]["answer_start"], qa["id"])
			context.add_QandA(qa)
		par.add_context(context)
	paragraphs.append(par)




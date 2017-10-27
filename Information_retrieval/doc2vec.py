import gensim, json, itertools, jieba
from os import listdir
from os.path import isfile, join
from gensim.models.doc2vec import LabeledSentence as LabeledSentence

class LabeledLineSentence(object):
	def __init__(self):
		self.wholeNovels = {}
		[self.wholeNovels.update(json.load(open(i, 'r'))) for i in listdir('./') if i.endswith('.json')]

	def __iter__(self):
		for key, value in self.wholeNovels.items():
			yield LabeledSentence(words=jieba.lcut(value),labels=[key])

it = LabeledLineSentence()

model = gensim.models.Doc2Vec(size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025) # use fixed learning rate
model.build_vocab(it)
for epoch in range(10):
	model.train(it)
	model.alpha -= 0.002 # decrease the learning rate
	model.min_alpha = model.alpha # fix the learning rate, no deca
	model.train(it)

model.save("doc2vec.model")
# print model.most_similar(“documentFileNameInYourDataFolder”)
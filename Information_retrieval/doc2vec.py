import gensim, json, itertools, jieba, os, sys, pyprind
from os import listdir
from os.path import isfile, join
from gensim.models.doc2vec import LabeledSentence as LabeledSentence
jieba.load_userdict(os.path.join('..', "dictionary", "NameDict_Ch_v2"))

wholeNovels = {}
[wholeNovels.update(json.load(open(i, 'r'))) for i in listdir('./') if i.endswith('.json')]

docs = [LabeledSentence(words=jieba.lcut(value), tags=[key]) for key, value in wholeNovels.items()]

model = gensim.models.Doc2Vec(size=300, window=10, min_count=5, workers=24,alpha=0.025, min_alpha=0.025) # use fixed learning rate
model.build_vocab(docs)
for epoch in pyprind.prog_bar(list(range(500))):
	#model.train(docs)
	model.train(docs,total_examples=model.corpus_count, epochs=model.iter)
	model.alpha -= 0.002 # decrease the learning rate
	model.min_alpha = model.alpha # fix the learning rate, no deca
	model.train(docs,total_examples=model.corpus_count, epochs=model.iter)

model.save(sys.argv[1]+".model")
#model = models.Doc2Vec.load('doc2vec.model')
model_loaded.docvecs.most_similar(["第三十六章 夢裡真 真語真幻"])

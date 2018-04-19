import requests, tqdm, json, sys
from pymongo import MongoClient
client = MongoClient(None)
db = client['ptt']
articlesCollect = db['articles_hatepolitics']
IndexCollect = db['invertedIndex_hatepolitics']
issue = sys.argv[1]
print('Please input the issue or keyword your want to retrieve from PTT:', issue)

##################Hatepolitics#####################

top10_table = {}
invertedIndex = IndexCollect.find({'issue':issue}).limit(1)[0]['ObjectID']
for ObjectID in tqdm.tqdm(invertedIndex):
    doc = ' '.join(articlesCollect.find({'_id':ObjectID}).limit(1)[0]['content'])
    if not doc:
        continue
    result = requests.post("http://140.120.13.243/tfidf/tfidf?flag=n", {"doc":doc}).json()
    top10 = sorted(result, key=lambda x:-x[1])[:10]
    for topk_word, topk_score in top10:
        top10_table[topk_word] = top10_table.setdefault(topk_word, 0) + 1

json.dump(top10_table, open('hatepolitics-{}.json'.format(issue), 'w'))


####################八卦版#########################3
articlesCollect = db['articles']
IndexCollect = db['invertedIndex']

top10_table = {}
invertedIndex = IndexCollect.find({'issue':issue}).limit(1)[0]['ObjectID']
for ObjectID in tqdm.tqdm(invertedIndex):
    doc = ' '.join(articlesCollect.find({'_id':ObjectID}).limit(1)[0]['content'])
    print(doc, ObjectID)
    if not doc:
        continue
    result = requests.post("http://140.120.13.243/tfidf/tfidf?flag=n", {"doc":doc}).json()
    top10 = sorted(result, key=lambda x:-x[1])[:10]
    for topk_word, topk_score in top10:
        top10_table[topk_word] = top10_table.setdefault(topk_word, 0) + 1

json.dump(top10_table, open('gossip-{}.json'.format(issue), 'w'))
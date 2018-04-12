import json, sys
topk = int(input("Please specify the topk you want to retrieve from gossip.json and hate.json:"))
gossip = json.load(open('gossip.json', 'r'))
hate = json.load(open('hatepolitics.json', 'r'))

gossip_topk = sorted(gossip.items(), key=lambda x:-x[1])[:topk]
hate_topk = sorted(hate.items(), key=lambda x:-x[1])[:topk]

print('gossip_topk:')
print('=================================')
print(gossip_topk)

print('hate_topk:')
print('=================================')
print(hate_topk)

json.dump(gossip_topk, open('gossip_topk.json', 'w'))
json.dump(hate_topk, open('hate_topk.json', 'w'))
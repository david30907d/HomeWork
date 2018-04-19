import json, sys

issue, topk = sys.argv[1], int(sys.argv[2])
print('Please input the issue or keyword your want to retrieve from PTT:', issue)
print("Please specify the topk you want to retrieve from gossip.json and hate.json:", topk)
gossip = json.load(open('gossip-{}.json'.format(issue), 'r'))
hate = json.load(open('hatepolitics-{}.json'.format(issue), 'r'))

gossip_topk = sorted(gossip.items(), key=lambda x:-x[1])[:topk]
hate_topk = sorted(hate.items(), key=lambda x:-x[1])[:topk]

print('gossip_topk:')
print('=================================')
# print(gossip_topk)

print('hate_topk:')
print('=================================')
# print(hate_topk)

json.dump(gossip_topk, open('gossip_topk-{}.json'.format(issue), 'w'))
json.dump(hate_topk, open('hate_topk-{}.json'.format(issue), 'w'))
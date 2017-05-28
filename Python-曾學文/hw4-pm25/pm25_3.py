import json, math
from collections import *
class Pm25(object):
    """docstring for Pm25"""
    def __init__(self):
        self.file = json.load(open('result.json', 'r'))
        with open('clean.txt', 'w') as f:
            for i in self.file:
                tmp = ''
                for j in i:
                    tmp = tmp + str(j) + ","
                f.write(tmp[:-1]+"\n")

    def cosine_similarity(self, v1, v2):
        """
        計算兩個向量的正弦相似度。距離越近，相似度數值會越高。
        :param v1:
        :param v2:
        :return:
        """
        if v1==[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] or v2==[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            return 0
        sum_xx, sum_xy, sum_yy = 0.0, 0.0, 0.0
        for i in range(0, len(v1)):
            sum_xx += math.pow(v1[i], 2)
            sum_xy += v1[i] * v2[i]
            sum_yy += math.pow(v2[i], 2)
        return sum_xy / math.sqrt(sum_xx * sum_yy)

    def Euclidean(self, v1, v2):
        result = 0
        for i in range(0, len(v1)):
            result += math.pow(v1[i]-v2[i], 2)
        return result

    def knn_classify(self, date, location, k):
        """
        執行kNN分類演算法
        :param input_tf: 輸入向量
        :param trainset_tf: 訓練集合向量
        :param trainset_class: 訓練集合分類
        :param k: 取k個最近鄰居
        :return:
        """
        for i in self.file:
            if date in i and location in i:
                input_tf = i
                break

        orderdict = OrderedDict(sorted(
            list(
                filter(
                    lambda x:date+location != x[0]
                    ,map(
                        lambda x:(x[0]+x[1], (self.cosine_similarity(x[3:], input_tf[3:]), x)), self.file[:k+1]
                    )
                )
            ), 
            key=lambda x:-x[1][0])
        )

        eudict = OrderedDict(sorted(
            list(
                filter(
                    lambda x:date+location != x[0]
                    ,map(
                        lambda x:(x[0]+x[1], (self.Euclidean(x[3:], input_tf[3:]), x)), self.file[:k+1]
                    )
                )
            ), 
            key=lambda x:x[1][0])
        )

        for data in self.file[k+1:]:
            tmp = self.cosine_similarity(data[3:], input_tf[3:])
            eu = self.Euclidean(data[3:], input_tf[3:])

            for index, value in orderdict.items():
                if data[0]+data[1] in orderdict or data[0]+data[1]==input_tf[0]+input_tf[1]:
                    continue
                if tmp > value[0]:
                    del orderdict[index]
                    orderdict[data[0]+data[1]] = (tmp, data)
                    if len(orderdict) <5:
                        print(orderdict)
                        raise Exception
                    break

            for index, value in eudict.items():
                if data[0]+data[1] in eudict or data[0]+data[1]==input_tf[0]+input_tf[1]:
                    continue
                if eu < value[0]:
                    del eudict[index]
                    eudict[data[0]+data[1]] = (eu, data)
                    if len(eudict) <5:
                        print(eudict)
                        raise Exception
                    break
        return orderdict, eudict

if __name__ == '__main__':
    p = Pm25()
    cos, ed = p.knn_classify('2015/01/01', '龍潭', 5)
    print('2015/01/01, 龍潭, 5')
    print('cosine similarity:')
    for i in cos.items():
        print(i)

    print('Euclidean:')
    for i in ed.items():
        print(i)

    print('------------------------------------')
    while True:
        date = input('please input date, eq:2015/01/01')
        location = input('please input location')
        num = int(input('how many neighbor do you want?'))
        cos, ed = p.knn_classify(date, location, num)

        print('cosine similarity:')
        for i in cos.items():
            print(i)

        print('Euclidean:')
        for i in ed.items():
            print(i)
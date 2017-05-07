# -*- coding: utf-8 -*-
from __future__ import absolute_import
import random, threading, time
from itertools import imap
from itertools import ifilter
threadLock = threading.Lock()

class Pocker(object):
    u"""docstring for pocker"""
    def __init__(self):
        self.card = list(imap(self.cal, xrange(1,53)))
        random.shuffle(self.card)

    @staticmethod    
    def cal(num):
        num = int(num)
        if num-num//13*13 == 0:
            return (num//13)-1, 13
        return (num//13, num-num//13*13 if num>13 else num)

    def getcard(self):
        return self.card.pop()

    def hasMoreCards(self):
        return len(self.card)!=0

p = Pocker()

class Player(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.card = set([p.getcard(), p.getcard(), p.getcard()])
        self.score = []

    def run(self):
        print self.threadName + u' start to play:' + unicode(self.card)
        flag, exit = False, False

        while p.hasMoreCards() and exit==False:
            time.sleep(0.01)
            while flag or threading.activeCount()==5:
                flag = True

                now = p.card[-1]
                threadLock.acquire()
                self.play()
                threadLock.release()
                if len(self.card) == 0:
                    self.finish()
                    exit = True
                    break

                time.sleep(1)
                if p.hasMoreCards() and p.card[-1] == now:
                    threadLock.acquire()
                    if p.card[-1] == now:
                        print self.threadName + u'偷牌：' + unicode(p.card[-1])
                        
                        self.score.append((u'Steal', p.getcard(), 5))
                        
                        self.showScore()
                        print
                    threadLock.release()

    def play(self):
        for i in list(ifilter(lambda x:x[1]==p.card[-1][1], self.card)):
            print u'搶牌前：'
            self.showScore()
            
            print u'{} use {} to get {}'.format(self.threadName, i, p.card[-1])
            self.card.remove(i)
            self.score.append((u'sameNum', p.getcard(), 30))

            print u'搶牌後：'
            self.showScore()
            print
            return 
        for i in list(ifilter(lambda x:x[0]==p.card[-1][0], self.card)):
            print u'搶牌前：'
            self.showScore()

            print u'{} use {} to get {}'.format(self.threadName, i, p.card[-1])
            self.card.remove(i)
            self.score.append((u'sameColor', p.getcard(), 10))

            print u'搶牌後：'
            self.showScore()
            print
            return

    def finish(self):
        print self.threadName + u'結束！'
        if threading.activeCount() == 5:
            self.score.append((u'finish', u'prize', 50))
        elif threading.activeCount() == 4:
            self.score.append((u'finish', u'prize', 20))

    def showScore(self):
        if len(self.score) >=2:
            result = reduce((lambda x,y:(0, 0, x[2]+y[2])), self.score)[-1]
        elif len(self.score)==1:
            result = self.score[0][2]
        else:
            result = 0
        print self.threadName, u'手牌：' + unicode(self.card) + u' 得分過程：' + unicode(self.score) + u' 總分：' + unicode(result)

# Create new threads
threads = []
for tName in [u"play1", u"play2", u"play3", u"play4"]:
    thread = Player(tName)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for t in threads:
    t.join()

for t in threads:
    t.showScore()
print u"Exiting Main Thread"
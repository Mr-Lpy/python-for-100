# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数

import re

class WordsCount:
    def __init__(self):
        self.wordDict = dict()

    def getWords(self,filepath):
        try:
            fin = open(filepath,'r')
            data = fin.read()

            reObj = re.compile('\b?(\w+)\b?')
            self.words = reObj.findall(data)
            
        except Exception as e:
            print('error:' + e)
    
    def count(self):
        for word in self.words:
            if word.lower() in self.wordDict.items():
                self.wordDict[word.lower()] += 1
            else:
                self.wordDict[word] = 1

        for k,v in self.wordDict.items():
            print('%s: %s' % (k,v))

'''
if __name__ == '__main__':
    wc = WordsCount()
    wc.getWords('D:/codefactory/git/100/python-for-100/4/test.txt')
    wc.count()
'''
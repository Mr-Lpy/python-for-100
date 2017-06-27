# **第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词

'''
1. 获取目录下文件列表
2. 统计所有文件单词次数
3. 返回规定单词次数
'''
import os
import sys
sys.path.append('D:\\codefactory\\git\\100\\python-for-100\\6')
import WordCount

class FileWordsCount:
    def __init__(self):
        self.wc = WordCount.WordsCount()
        self.wordsDic = dict()
        self.filter = ['a','the','to']

    def __count(self,filepath):
        self.wc.getWords(filepath)
        return self.wc.count()

    def getWords(self,dir):
        # 获取目录下所有的文件
        if not os.path.isdir(dir):
            return
        fileList = os.listdir(dir)
        for file in fileList:
            filepath = os.path.join(dir,file)
            fileDict = self.__count(filepath)
            for word in fileDict:
                if word in self.wordsDic:
                    self.wordsDic[word] += fileDict[word]
                else:
                    self.wordsDic[word] = fileDict[word]

    def mywords(self):
        for word in self.wordsDic:
            word = word.lower()
            wordDict = dict()
            if not word in self.filter:
                continue
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1

        ansList = sorted(wordDict.items(),key=lambda t: t[1], reverse=True)
        print(ansList) 

if __name__ == '__main__':
    fwc = FileWordsCount()
    fwc.getWords("D:\\codefactory\\git\\100\\python-for-100\\6\\files\\")
    fwc.mywords()
# **第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os 
import re

def stat_code(dir):
    if not os.path.isdir(dir):
        return
    
    exp_re = re.compile(r'^#.*')
    file_list = os.listdir(dir)
    print("%s\t%s\t%s\t%s"%('file','all_lines','space_lines','exp_lines'))
    for file in file_list:
        file_path = os.path.join(dir,file)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.py':
            f = open(file_path,mode='r',encoding='utf-8')
            all_lines = 0
            space_lines = 0
            exp_lines = 0
            
            for line in f.readlines():
                all_lines += 1
                if line.strip() == '':
                    space_lines += 1
                    continue
                exp = exp_re.findall(line.strip())
                if exp:
                    exp_lines += 1
               
            print("%s\t%s\t%s\t%s" % (file,all_lines,space_lines,exp_lines))


if __name__ == '__main__':
    stat_code('d:\\codefactory\\git\\100\\python-for-100\\7\\')
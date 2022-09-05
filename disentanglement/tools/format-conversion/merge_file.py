"""
将以天为单位存储的解耦后文件合并成一个文件
"""
import os
path = "..\\..\\..\\..\\Data\\Gitter_Channels\\Angular\\disentangle\\message_by_day\\disentangled\\"
dir = os.listdir(path)
file = open("..\\..\\..\\..\\Data\\Gitter_Channels\\Angular\\disentangle\\Angular_result.txt","w",encoding="UTF-8")
dir.sort()
for fileName in dir:
    row = 1
    for line in open(path+fileName):
        if line.startswith("------") :
            file.write(line)
            row =1
            print(line)
        else:
          line =str(row)+" ["+fileName[:10] + " " + line[1:]
          row = row + 1
          file.write(line)
          print(line)
file.close()

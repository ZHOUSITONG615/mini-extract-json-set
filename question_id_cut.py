import os
import json

filePath1 = r"D:\VQA\ST-VQA\human\code\human_train3.txt"#读取图片id信息
fpa1 = open(filePath1)
filePath2 = r"D:\VQA\ST-VQA\human\code\v2_OpenEnded_mscoco_train2014_questions.json"#读取图片id信息
fpa2 = open(filePath2)
fp1 = open("D:\VQA\ST-VQA\human\code\human_train4.txt", "w+")
linea=0

for line in fpa1.readlines():
    for line2 in fpa2.readlines():
        line = line.split('COCO_train2014_000000')
    fp1.writelines(line)

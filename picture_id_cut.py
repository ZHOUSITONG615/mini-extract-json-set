import os

filePath = r"D:\extract-json-set/food_val.txt"
#filePath = r"D:\extract-json-set\food_train.txt"
fpa = open(filePath)
#fp1 = open("D:\VQA\ST-VQA\human\code\food_train1.txt", "w")
#fp1 = open("D:\extract-json-set\food_test1.txt", "w")
fp1 = open("D:\extract-json-set/food_val1.txt", "w")

# fp2 = open("2.txt", "w")
for linea in fpa.readlines():
    #linea = linea.split('COCO_train2014_000000')
    #linea = linea.split('COCO_test2015_000000')
    linea = linea.split('COCO_val2014_000000')
    #linea = linea.split('.jpg')
    # linea=(linea.lstrip('STCOCO_train2014_000000').rstrip('.jpg'))
    # linea = linea.replace("\n", "").split("\t")
    fp1.writelines(linea)
    # fp2.writelines(linea[1])
    print(fpa)
fpa.close()
fp1.close()



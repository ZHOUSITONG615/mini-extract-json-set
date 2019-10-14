# Read pictures' name in file_path
# Write into the .txt file

import os

file_path = "D:\DMN-datsset\Images\human-image-set\human_test_set"

path_list = os.listdir(file_path)
# print(path_list)

path_name = []

for i in path_list:
    # path_name.append("ST"+i)
    path_name.append(i.split(".")[0])

# path_name.sort()

for file_name in path_name:
    with open("D:\extract-json-set\human_test.txt", "a") as f:
        f.write(file_name + "\n")
        print(file_name)
    f.close()

filePath = r"D:\extract-json-set\human_test.txt"
fpa = open(filePath)
#fp1 = open("D:\VQA\ST-VQA\human\code\human_train2.txt", "w")
fp1 = open("D:\extract-json-set\human_test1.txt", "w")

# fp2 = open("2.txt", "w")
for linea in fpa.readlines():
    #linea = linea.split('COCO_train2014_000000')
    linea = linea.split('COCO_test2015_000000')
    #linea = linea.split('.jpg')
    # linea=(linea.lstrip('STCOCO_train2014_000000').rstrip('.jpg'))
    # linea = linea.replace("\n", "").split("\t")
    fp1.writelines(linea)
    # fp2.writelines(linea[1])
    print(fpa)
fpa.close()
fp1.close()



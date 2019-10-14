#Read pictures' name in file_path 
#Write into the .txt file

import os
#file_path = "D:\DMN-datsset\Images\human-image-set\food_train_set"
#file_path = "D:\DMN-datsset\Images\human-image-set\food_val_set"
file_path = "D:\DMN-datsset\Images/food-image-set/food_test_set"
path_list = os.listdir(file_path)
# print(path_list)

path_name=[]

for i in path_list:

    # path_name.append("ST"+i)
    path_name.append(i.split(".")[0])

#path_name.sort()

for file_name in path_name:
    with open("D:\extract-json-set/food_test.txt","a") as f:
        f.write(file_name + "\n")
        print(file_name)
    f.close()
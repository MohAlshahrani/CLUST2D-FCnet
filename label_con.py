import os
from PIL import Image
from util import filesNdirec
import numpy as np

#put the directory  here the folder of all training images reside.
trainig_dir = "../../../scratch/mqa5928/CLUST2D/train/"

files_list=[]
names=[]
roots =[]
f_idx = 2
i = 3

for folder in os.listdir(trainig_dir):
    # each folder is one video sequance
    path = trainig_dir+folder
    f_idx+= 1
    f_num = 1
    used_imgs=[]
    p1=[]
    p2=[]
    p3=[]

    # check how many objects in each sequance?
    full_path_txt,names_txt,dir_txt= filesNdirec(path,".txt")
    NumOfObj = len(names_txt)
    full_path_img,name_img,dir_img = filesNdirec(trainig_dir+folder,".png")
    NumOfImgs = len(name_img)

    for obj in range(0,NumOfObj):
        temp = open(full_path_txt[obj],'r')
        # print(full_path_txt[obj])
        annotations = []
        with open(full_path_txt[obj],'r') as f:
            for line in f:
                temp_anno= line.split(None)
                annotations.append(temp_anno[0])
                annotations.append(temp_anno[1])
                annotations.append(temp_anno[2])
        temp.close()

        for i in range(0,len(annotations)):
            annotations[i] = int(float(annotations[i]))

        annotation = np.reshape(annotations,((int(len(annotations)/3)),3))
        imgs = annotation[:,0]
        img_seq = 1
        for img in imgs:
            img_name = str(img).zfill(5)
            image = Image.open("{0}/{1}.png".format(dir_txt[obj],img_name))
            width, height = image.size
            image.close
            output_file = open("{0}/{1}_{2}.txt".format(dir_txt[obj],img_name,obj),"w")
            output_file.write("3,{0},{1},{2},1,{3},{4},{5},50,50,{6}\n".format(f_idx,img_seq+3,obj,f_num,width,height,dir_txt[obj]))
            output_file.close
            img_seq =+ 1
        
        counter = 0
        used_imgs = [] 
        for img in imgs: 
            img_name = str(img).zfill(5)
            used_imgs.append("{0}/{1}.png".format(dir_txt[obj],img_name))
            counter =+ 1
    
        p1,p2,p3 = filesNdirec(dir_txt[obj],".png")

    result = [m for m in p1 if not m in used_imgs or used_imgs.remove(m)]
    for files in result:
        os.remove(files)

    # i is 3, f_idx, k img_seq start at 3, object numb ,track id, class_name , img.width, img.hieght,bboxw,bbxh, im.path

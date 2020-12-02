import os
import ipyplot
import numpy as np
import pandas as pd
import cv2
DATA_PATH = "/home/delll/fga/veiculos_autonomos/datasets/PKLot/PKLotSegmented"
NEW_DATA_PATH = "/home/delll/fga/veiculos_autonomos/datasets/PKLot/ready2go/"


def pad_image(img, bigger_w, bigger_h):
    
    padding_sides = (bigger_w - img.shape[0])/ 2
    if(padding_sides.is_integer() ==  False):
        padding_sides = int(padding_sides - 0.5)
    else:
        padding_sides = int(padding_sides)

    padding_top = (bigger_h - img.shape[1])/2    
    if(padding_top.is_integer() ==  False):
        padding_top = int(padding_top - 0.5)
    else:
        padding_top = int(padding_top)

    result = np.ones([bigger_w, bigger_h, 3])
    result[padding_sides: padding_sides+img.shape[0], padding_top: padding_top + img.shape[1]] = img
    return result




def read_dataset_dir(parkinglot_name, weather, bigger_w, bigger_h, new_images_path):
    images_path = DATA_PATH + "/"+ parkinglot_name + "/" + weather + "/"

    for date in os.listdir(images_path):
        dir_info_list= []

        for state in os.listdir(images_path + date +"/"):

            for file in os.listdir(images_path + date +"/" + state):
                # path to image file
                
                file_path = images_path + date +"/" + state + "/" + file
                new_file_path = os.path.join(new_images_path , file)

                img = cv2.imread(file_path)
                # make padding and save image
                new_img = pad_image(img, bigger_w, bigger_h)  
                cv2.imwrite(new_file_path, new_img)
                dir_info_list.append([ new_file_path,  parkinglot_name, date, weather,  state ])
                
                # should be changed to a log function
                print("Leitura da imagem com sucesso: ", new_file_path.split("/")[-1],  parkinglot_name, date, weather, state)
    return dir_info_list


# Maiores dimencoes ja levantadas
bigger_w = 176
bigger_h = 93


puc_cloudy = read_dataset_dir("PUC", "Cloudy", bigger_w, bigger_h, NEW_DATA_PATH)
puc_sunny = read_dataset_dir("PUC", "Sunny", bigger_w, bigger_h, NEW_DATA_PATH)
puc_rainy = read_dataset_dir("PUC", "Rainy", bigger_w, bigger_h, NEW_DATA_PATH)

UFPR04_cloudy = read_dataset_dir("UFPR04", "Cloudy", bigger_w, bigger_h, NEW_DATA_PATH)
UFPR04_sunny  = read_dataset_dir("UFPR04", "Sunny", bigger_w, bigger_h, NEW_DATA_PATH)
UFPR04_rainy  = read_dataset_dir("UFPR04", "Rainy", bigger_w, bigger_h, NEW_DATA_PATH)            

UFPR05_cloudy = read_dataset_dir("UFPR05", "Cloudy", bigger_w, bigger_h, NEW_DATA_PATH)
UFPR05_sunny = read_dataset_dir("UFPR05", "Sunny", bigger_w, bigger_h, NEW_DATA_PATH)
UFPR05_rainy = read_dataset_dir("UFPR05", "Rainy", bigger_w, bigger_h, NEW_DATA_PATH)    


info_list = puc_sunny + puc_cloudy + puc_rainy + UFPR04_cloudy + UFPR04_sunny + UFPR04_rainy + UFPR05_cloudy + UFPR05_sunny + UFPR05_rainy


df = pd.DataFrame(data=info_list, columns=["relative_path", "parkinglot_name",	"date",	"weather", "status"])



df.to_csv("save_ue.csv")







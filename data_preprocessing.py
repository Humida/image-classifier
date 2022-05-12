import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import cv2

def images_path(label):
    paths = []
    for i in range(1, 1001):
        index_image = str(100000 + i)[1:]
        path_image = f"./data/{label}/{label}_{index_image}.jpg"
        paths.append(path_image)
    return paths

def read_images(paths):
    data_store = []
    for path in paths:
        image = cv2.imread(path)
        image_resize = cv2.resize(image, (256, 256), interpolation = cv2.INTER_AREA)
        image_gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
        image_element = {
            path.split('/')[2]: image_gray
        }
        data_store.append(image_element)
    return data_store

def store_data(data, label):
    data_train = data[0:len(data*0.7)]
    data_test = data[len(data*0.7+1):]
    label_train = label[0:len(label*0.7)]
    label_test = label[label*0.7+1:]




def data_processing():
    cats_path = images_path('cats')
    dogs_path = images_path('dogs')
    panda_path = images_path('panda')

    dogs_image = read_images(dogs_path)
    cats_image = read_images(cats_path)
    panda_image = read_images(panda_path)

    images = dogs_image + cats_image + panda_image
    random.shuffle(images)
    data_images = [list(item.values())[0] for item in images]
    label = [list(item.keys())[0] for item in images]
    # data = {
    #     'image': data_image,
    #     'label': label
    # }
    data_csv = pd.DataFrame( data = data_images, columns= ['image', 'label'])
    data_csv.to_csv("data.csv")
    return

data, label = data_processing()












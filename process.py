import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def getTrainData():
    # max1, min1, max2, min2 = 0,1000,0,1000
    X_color = []
    count = 0
    directory = r'C:\Users\abina\Desktop\Coding\CS Projects\FakeUrGramML\artworks\resized\resized'
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            imgpath = os.path.join(directory, filename)
            image = Image.open(imgpath).convert("L")
            
            # print(data.shape)
            width, height = image.size 

            if(width >= 300 and height >= 300):
                print(os.path.join(directory, filename))
                left = width/2 - 150
                right = width/2 + 150
                top = height/2 - 150
                bottom = height/2 + 150
                image = image.crop((left, top, right, bottom))

                data = np.asarray(image)
                if(len(data.shape) == 2):
                    count+=1
                    data = data.flatten()
                    data = data/255 * 2 - 1
                    X_color.append(data)
                    # print(count, data.shape)
                    #print(data)
                # if count == 1:
                #     image.show()
                #     break
        else:
            continue

    X_color = np.asarray(X_color, dtype = np.float32)

    # img = Image.fromarray(X_color[999].reshape(300,300,3), 'RGB')
    # img.show()
    print(X_color.shape)
    return X_color
getTrainData()

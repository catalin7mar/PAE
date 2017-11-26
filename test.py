import classer_service
import os
if __name__ == '__main__':
    #Pfad fuer bild angeben
    imagepath='/Users/CatalinVasilescu/Desktop/imager.jpg'
    l=classer_service.getImageList(imagepath)
    print('Test: Label und Score der 5 hauefigsten treffer fuer: ',imagepath)
    for index in range(l.__len__()):
        print(l[index])
    os.system("pause")

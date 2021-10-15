
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
import cv2

def captcha(img):

  resultado=[]
  
  grayscaled= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  retva1, threshold2= cv2.threshold(grayscaled,230,255,cv2.THRESH_BINARY_INV)

  contornos=cv2.findContours(threshold2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

  for i in range(len(contornos)):
    threshold2= cv2.drawContours(threshold2, contornos,i,(0,0,0),1)

  threshold2=cv2.rectangle(threshold2,(0,0),(150,100),color=(255,255,255),thickness=2)

  contornos=cv2.findContours(threshold2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
  contornos_rec=[]
  x_orden=[]
            
  for i in range(len(contornos)):
    x_max= contornos[i][0][0][0]
    x_min= contornos[i][0][0][0]
    y_max= contornos[i][0][0][1]
    y_min= contornos[i][0][0][1]
              
    for punto in contornos[i]:
      if x_max<punto[0][0]:
        x_max=punto[0][0]
      if x_min>punto[0][0]:
        x_min=punto[0][0]
      if y_max<punto[0][1]:
        y_max=punto[0][1]
      if y_min>punto[0][1]:
        y_min=punto[0][1]

    if (y_max-y_min) >= 20 and (y_max-y_min)<45:
      contornos_rec.append((x_min,x_max,y_min,y_max))
      x_orden.append(x_min)
  x_orden1=np.argsort(x_orden)

  for i in x_orden1:
    x_min,x_max,y_min,y_max= contornos_rec[i]
    img_char=threshold2[y_min:y_max, x_min:x_max]

    resultado.append(img_char)

  return resultado,threshold2
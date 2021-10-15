import tensorflow as tf
import matplotlib.pyplot as plt
import os

carpeta = os.listdir('CNN_capcha/Train')

for c in carpeta:
  print("Entrenamiento para el caracter", c)
  contenido = os.listdir('CNN_capcha/Train/'+c)
  fig, ax = plt.subplots(6, 5,  figsize=(12,8))
  j=0
  k=0
  for i in range(36):
    file_img=tf.io.read_file("CNN_capcha/Train/"+c+"/"+contenido[i])
    img=tf.image.decode_jpeg(file_img)
  
    if j<5:
      ax[k,j].axis('off')
      ax[k,j].imshow((img[:,:,0]),cmap='gray')
      j=j+1
    else:
      j=0
      k=k+1
  plt.subplots_adjust(left=0.1,
                      bottom=0.1, 
                      right=0.4, 
                      top=0.8, 
                      wspace=0.0, 
                      hspace=0.1)
  plt.savefig("CNN_capcha/Views/"+str(c)+".png")
#Para centralizar imagens, e cropar num quadrado

from PIL import Image
import os


global n
n = 0
#caminho da foto
folder_path = "Finger/zap/fotos/"
fotos = os.listdir(folder_path)
i = len(fotos)
def make_square(im, min_size=2, fill_color=(255,255,255)):
    x, y = im.size
    size = max(min_size, x, y)    
    new_im = Image.new('RGB',(size,size), fill_color)
    new_im.paste(im,(int((size-x)/2),int((size-y)/2)))
    return new_im


for n in range(i):
    print(fotos[n])
    test_image = Image.open(folder_path + fotos[n])
    new_image = make_square(test_image,fill_color=(255,255,255))
    n = n+1
#pasta em que a foto será salva
    new_image.save('fotos/' + fotos[n])



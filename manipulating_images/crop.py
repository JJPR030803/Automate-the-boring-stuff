from PIL import Image
catIm = Image.open('gatooo.png')
croppedIm = catIm.crop((335,345,565,560))
croppedIm.save('cropped.png')
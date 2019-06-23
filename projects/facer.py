import os
import face_recognition
from PIL import Image

x=[]
y=[]


image = face_recognition.load_image_file("sundarpichai.jpg")
image_enc = face_recognition.face_encodings(image)[0]
dir_image = os.listdir("images")

for i in dir_image:
    images_in_dir = face_recognition.load_image_file('images/'+i)
    images_in_dir_enc = face_recognition.face_encodings(images_in_dir)[0]
    res = face_recognition.compare_faces([images_in_dir_enc],image_enc)
    
    if res[0] == True:
        x.append(i)
       
    else:
        y.append(i)

t='\n'.join(x)
f='\n'.join(y)
l=len(x)
n=str(l)

print("Total images matched:" +n+ "\n\nMatched with:\n\n" +t+ '\n')
print("Could not match with:\n\n" +f+ "\n\n")

for p in x:
    
    if os.path.exists(p)==True:
        print("Images printed on screen\n")
        img=Image.open(p)
        img.show()
        
    else:
        a=os.path.join('images',p)
        img = Image.open(a)
        img.show()
        
        

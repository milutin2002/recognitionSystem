import cv2
import numpy as np
import face_recognition
cam=cv2.VideoCapture(0)
model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
name=input("Enter your name: \n")
s=0
offset=30
faceData=[]
count=0
while True:
    suc,img=cam.read()
    if not suc:
        print("Camera read failed")
        break
    faces=model.detectMultiScale(img,1.3,2)
    if len(faces)>0:
        faces=sorted(faces,key=lambda f:f[2]*f[3])
        x,y,h,w=faces[-1]
        croppedFace=img[y-offset:y+h+offset,x-offset:x+w+offset]
        croppedFace=cv2.resize(croppedFace,(150,150))
        rgbFace=cv2.cvtColor(croppedFace,cv2.COLOR_BGR2RGB)
        encodings=np.array(face_recognition.face_encodings(rgbFace))
        cv2.imshow("Lice", croppedFace)
        if len(encodings) >0 and encodings.shape[0]==1 and encodings.shape[1]==128 and s % 10 == 0:
            faceData.append(encodings)
            print(s//10)
            print(encodings.shape)
            count=count+1
            #print("Saved so far "+str(len(encodings)))
        s = s + 1
    #cv2.imshow("Image windows",img)
    if count==20:
        break
filename="./data/"+name+".npy"
faceData=np.asarray(faceData)
m=faceData.shape[0]
print("Facedata shape is "+str(faceData.shape))
print("S is equal to "+str(s//10+1))
faceData=faceData.reshape((count,-1))
np.save(filename,faceData)
cam.release()
cv2.destroyAllWindows()
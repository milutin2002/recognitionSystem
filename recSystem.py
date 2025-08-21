import cv2
import numpy as np
import os
import face_recognition
datasetPath="./data/"
faceData=[]
labels=[]
id=0
namemap={}
for f in os.listdir(datasetPath):
    if f.endswith(".npy"):
        namemap[id]=f[:-4]
        dataItem=np.load(datasetPath+f)
        m=dataItem.shape[0]
        faceData.append(dataItem)
        print(dataItem.shape)
        target=int(id)*np.ones((m,))
        id+=1
        labels.append(target)
X=np.concatenate(faceData,axis=0)
y=np.concatenate(labels,axis=0).reshape((-1,1))
print(X.shape)
print(y.shape)
print(namemap)
offset=20
def dist(p,q):
    return np.sqrt(np.sum((p-q)**2))

def knnPredict(X,y,xt,k=5):
    m=X.shape[0]
    dlist=[]
    for i in range(m):
        d=dist(X[i],xt)
        dlist.append((d,y[i][0]))
    dlist=sorted(dlist)
    dlist=np.array(dlist[:k])
    l=dlist[:,1]
    l,cnt=np.unique(l,return_counts=True)
    idx=cnt.argmax()
    pred=l[idx]
    return int(pred)
cam=cv2.VideoCapture(0)
try:
    model=cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    while True:
        suc,img=cam.read()
        if not suc:
            print("Camera read failed")
            break
        faces=model.detectMultiScale(img,1.3,5)
        for f in faces:
            try:
                faces=sorted(faces,key=lambda z:z[2]*z[3])
                x,yy,h,w=f
                croppedFace=img[yy-offset:yy+h+offset,x-offset:x+w+offset]
                croppedFace=cv2.resize(croppedFace,(150,150))
                rgbFace = cv2.cvtColor(croppedFace, cv2.COLOR_BGR2RGB)
                encodings = np.array(face_recognition.face_encodings(rgbFace))
                if encodings.shape[0]==1 and encodings.shape[1]==128:
                    clas=knnPredict(X,y,encodings)
                    cv2.rectangle(img,(x,yy),(x+w,yy+h),(0,255,0),2)
                    cv2.putText(img,namemap[clas],(x,yy-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
            except Exception:
                pass
        cv2.imshow("Video",img)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    cam.release()
except KeyboardInterrupt:
    cam.release()
cv2.destroyAllWindows()

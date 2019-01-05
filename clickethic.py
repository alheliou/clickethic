import numpy as np
import cv2
import os, time
import face_recognition
from PIL import Image


def changes(path_to_watch,before):
    while 1:
        time.sleep (1)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        if added: 
            return added,after

def picture_capture(cap):
     # video capture source camera (Here webcam of laptop) 
    for i in range(10):
        ret,frame = cap.read() # return a single frame in variable `frame`
    return frame


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    prenom = input("Entrez votre prénom: ")
    frame=picture_capture(cap)
    nom = input("Entrez votre nom: ")
    path_to_watch0="/Users/aliceheliou/Documents/MIU/download/"+prenom+"\ "+nom
    path_to_watch="/Users/aliceheliou/Documents/MIU/download/"+prenom+" "+nom
    os.system("if [ -d "+path_to_watch0+" ]; then rm -r "+path_to_watch0+"; fi; mkdir "+path_to_watch0)
    Arguments='python3 google_images_download.py -k "'+prenom+' '+nom+'" -l 50 -o /Users/aliceheliou/Documents/MIU/download/'
    cmd='cd /Users/aliceheliou/Documents/MIU/download-images/google_images_download/ ;'+Arguments+' > out1.tmp &'
    os.system(cmd)

    before = dict ([(f, None) for f in os.listdir(path_to_watch)])

    Image_file='/Users/aliceheliou/Documents/MIU/known_people/'+prenom+' '+nom+'.png'
    cv2.imwrite(Image_file,frame)

    picture_of_you = face_recognition.load_image_file(Image_file)
    your_face_encoding = face_recognition.face_encodings(picture_of_you)[0]
    
    nb=0
    res=0
    #imgs=[]
    
    while (nb<49):
        list_images, after=changes(path_to_watch, before)
        for images in list_images:
            unknown_picture = face_recognition.load_image_file(path_to_watch+"/"+images)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
            if len(unknown_face_encoding)>0:
                results = face_recognition.compare_faces([your_face_encoding], unknown_face_encoding[0])
                if results[0] == True:
                    #print("Est-ce vous sur cette image ?")
                    if res==0:
                        cap.release()
                    try :
                        cmd="open -a Preview "+path_to_watch0+"/"+images.replace(" ", "\ ")
                        os.system(cmd)
                    except :
                        print("erreur d'ouverture")
                    #imgs.append(cv2.imread(path_to_watch+"/"+images))
                        #cv2.imshow('image'+str(res), imgs[res])
                        #imgs.append(Image.open(path_to_watch+"/"+images))
                        #imgs[res].show("image"+str(res))
                    res=res+1
            nb=nb+1
        before=after
    print(str(res)+" images de vous ont été trouvées.")
    os.system(cmd)
    
    cv2.destroyAllWindows()



#cmd='face_recognition /Users/aliceheliou/Documents/MIU/known_people/ /Users/aliceheliou/Documents/MIU/download/'+prenom+'\ '+nom+'> out2.tmp'
#os.system(cmd)

#cmd='grep ",'+prenom+' '+nom+'" out2.tmp'
#os.system(cmd)

#img = Image.open('picture.jpg')
#img.show()
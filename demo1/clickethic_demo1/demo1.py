"""
Copyright (C) 2019  Alice Héliou, alice.heliou@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import numpy as np
import cv2
import os, time
import face_recognition
from PIL import Image
import configparser

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

"""This funtion set the directories used to store pictures"""
def set_config():
    saved_picture_dir = input("Entrez le chemin absolu pour saved_picture_dir: ")
    google_picture_dir = input("Entrez le chemin absolu pour google_picture_dir: ")
    config = configparser.ConfigParser()
    config["paths"]={}
    config["paths"]["saved_picture_dir"]=saved_picture_dir
    config["paths"]["google_picture_dir"]=google_picture_dir
    with open('configurations.cfg', 'w') as configfile:
       config.write(configfile)

"""This funtion print the directories used to store pictures"""
def get_config():
    my_conf = configparser.ConfigParser()
    my_conf.read('configurations.cfg')
    saved_picture_dir=my_conf["paths"]["saved_picture_dir"]
    google_picture_dir=my_conf["paths"]["google_picture_dir"]
    print(saved_picture_dir)
    print(google_picture_dir)

"""This function runs demo1"""
def demo1(nb_pictures=50):
    my_conf = configparser.ConfigParser()
    my_conf.read('configurations.cfg')
    saved_picture_dir=my_conf["paths"]["saved_picture_dir"]
    google_picture_dir=my_conf["paths"]["google_picture_dir"]
    print(saved_picture_dir)
    cap = cv2.VideoCapture(0)
    prenom = input("Entrez votre prénom: ")
    frame=picture_capture(cap)
    nom = input("Entrez votre nom: ")
    path_to_watch0=google_picture_dir+prenom+"\ "+nom
    path_to_watch=google_picture_dir+prenom+" "+nom
    os.system("if [ -d "+path_to_watch0+" ]; then rm -r "+path_to_watch0+"; fi; mkdir "+path_to_watch0)
    Arguments='googleimagesdownload -k "'+prenom+' '+nom+'" -l '+str(nb_pictures)+' -o '+google_picture_dir
    cmd=Arguments+' > out1.tmp &'
    os.system(cmd)

    before = dict ([(f, None) for f in os.listdir(path_to_watch)])

    Image_file=saved_picture_dir+prenom+' '+nom+'_taken.png'
    print(Image_file)
    cv2.imwrite(Image_file,frame)

    picture_of_you = face_recognition.load_image_file(Image_file)
    your_face_encoding = face_recognition.face_encodings(picture_of_you)[0]
    
    nb=0
    res=0
    
    while (nb<nb_pictures):
        list_images, after=changes(path_to_watch, before)
        for images in list_images:
            unknown_picture = face_recognition.load_image_file(path_to_watch+"/"+images)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
            if len(unknown_face_encoding)>0:
                results = face_recognition.compare_faces([your_face_encoding], unknown_face_encoding[0])
                if results[0] == True:
                    if res==0:
                        cap.release()
                    try :
                        cmd="open -a Preview "+path_to_watch0+"/"+images.replace(" ", "\ ")
                        os.system(cmd)
                    except :
                        print("erreur d'ouverture")
                    res=res+1
            nb=nb+1
        before=after
    print(str(res)+" images de vous ont été trouvées.")
    os.system(cmd)
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    demo1()


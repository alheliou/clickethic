# Demo 1 : Face recognition

Petite démo permettant de trouver sur Google les photos correspondant au nom de l'utilisateur et ressemblant à sa photo

## Requirements

Should work for Linus and Mac, not sure for Windows
* Python 3 (see https://www.python.org/downloads/)
* opencv:
    https://docs.opencv.org/master/df/d65/tutorial_table_of_content_introduction.html

* google_images_download:
    https://github.com/hardikvasa/google-images-download
    
    `python3 -m pip install google_images_download`

* face_recognition:
    https://github.com/ageitgey/face_recognition
    
    `python3 -m pip install face_recognition`

## Easy install (ne marche pas encore)

`python3 -m pip install --index-url https://test.pypi.org/simple/ demo_1_face_recognition`

Mais il risque d'y avoir un soucis avec les confs

## Installation classique

* Installer les requirements

* Télécharger le dossier

    `git clone https://github.com/alheliou/clickethic.git Clickethic`

* Se placer dans le bon dossier

    `cd Clickethic/demo1/face_recognition`

* Modifier les dossier où télécharger les images dans configurations.cfg

* Lancer la démo

    `python3 clickethic.py`
    
## Configurations
You need to update the two variables of configurations.cfg



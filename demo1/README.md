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

## Easy install 

* Installer opencv, et les autres requirements (les requirements de type python pourront bientot etre installés automatiquement, mais pas encore)

* Installer la démo

    `python3 -m pip install --index-url https://test.pypi.org/simple/ clickethic_demo1`

* Importer le package

    `python3`

        import clickethic_demo1
        from clickethic_demo1 import demo1
        demo1.set_config()
        demo1.demo1()

    Par défault la démo se lance sur 50 images, mais si on demande demo1.demo1(10), elle se lancera sur 10 images

## Installation classique

* Installer les requirements

* Télécharger le dossier

    `git clone https://github.com/alheliou/clickethic.git Clickethic`

* Se placer dans le bon dossier

    `cd Clickethic/demo1/clickethic_demo1`

* Modifier les dossier où télécharger les images dans configurations.cfg, et se placer à l'endroit où est se fichier

* Lancer la démo

    `python3 demo1.py`
    
## Configurations
You need to update the two variables of configurations.cfg



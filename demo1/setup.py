import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo_1_face_recognition",
    version="0.0.1",
    author="Alice Héliou",
    author_email="alice.heliou@thales-services.fr",
    description="Petite démo permettant de trouver sur Google les photos correspondant au nom de l'utilisateur et ressemblant à sa photo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
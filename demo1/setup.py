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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements=[
    'face_recognition',
    'numpy',
    'Pillow',
    'google_images_download',

]

setuptools.setup(
    name="demo_1_face_recognition",
    version="0.0.2",
    author="Alice Héliou",
    author_email="alice.heliou@gmail.com",
    description="Petite démo permettant de trouver sur Google les photos correspondant au nom de l'utilisateur et ressemblant à sa photo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alheliou/clickethic/demo1",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

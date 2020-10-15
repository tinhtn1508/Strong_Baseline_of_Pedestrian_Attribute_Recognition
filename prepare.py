import os
import subprocess

ROOT_PATH = subprocess.getoutput("pwd")
REPOS_PATH = ROOT_PATH + "/Strong_Baseline_of_Pedestrian_Attribute_Recognition"
PA100K_PATH = REPOS_PATH + "/data"
REPOS_LINK = "https://github.com/tinhtn1508/Strong_Baseline_of_Pedestrian_Attribute_Recognition.git"

# PA-100K dataset
annotationLink = "https://drive.google.com/uc?id=0B5_Ra3JsEOyOOWdHcUx5eVVvMW8"
dataLink = "https://drive.google.com/uc?id=0B5_Ra3JsEOyOZ1BVN09XQ2xXbFU"
annotationName = "/content/annotation.zip"
dataName = "/content/data.zip"

# Cloning repos
if not os.path.isdir(REPOS_PATH):
    os.system("git clone {}".format(REPOS_LINK))

# unzip
if not os.path.isdir(PA100K_PATH):
    os.system("mkdir -p {}".format(PA100K_PATH))
    os.system("gdown {}".format(annotationLink))
    os.system("gdown {}".format(dataLink))
    os.system("unzip {} -d {}".format(annotationName, "/content/PA100k"))
    os.system("unzip {} -d {}".format(dataName, "/content/PA100k"))
    os.system("mv {} {}".format("/content/PA100k/release_data/release_data", "/content/PA100k/data"))
    os.system("rm -rf {}".format("/content/PA100k/release_data"))
    os.system("mv /content/PA100k {}".format(PA100K_PATH))

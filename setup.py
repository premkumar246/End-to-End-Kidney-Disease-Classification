import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "End-to-End-Kidney-Disease-Classification"
AUTHOR_USER_NAME = "premkumar246"
SRC_REPO = "Kidney_Disease_Classification_App"
AUTHOR_EMAIL = "sanamalapremkumar@gmail.com"

setuptools.setup(

    name = SRC_REPO, 
    version= __version__, 
    author = AUTHOR_USER_NAME, 
    description= "This repository holds all the project files belongs to a Kidney diesease classification application which takes x-rays images and classify the image as dieseased or healthy by using Deep learning CNN classification techniques.", 
    long_description= long_description, 
    long_description_content_type= "text/markdown",
    url = f"https://github.com/premkumar246/End-to-End-Kidney-Disease-Classification.git", 
    project_urls = {
        "Bug Tracker" : f"https://github.com/premkumar246/End-to-End-Kidney-Disease-Classification.git"
    }, 
    package_dir={ "":"src"}, 
    packages=setuptools.find_packages(where="src")

)
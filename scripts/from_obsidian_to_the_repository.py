import os, shutil, re

"""
1. argiuments:
    - path to the file with presentation
    - path to the images:
        - generate a dictionary of subfolder/filename:fullPath
2. copy to the repository:
    - main html
    - main md:
        - update paths to images
    - all images
"""


pathToVault = "/Users/romanov/Dropbox/0_Zettelkasten/research_vault/"
pathToPresentations = pathToVault + "/0.presentations/"
pathToAttachments   = pathToVault + "/attachments/"

targetFolder = "/Users/romanov/Dropbox/_EIS1600_Working/github_repositories/presentations/"



files = os.listdir(pathToPresentations)

for f in files:
    if f.endswith(".html"):
        print(f)
        presentation = f.split(".")[0]
        print(presentation)

        if not os.path.exists(targetFolder + "/images/"):
            os.makedirs(targetFolder + "/images/")

        with open(pathToPresentations + f, "r", encoding="utf8") as f1:
            data = f1.read()#.replace(presentation, "index")
            #data = data.replace("style.css", "../style.css")
            #data = data.replace('<script src="remark-latest.min.js"></script>', '<script src="../remark-latest.min.js"></script>')

            # find all images
            for i1 in re.findall(r"(\.\./attachments/[^\"\) ]+)", data):
                i2 = "/images/" + i1.split("/")[-1]
                #print(i1)
                #print(i2)
                shutil.copy(pathToVault + i1[2:], targetFolder + i2.strip())
                print("\t", i1, " > ", i2)

                #input()

                data = data.replace(i1, "." + i2)
                #input(i2)
            # copy all images
            # update all paths in MD

            # save the updated MD
            with open(targetFolder + f, "w", encoding = "utf8") as f9:
                f9.write(data)


        


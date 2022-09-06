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
    if f.startswith("2") and f.endswith(".html"):
        print(f)
        presentation = f.split(".")[0]
        print(presentation)

        if not os.path.exists(presentation):
            os.makedirs(presentation)
        if not os.path.exists(presentation + "/images/"):
            os.makedirs(presentation + "/images/")

        with open(pathToPresentations + f, "r", encoding="utf8") as f1:
            data = f1.read().replace(presentation, "index")
            data = data.replace("style.css", "../style.css")

            with open(targetFolder + presentation + "/index.html", "w", encoding="utf8") as f9:
                f9.write(data)

        with open(pathToPresentations + presentation + ".md", "r", encoding = "utf8") as f1:
            mdData = f1.read()

            # find all images
            for i1 in re.findall(r"(\.\./attachments/[^\"\) ]+)", mdData):
                i2 = "/images/" + i1.split("/")[-1]
                shutil.copy(pathToVault + i1[2:], targetFolder + presentation + i2.strip())
                print("\t", i1, " > ", i2)

                mdData = mdData.replace(i1, "." + i2)
                #input(i2)
            # copy all images
            # update all paths in MD

            # save the updated MD
            with open(targetFolder + presentation + "/index.md", "w", encoding = "utf8") as f9:
                f9.write(mdData)


        


import os


def search():
    for folder, subfolders, files in os.walk(input("\n Directory to search thru: \n")):
        print(folder)
        for subfolders in subfolders:
            print(subfolders)
            for file in files:
                print(file)

                

               

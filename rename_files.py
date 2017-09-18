import os
#The reserved word=> def is for defining a function followed of  the name of funcition
def rename_files() :
    #(1) get files names from a folder
    file_list = os.listdir(r"C:\Users\Anys\Documents\python\secretMessage\prank")
    #print (file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is"+saved_path)
    os.chdir(r"C:\Users\Anys\Documents\python\secretMessage\prank")

    #(2)for each file, rename filename
    for filename in file_list :
        print("Old name - "+filename)
        os.rename(filename, filename.translate(None, "0123456789"))
rename_files()

import os
#The reserved word=> def is for defining a function followed of  the name of funcition
def rename_files() :
    #(1) get files names from a folder
    file_list = os.listdir(r"C:\Users\Anys\Documents\python\secretMessage\prank")
    print (file_list)
    #(2)for each file, rename filename
rename_files()

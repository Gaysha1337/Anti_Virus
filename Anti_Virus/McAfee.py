import os, time, sys, shutil
dir_to_remove = "C:\\Users\\dimit\\Desktop\\Anti_Virus\\Files"
original_file_path = "C:\\Users\\dimit\\Desktop\\Anti_Virus\\Files"
path = "C:\\Users\\dimit\\Desktop\\Archivos_Importante"
destination = "C:\\Users\\dimit\\Desktop\\Anti_Virus\\Files" #"C:\\Users\\dimit\\Desktop\\Archivos_Importante\\Copy"
dirs = os.listdir(path) #Get the dirs and files with path as an arg
"""
os.chdir(original_file_path)
os.rmdir(dir_to_remove)
os.mkdir("Files")
"""
os.chdir(path)
files = [] #Empty list where we will store the files

def loop_files(path):
    #loop each file in dirs, then prints it and appends it to files list
    for file in dirs:
        files.append(file)
    shutil.move(path, destination)
    print("We have moved your files")

print(os.getcwd() + "\n We are in your important directory")
os.system("ECHO We are installing software")
#Seconds to sleep
time.sleep(4)
os.system("ECHO Get rekted we have ur files")

try:
    loop_files(path)
except PermissionError:
    time.sleep(4)
    print(files)
    QUIT = input("U have been hacked, if you wanna remove this screen type anything")
    time.sleep(5)





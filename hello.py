import shutil
import os
import pdb
import random
import string

dicted = "NSDictionary *dic = @{"

# get all directory files
def getResourcePath(targetpath):
    # print("=====================Find all Files=========================")
    filelist = []
    # pdb.set_trace()
    os.listdir(targetpath)
    for fileName in os.listdir(targetpath):
        filePath = targetpath + '/' + fileName
        # print(filePath)
        if os.path.isdir(filePath):
            renameDir(filePath)
            files = getResourcePath(filePath)
            filelist.extend(files)
        else:
            
            if "DS_Store" in filePath:
                print("============" + filePath)
            else:
                filelist.append(filePath)            
    return filelist

       
# move file of files to dir
def moveFiles(files,dir):
    print("=====================Move Files=========================")
    for filePath in files:
        # print("files:"+filePath + "->" + "newPath:"+dir)
        pathFileName = os.path.basename(filePath)
        if not os.path.exists(dir + '/' + pathFileName):
            shutil.move(filePath,dir)
        else:
            print("======================================================path:"+ filePath)
                

# rename all files of dir
def renameDir(dir):
    print("=====================Randomly renamed=========================")
    files = os.listdir(dir)
    dic = ""
    for fileName in files:
        # print("fileName:"+ fileName + '\n')
        oldFilename = dir + '/' + fileName;
        suffix = os.path.splitext(oldFilename)[-1]
        salt = ''.join(random.sample(string.ascii_letters + string.digits, len(fileName) - len(suffix))) # ramdom
        newFileName = dir + '/' + salt + suffix;
        # print(fileName +'->' + salt + suffix);
        if not os.path.isdir(oldFilename):
            os.rename(oldFilename,newFileName)
        dic = dic + "@\"" +oldFilename.split(os.getcwd() + "/Demo")[1] + "\"" + ":" + "@\"" + salt + suffix + "\"" + ",\n"

    print("dic:" + dic);
    global dicted    
    dicted = dicted + dic; 
#   return "fa"
    

def writeFile():
    global dicted    
    dicted = dicted + "};"
    try:
		file_object = open(os.getcwd() + "/log.txt", "w")
		file_object.write(dicted)
		file_object.close()
    except IOError:
        print("write file failed! file: ")    


def main():
    print("this main run")
    dir = os.getcwd() + "/Demo"
    files = getResourcePath(dir)
    # print(files)
    moveFiles(files,dir)
    # renameDir(dir)  
    writeFile()
    print("=====================sucesssul!!!!=========================")



if __name__ == "__main__":
	main()
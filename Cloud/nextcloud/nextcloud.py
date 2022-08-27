
import sys
#import time
#import random
#import datetime
#import shlex
#import subprocess
import os
#import re
#import signal


mUsername = "Doyfmjb6N3pj6xnB"
mPassword = "demo"
    
def nextcloudUpload(nextcloudPath, localFilePath):
    #print("Nextcloud path: ", nextcloudPath)  #https://demo2.nextcloud.com/index.php/apps/files/?dir=/%E3%83%86%E3%82%B9%E3%83%88&fileid=23163452
    #print("Local file path: ", localFilePath, "\n") #myfile.zip

    startPattern = "index.php/apps/files/?dir="
    endPattern = "&fileid="
    
    pos1 = nextcloudPath.find(startPattern)
    pos2 = nextcloudPath.rfind(endPattern)
    
    if not (pos1 > 0 and pos2 > pos1) :
        print("Nextcloud path invalid !")
        return
    
    folderPath = nextcloudPath[pos1 + len(startPattern):pos2]
    if folderPath == '/':
        folderPath = ""

    uploadFimename = os.path.basename(localFilePath)
    nextcloudFile = nextcloudPath[0:pos1-1] + "/remote.php/dav/files/" + mUsername + "" + folderPath + "/" + uploadFimename
    cmd = "curl -u \"" + mUsername +":" + mPassword + "\" -T \"" +  localFilePath + "\" -X PUT \"" + nextcloudFile + "\""
    print("\n\n", cmd)
    #curl -u 'LTGdyrwMGACoJM4Y:demo' -T "myfile.zip" "https://demo2.nextcloud.com/remote.php/dav/files/LTGdyrwMGACoJM4Y/%E3%83%86%E3%82%B9%E3%83%88/myfile.zip"
    
    
    #cmd = shlex.split("/bin/bash -c \"cp -rf " + logpath + " " + logpath_bak + "\"")
    #cmd = shlex.split("/bin/bash -c \"curl -u \"LTGdyrwMGACoJM4Y:demo\" -T " + localFilePath + " -X PUT " + nextcloudFile + "\"")
    #print("cmd: " + str(cmd))
    
    #curlcmd = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #curlcmd.wait()
    #curlcmd.stdout.readline()
 
    #for line in curlcmd.stdout:
        #print(line)
        
def main():
    if len(sys.argv) < 3 :
        print("Error: Input arguments invalid \nUsage:\n   nextcloud <\"nextcloud path\"> <\"upload file name\"> ")
        return
    nextcloudUpload(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
    
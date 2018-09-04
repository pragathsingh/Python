from __future__ import print_function
import os
import string
from ctypes import windll
import time
import sys

LocDic = {}
SizeDic = {}
notAccessable = []
drives = []
checksize = 0

index = 0


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


if __name__ == '__main__':
    temp = get_drives()
    for a in temp:
        drives.append(a + ':/')


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%0.03f %s " % (num, x)
        num /= 1024.0


folders = 0
value = 0
newdir = {}
info = {}
oncedir = []

def MakeList(dirname):
    global value
    global newdir
    global checksize
    tmpname = ""
    try:
        if(dirname not in oncedir): oncedir.append(dirname)
        else: return
        for x in os.listdir(dirname):
            try:
                tmpname = name = dirname + "/" + x
                if not os.path.isdir(name):
                    if name not in info:
                        info[name] = os.stat(name).st_size
                    else:
                        info[name] += os.stat(name).st_size
                    newdir[name] = os.stat(name).st_size
                    checksize += os.stat(name).st_size
                l.append(name)
            except WindowsError:
                notAccessable.append(tmpname)                

    except WindowsError:
        notAccessable.append(tmpname)
        #print dirname
    return l


for dr in drives:

    if (os.path.exists(dr)):

        if 'C:/' in dr:
            continue
        if 'G:/' in dr:
            continue
        if 'E:/' in dr:
            continue
        if 'F:/' in dr:
            continue

        for a in os.listdir(dr):
            name = dr + a
            folders += 1
            try:
                if os.path.isdir(name):
                    l = []
                    tmpDic = {}
                    l = MakeList(name)
                    tmpDic[name] = l
                    LocDic[index] = tmpDic
                    index += 1

                else:
                    checksize += os.stat(name).st_size



            except WindowsError:
                notAccessable.append(name)

print ('continue')
file = 0
size = 0
keys = 0
startTime = time.time()

tmpvar = 0
once = True
# lets say index is 10
print ('index: ', index)
print ('dic size : ', len(LocDic))
end = True

def checkitforme(v):
    
    global tmpvar
    global LocDic
    tDic = {} 
    
    l = MakeList(v)
    tDic[v] = l         
    return tDic

isdir = 0
LocDicCopy = LocDic
while (tmpvar != len(LocDic)):
    if LocDic[tmpvar] is not None:print(LocDic[tmpvar].keys)
    print (convert_bytes(checksize),end="")
    print("\b")
   
    # put an elemnt first then change the index
    try:
        tmpDic = LocDic[tmpvar]
        if tmpDic is not None:
            try:
                for key,value in tmpDic.items():
                    #if value.count >40000:
                    print( key,'\n')
                   # print key,'\n ',value
                    for v in value:
                        if os.path.isdir(v):
                            print(v)
                            isdir += 1
                            LocDic.update({len(LocDic):checkitforme(v)})
                        
            except WindowsError:
               ''
    except KeyError:
        if tmpvar > len(LocDic):
            break
    tmpvar +=1
    print(isdir,' : ',tmpvar,' : ',len(LocDic))
        # print LocDic[tmpvar]
        
    
       
#print ('compared : ' ,cmp(LocDic,LocDicCopy))
print (tmpvar)
print ('size of LocDic is '+str(len(LocDic)))

#print ('pc size is : ', convert_bytes(checksize))






import os
import string
from ctypes import windll
import time


LocDic = {}
SizeDic = {}
notAccessable =[]
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
        drives.append(a+':/')

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
def MakeList(dirname):
    global value
    global newdir
    global checksize
    try:
        for x in os.listdir(dirname):
            try:
                name = dirname+"/"+x
                if not os.path.isdir(name):
                    value += 1
                    if dirname not in info:
                        info[dirname] = os.stat(name).st_size
                    else:
                        info[dirname] += os.stat(name).st_size
                    newdir[name] = os.stat(name).st_size
                    checksize += os.stat(name).st_size
                l.append(name)
            except WindowsError:
                notAccessable.append(name)
                print name

    except WindowsError:
        notAccessable.append(dirname)
        print dirname
    return l


for dr in drives:
    global index
    if(os.path.exists(dr)):     
        
        if 'C:/' in dr:
            continue
        if 'G:/' in dr:
            continue
        if 'E:/' in dr:
            continue
        if 'F:/' in dr:
            continue        

        for a in os.listdir(dr):
            name = dr+a
            folders +=1
            try:        
                if os.path.isdir(name):                   
                    l = [] 
                    tmpDic = {}
                    l = MakeList(name)
                    tmpDic[name] = l
                    LocDic[index] = tmpDic
                    index +=1
                
                else:
                    checksize += os.stat(name).st_size
            
                

            except WindowsError:
                    notAccessable.append(name)
    
print 'continue'
file = 0
size = 0
keys = 0
startTime = time.time()

tmpvar = 0
once = True                        
#lets say index is 10
print 'index: ',index
print 'dic size : ',len(LocDic)
end = True
while( tmpvar != len(LocDic)): 
    #put an elemnt first then change the index 
    #if (tmpvar > index):
    tmpDic = LocDic[tmpvar]
    try:
        
        print tmpDic.values
        values = tmpDic.values
        for value in values:            
            l = MakeList(value)
            if l.count != 0:
                tDic = {value,l}
                LocDic[tmpvar+1] = tDic
                tmpvar+=1
    #print LocDic[tmpvar]    
    
    tmpvar +=1

"""
for value in LocDic.values():
    keys += 1   
    for v in value: 
        if(os.path.isdir(v)):
            if v not in LocDic:               
                folders += 1
                LocDic[v] = MakeList(v)  
"""
for key in notAccessable:
    print key

print 'counting started'
print 'pc size is : ',convert_bytes(checksize)
startTime = time.time()
tmpDir = {}
infosize = 0
for key in info:
    infosize += info[key]
    print key,'    size :  ',convert_bytes(info[key])

print convert_bytes(infosize)
totalfiles = 0
time.sleep(60)



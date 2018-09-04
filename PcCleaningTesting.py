import os
import string
from ctypes import windll
import time
LocDic = {}
SizeDic = {}
notAccessable =[]
drives = []
checksize = 0 
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
values = 0
newdir = {}
def MakeList(dirname):
    global values
    global newdir
    global checksize
    try:
        for x in os.listdir(dirname):
            name = dirname+"/"+x
            if not os.path.isdir(name):
                values += 1
                newdir[name] = os.stat(name).st_size
                checksize += os.stat(name).st_size
            l.append(name)
    except KeyError:
        ''
    except WindowsError:
        ''
        #notAccessable.append(dirname)    
    return l

for dr in drives:
    if(os.path.exists(dr)):     
        
        if 'D:/' in dr:
            continue
        if 'G:/' in dr:
            continue
        if 'C:/' in dr:
            continue
        if 'F:/' in dr:
            continue
        

        for a in os.listdir(dr):
            name = dr+a
            folders +=1
            print a,'\n Files : \n'
            try:        
                if os.path.isdir(name):                   
                    l = []             
                    l = MakeList(name)
                    LocDic[name] = l
                    for p in l:
                        print '      ',p ,'    size : ',convert_bytes(os.stat(p).st_size)
                else:
                    checksize += os.stat(name).st_size
            except WindowsError:
                notAccessable.append(name)
            except KeyError:                
                notAccessable.append(name)
    
print 'continue'
file = 0
size = 0
totalfiles = 0
keys = 0
"""
for key in LocDic:
         
    file +=1
    keysize = 0
    #print key 
    for v in LocDic[key]:  
        print v
        if os.path.isdir(v):                             
            LocDic[v] = MakeList(v)
            totalfiles += 1                  
            #tmpDir[value] = os.stat(value).st_size
            keysize += os.stat(v).st_size
        else:    
            checksize += os.stat(v).st_size
"""    

for value in LocDic.values():
    keys += 1   
    for v in value: 
        #if v.endswith(".mp4"):
        #    print convert_bytes(os.stat(v).st_size
        if(os.path.isdir(v)):
            if v not in LocDic:               
                folders += 1
                LocDic[v] = MakeList(v)  
        else:
            if v.endswith(".mp4"):
                print convert_bytes(os.stat(v).st_size)
            checksize += os.stat(v).st_size


print 'keys : ',keys
print 'folders : ',folders ,' , files : ',values
print 'counting started'
print 'pc size is : ',convert_bytes(checksize)
startTime = time.time()
tmpDir = {}
totalfiles = 0
time.sleep(120)

"""
startTime = time.time()
for key in newdir:
    size += newdir[key]
    if time.time()- startTime >= 10:
        print convert_bytes(size)
        startTime = time.time()

print convert_bytes(size)


for key in LocDic:
    file +=1
    keysize = 0
    for value in LocDic[key]:
        try: 
            if not os.path.isdir(value):                
                if value not in tmpDir:
                    #if value.endswith(".mp4"):
                    totalfiles += 1                  
                    tmpDir[value] = os.stat(value).st_size
                    keysize += os.stat(value).st_size
                    checksize += os.stat(value).st_size

            if time.time() - startTime >= 10:                
                print 'size is : ',convert_bytes(checksize),' , files : ',totalfiles,'   ',file
                startTime = time.time()
   
    
        except WindowsError:
            ''
    #for k in tmpDir:
     #   print k,'  ', convert_bytes(tmpDir[k])
      #  time.sleep(0.3)
            #print key ,'   ', convert_bytes(keysize)
try:
    for key in tmpDir:
        print key,'  ',convert_bytes(tmpDir[key])
    print convert_bytes(checksize), ' is the testing size of pc '
except KeyError:
    ''
totalPcSize = 0
"""
"""
print count

for key in LocDic:
    try:
        size = 0
        total = 0        
        for v in LocDic[key]:           
            enter = (os.path.isdir(v))
            enter != enter
            if (enter):
                size = os.stat(v).st_size            
                SizeDic[v] = size            
                total +=size
        totalPcSize += total
        SizeDic[key] = total        
    except WindowsError:
        notAccessable.append(value)

print 'Total pc size ',convert_bytes(totalPcSize)
files = 0
newSizeDic = {}

for key,value in LocDic.items():
    global filescount
    t = 0
    size = ''
    for v in value:     
        if v in SizeDic:            
            size = SizeDic[v]
            t += size
            newSizeDic[v] = size
            files +=1
        newSizeDic[key] = t
        break
    break
    
"""





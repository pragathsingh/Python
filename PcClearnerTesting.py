import os
import string
from ctypes import windll

LocDic = {}
SizeDic = {}
notAccessable =[]
drives = []

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
            return "%3.1f %s " % (num, x)
        num /= 1024.0
        


def MakeList(dirname):
    try:
        for x in os.listdir(dirname):
            l.append(dirname+"/"+x)
    except WindowsError:
        notAccessable.append(dirname)
    return l

for dr in drives:
    if(os.path.exists(dr)):
        for a in os.listdir(dr):
            try:
                print(a)
                     
                if os.path.isdir(dr+a):
                    #print a
                    l = []
                    for x in os.listdir(dr+a):
                        l.append(dr+a+"/"+x)
                    LocDic[dr+a] = l
            except WindowsError:
                notAccessable.append(dr+a)
        count = 0

for value in LocDic.values():
    for v in value:
        if(os.path.isdir(v)):
            if v in LocDic:
                ''
            else:
                count += 1
                LocDic[v] = MakeList(v)

print count
totalPcSize = 0
for value in LocDic:
    try:
        s = 0
        total = 0
        print '\n'
        for v in LocDic[value]:
            #print value,'\n'
            s = os.stat(v).st_size
            totalPcSize += s
            #SizeDic[v] = convert_bytes(s)
            SizeDic[v] = s
            #print v,'    ',convert_bytes(s)
            total +=s
        
        #print convert_bytes(total)
        break
    except WindowsError:
        notAccessable.append(value)

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


#for key in SizeDic:
#    if os.path.isdir(key):
#        print key,SizeDic[key]

print files
for a in notAccessable:
    print a
print 'Total Pc Size is : ',convert_bytes(totalPcSize)
#for v,w in newSizeDic.items():
    #print v,'  ',convert_bytes(w)

    #print key,size


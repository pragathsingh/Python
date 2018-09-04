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
print drives

for dr in drives:
    if(os.path.exists(dr)):
        for a in os.listdir(dr):
            print(a)
            try:        
                if os.path.isdir(dr+a):
                    #print a
                    l = []
                    for x in os.listdir(dr+a):
                        l.append(dr+a+"/"+x)
                    LocDic[dr+a] = l
            except WindowsError:
                    notAccessable.append(a)
        count = 0
oneTime = True
for value in LocDic.values():
    
    #print value,'\n'
    for v in value: 
        if(os.path.isdir(v)):            
            if v in LocDic:
                ''
            else:
                count += 1
                LocDic[v] = MakeList(v)                
        
totalPcSize = 0
print count

for key in LocDic:
    if 'E:/' in key:
        print key
for key in LocDic:
    try:
        size = 0
        total = 0        
        for v in LocDic[key]:
            size = os.stat(v).st_size          
            SizeDic[v] = size            
            total +=size
            totalPcSize += size        
        SizeDic[key] = total
        if 'GB' in convert_bytes(total):
            print key,'   ',convert_bytes(SizeDic[key])
        break
    except WindowsError:
        notAccessable.append(value)

print 'Total pc size ',convert_bytes(totalPcSize)
files = 0
newSizeDic = {}
tmptotal = 0
for key,value in LocDic.items():
    #print key
    for v in value:
        enter = os.path.isdir(v)
        enter != enter
        if enter:
            size = os.stat(v).st_size
            newSizeDic[key] = size
            tmptotal += size
    #print convert_bytes(tmptotal)
print 'new size of pc is : ',convert_bytes(tmptotal)

for a in drives:
    if os.path.exists(a):
        print a, '  ',convert_bytes(os.stat(dr).st_size)
"""
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
        if 'GB' in convert_bytes(t):
            print key,'  ',convert_bytes(t)
        break
    break    




"""
import os,time

stat = os.stat('C:/Important/exceptions.py')
size = stat.st_size
#print stat
#print(size)
count = 1
c = "c:/"
d = "d:/" 
e = "e:/"
f = "f:/"
g = "g:/"
h = "h:/"

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def loop(location):
    if os.path.isdir(location):
        try:
                stat = os.stat(c+a)                
                name = a
                if os.path.isdir(c+a+"/"):
                    isFolder = True
                    location = c+name+"/"
                else:
                    isFolder = False
                    location = c+name
                size = convert_bytes(stat.st_size)
                print count,name,'\t', size
                if(isFolder):
                    loop(location)
                else:
                    print name , convert_bytes(stat.st_size)                
                
        except WindowsError:
            'skip'    


for a in os.listdir(c):
    whilebool = True
    if(os.path.isdir(c+a)):
        parent = c+a
        isFolder = False
        while(whilebool):

            try:
                stat = os.stat(c+a)                
                name = a
                if os.path.isdir(c+a+"/"):
                    isFolder = True
                    location = c+name+"/"
                else:
                    isFolder = False
                    location = c+name
                size = convert_bytes(stat.st_size)
                print count,name,'\t', size
                if(isFolder):
                    loop(location)
                else:
                    print name , convert_bytes(stat.st_size)
                    break
            
                
            except WindowsError:
                'skip'    
    count+=1

time.sleep(5)
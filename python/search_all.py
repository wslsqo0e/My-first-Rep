"""
################################################################################
Use: "python ...\Tools\search_all.py dir string".
Search all files at and below a named directory for a string; uses the
os.walk interface, rather than doing a find.find to collect names first;
similar to calling visitfile for each find.find result for "*" pattern;
################################################################################
"""

import os,sys
listonly=False
textexts=['.py','.pyw','.txt','.c','.h','.el']

def searcher(startdir,searchkey):
    global fcount,vcount
    fcount=vcount=0
    for (thisDir,dirsHere,filesHere) in os.walk(startdir):
        for fname in filesHere:
            fpath=os.path.join(thisDir,fname)
            visitfile(fpath,searchkey)

def visitfile(fpath,searchkey):
    global fcount,vcount
    print(vcount+1,'=>',fpath,end=" ")
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textexts:
                print('Skipping',fpath)
            elif searchkey in open(fpath).read():
                print("***found!")
                input('%s has %s' % (fpath,searchkey))
                fcount+=1
            else:
                print("not found!")
    except:
        print('Failed:',fpath,sys.exc_info()[0])
    vcount+=1

if __name__=='__main__':
    if len(sys.argv)!=3:
        startDir=input("Please input the startDir you what to search (it can have nested Dir and use . for local Dir):\n")
        searchKey=input("Please input the string you what to search\n")
    else:
        startDir=sys.argv[1]
        searchKey=sys.argv[2]
    searcher(startDir,searchKey)
    print('Found in %d files,visited %d' % (fcount,vcount))


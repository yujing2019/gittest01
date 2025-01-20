"""

arrange files according to the file extent
"""
import sys
import os


def cleanup(dirpath):
    """
    1.create a dictionary for key = extent of the file,value is the name for the multiple files.
    1.os.mkdir : create multiple dir according to the different extent of file
    2.os.rename :move the files to the coincides dir
    :param dirpath:
    :return:
    """
    dirlist={}
    for f in os.listdir(dirpath):
        fdir,fext=os.path.splitext(f)
        fext=fext[1:]
        if fext not in dirlist.keys():
            dirlist[fext]=[]
        dirlist[fext].append(f)
    for k,v in dirlist.items():
        dirt="%s/%s"%(dirpath,k)
        os.mkdir(dirt)
        for var in v :
            old_path="%s/%s"% (dirpath,var)
            new_path="%s/%s"%(dirt,var)
            os.rename(old_path,new_path)


if __name__ =="__main__":
    if len(sys.argv) != 2:
        raise  Exception ("please give the cleanup dir path")
    dirpath =sys.argv[1]
    if not os.path.isdir(dirpath):
        raise Exception("%s is not a true dir"%dirpath)
    cleanup(dirpath)
    print("success")



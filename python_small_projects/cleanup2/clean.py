import sys
import os

d1={}
def clean(dirp):
    for fpath in os.listdir(dirp):
        file,fext=os.path.splitext(fpath)
        fext=fext[1:]
        if fext not in d1.keys():
            d1[fext]=[]
        d1[fext].append(fpath)
    for k,vs in d1.items():
        ext_dir= "%s/%s"%(dirp,k)
        if not os.path.exists(ext_dir):
            os.mkdir(ext_dir)
        for v in vs:
            old_path="%s/%s"%(dirp,v)
            new_path="%s/%s"%(ext_dir,v)
            os.rename(old_path,new_path)






if __name__ == "__main__":
    if len(sys.argv)!=2:
        raise Exception(" path null")
    if not os.path.isdir(sys.argv[1]):
        raise Exception("given path is abnormal ")
    dirpath=sys.argv[1]
    clean(dirpath)
    print("success done")


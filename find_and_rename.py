import os
from .parse_meta import find_esin
def find_and_rename():
    pwd = os.getcwd();

    dirs = os.listdir()

    for subdir in dirs:
        subdir = pwd+"/"+subdir;
        if os.path.isdir(subdir):
            os.chdir(subdir);
            subsubdirs = os.listdir();
            for subsubdir in subsubdirs:
                subsubdir = subdir+"/"+subsubdir;
                if os.path.isdir(subsubdir):
                    os.chdir(subsubdir);
                    if os.path.exist("cover.jpg") & os.path.exist("metadata.opf"):
                        print(find_esin('metadata.opf'));
                    
                    continue;
                continue;
            continue;
        continue;
    return ("File Processed Succcessfully")

    
#!/usr/bin/env python3
import os
import shutil
import glob
import getpass
from package.parse_meta import get_esin
def find_and_rename(directory):
    os.chdir(directory);
    user = getpass.getuser()
    files = os.listdir('/media/piedpipr/')
    print(files)
    
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
                    if os.path.exists("cover.jpg") & os.path.exists("metadata.opf"):
                        esin = get_esin("metadata.opf");
                        print(esin)
                        this_dir = os.getcwd();
                        oldname_cover = "cover.jpg"
                        oldname_book = "*.mobi"
                        dest_cover = "/media/piedpipr/Kindle/system/thumbnails/thumbnail_%s_EBOK_portrait.jpg" % esin
                        shutil.copy2(oldname_cover, dest_cover, follow_symlinks=True)

                        for file in glob.glob(r'*.mobi'):
                            dest_book = "/media/piedpipr/Kindle/documents/%s" % file
                            shutil.copy2(file, dest_book, follow_symlinks=True)

                    continue;
                continue;
            continue;
        continue;
    print("Done")
    

   

    
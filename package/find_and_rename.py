#!/usr/bin/env python3
import os
from package.parse_meta import get_esin
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
                    if os.path.exists("cover.jpg") & os.path.exists("metadata.opf"):
                        print (get_esin("metadata.opf"));
                        os.rename("*.mobi",kindle_book_dir) ## Kindle and Copy Functon Need To Be Added
                        os.rename("cover.jpg", kindle_thumb_dir)## Kindle and Copy Functon Need To Be Added
                    continue;
                continue;
            continue;
        continue;
    return ("File Processed Succcessfully")

    
#!/usr/bin/env python3
""" deobfuscate the contents of jars/objects which is mostly the music and sound effects (program by Giwby Albatross)
don't release the resulting files as it is a copyright issue according to https://github.com/WangTingZheng/mcp940/issues/2#issuecomment-2883062912 
I AM NOT RESPONSIBLE FOR COPYRIGHT PROBLEMS IF YOU RELEASE THE DEOBFUSCATED FILES """

import json
import time
import pathlib
import shutil

MC_VERSION = '1.12'

start_time = time.time()
assets_folder = pathlib.Path("jars", "assets")
objects_folder= pathlib.Path(assets_folder, "objects")
indexes_folder= pathlib.Path(assets_folder, "indexes")
result_folder = pathlib.Path("objects")
logfile = open(pathlib.Path("logs", "deobfuscate_assets.log"), 'w')

def log(*args, **kwargs):
    kwargs['file'] = logfile
    kwargs['flush']= True
    print(f"[{time.time()-start_time}]", *args, **kwargs)

def main(argv) -> int:
    log("Reading index file:", str(indexes_folder / (MC_VERSION+'.json')))
    mapping_file = open(indexes_folder / (MC_VERSION+'.json'))
    mappings = json.load(mapping_file)['objects']
    for file in mappings:
        file_id = mappings[file]['hash']
        hashdir = objects_folder / file_id[:2]
        fileloc = hashdir / file_id
        endpath = result_folder / file
        end_dir = endpath.parents[0]
        log("Putting file", file, "in", end_dir, "from hash:", file_id)
        end_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(fileloc, endpath)
    logfile.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

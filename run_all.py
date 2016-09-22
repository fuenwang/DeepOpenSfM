#!/usr/bin/env python

import Config
import subprocess
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Assign path'
        exit()
    subprocess.call('%s/bin/focal_from_exif %s'%(Config.OPENSFM_PATH, sys.argv[1]), shell=True)
    subprocess.call('python run_deepmatching.py %s'%sys.argv[1], shell=True)
    subprocess.call('python create_deep_track.py %s'%sys.argv[1], shell=True)
    subprocess.call('%s/bin/reconstruct %s'%(Config.OPENSFM_PATH, sys.argv[1]), shell=True)
    subprocess.call('%s/bin/mesh %s'%(Config.OPENSFM_PATH, sys.argv[1]), shell=True)

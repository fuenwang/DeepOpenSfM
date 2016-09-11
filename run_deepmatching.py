import Config
import sys
import subprocess
import os
import numpy as np

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'argv error'
        exit()

    data_path = sys.argv[1]
    image_path = '%s/images'%data_path
    match_path = '%s/matches'%data_path
    match_tmp_path = '%s/matches_deep'%data_path
    subprocess.call('mkdir -p %s && mkdir -p %s'%(match_path, match_tmp_path), shell=True)

    image_lst = sorted(os.listdir(image_path))
    total = len(image_lst)
    pairs = []
    for i, img in enumerate(image_lst):
        if i + 2 < total:
            pairs.append([img, image_lst[i+1]])
            pairs.append([img, image_lst[i+2]])
        elif i + 1 < total:
            pairs.append([img, image_lst[i+1]])
        else:
            continue
    #print pairs
    for pair in pairs:
        out_name = '%s/%s__MATCH__%s.txt'%(match_tmp_path, pair[0], pair[1])
        #print out_name
        #print pair
        print '%s ---------- %s'%(pair[0], pair[1])
        img_0 = '%s/%s'%(image_path, pair[0])
        img_1 = '%s/%s'%(image_path, pair[1])
        command = '%s %s %s -nt %d -out %s'%(Config.DEEPMATCH_PATH, img_0, img_1, Config.DEEPMATCH_THREAD, out_name)
        #print command
        #subprocess.call(command, shell=True)
    deep_file_lst = sorted(os.listdir(match_tmp_path))
    #print deep_file_lst
    for img in image_lst:
        matches = {}
        match_lst = [x for x in deep_file_lst if x.startswith(img)]
        for match_file in match_lst:
            match_img = match_file.split('__MATCH__')[1][:-4]
            match_tmp = []
            f = open('%s/%s'%(match_tmp_path, match_file), 'r') 
            for line in f:
                line = line.split(' ')
                A_row = int(line[1])
                A_col = int(line[0])
                B_row = int(line[3])
                B_col = int(line[2])
                A_feature_id = A_col * Config.IMAGE_HEIGHT + A_row + 1
                B_feature_id = B_col * Config.IMAGE_HEIGHT + B_row + 1
                match_tmp.append([A_feature_id, B_feature_id])
            f.close()
            matches[match_img] = np.array(match_tmp)
        print matches









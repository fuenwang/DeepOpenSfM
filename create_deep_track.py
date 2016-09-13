#!/usr/bin/env python
import Config
import sys
sys.path.append(Config.OPENSFM_PATH)

import numpy as np
from itertools import combinations
import argparse
import networkx as nx
from opensfm import dataset
from opensfm import matching
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


parser = argparse.ArgumentParser(description='Create tracks by grouping the robust matches')
parser.add_argument('dataset',
                    help='path to the dataset to be processed')
args = parser.parse_args()


data = dataset.DataSet(args.dataset)
images = sorted(data.images())

# Read local features
features = {}
colors = {}
info = Config.Info(args.dataset)
for im in images:
    '''
    p, f, c = data.load_features(im)
    features[im] = p[:,:2]
    colors[im] = c
    '''
    point_data = info.LoadPointData(im)
    features[im] = point_data['points']
    colors[im] = point_data['color']
    #print data
    #exit()

# Read matches
matches = {}
for im1 in images:
    try:
        im1_matches = data.load_matches(im1)
    except IOError:
        continue
    for im2 in im1_matches:
        matches[im1, im2] = im1_matches[im2]


tracks_graph = matching.create_tracks_graph(features, colors, matches, data.config)
data.save_tracks_graph(tracks_graph)

import gzip
import pickle



f = gzip.open('image-00034.jpg_matches.pkl.gz', 'rb')
matches = pickle.load(f)


print matches

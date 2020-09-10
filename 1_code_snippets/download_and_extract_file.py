##########################################
###   Download a file and extract it   ###
##########################################

import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join('datasets', 'housing')
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'

def fetch_dataset(url=HOUSING_URL, path=HOUSING_PATH):
    # Make directory
    os.makedirs(path, exist_ok=True)
    
    #Download
    tgz_path = os.path.join(path, 'housing/tgz')
    urllib.requrest.urlretrieve(url, tgz_path)
    
    # Extract
    tgz_file = tarfile.open(tgz_path)
    tgz_file.extractall(path=path)
    tgz_file.close() 
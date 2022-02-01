#!/usr/bin/env python
# coding: utf-8

"""
Usage:
    extract_descriptors.py [options]

The extract descriptor file extract PLEC and GRID features for interaction
between the protein and the ligand. The following argument is the type of
interaction features and the path for the csv file to be saved. For example, 
if you want to extract the plec features you can use the following commands.

python data/extract_descriptors.py --type PLEC --csv_path data/features/PLEC_features.csv 

On the other hand, if you want to extract the grid features, you can use the following commands.

python data/extract_descriptors.py --type GRID --csv_path data/features/GRID_features.csv

Options:
    -h --help                Show this screen.
    --type type              Feature Type (i.e. PLEC or GRID)
    --csv_path path          csv file to be saved as a csv file after feature calculation   
    
"""


import oddt.pandas as opd
import os
import numpy as np
import deepchem as dc
from deepchem.feat import RdkitGridFeaturizer
from oddt.fingerprints import PLEC
import oddt
import glob
from joblib import Parallel, delayed
from tqdm import tqdm
import multiprocessing
import warnings
import pandas as pd
from docopt import docopt
import sys



featurizer = RdkitGridFeaturizer(voxel_width=16.0, feature_types=["ecfp", "splif", "hbond", "salt_bridge"], ecfp_power=9,splif_power=9,flatten=True)
protein = "data/protein/6NM8-receptor.pdb"


def extract_grid_feature(ligand_file):
    feature = featurizer._featurize((ligand_file, protein))
    return feature

def extract_plec_feature(ligand_file):
    receptor = next(oddt.toolkit.readfile("pdb", protein))
    receptor.protein = True
    mol = next(oddt.toolkit.readfile('sdf', ligand_file))
    feature = PLEC(mol, receptor, size = 4092, depth_protein = 4, depth_ligand = 2, distance_cutoff = 4.5, sparse = False)
    return feature

def extract_all_sdf_files(type= "PLEC"):
    sdf_files = glob.glob("data/compounds/docked/*.sdf")
    if (type == "GRID"):
        feature = Parallel(n_jobs = multiprocessing.cpu_count(), backend = "multiprocessing")(delayed(extract_grid_feature)(sdf_file) for sdf_file in tqdm(sdf_files))
    else:
        feature = Parallel(n_jobs = multiprocessing.cpu_count(), backend = "multiprocessing")(delayed(extract_plec_feature)(sdf_file) for sdf_file in tqdm(sdf_files))
    return pd.DataFrame(feature)


if __name__ == "__main__":
    ## parse args
    args = docopt(__doc__)
    if args.get('--type'):
        type = args.get('--type')
    else:
        print("Please specify feature type")
        exit()

    if args.get('--csv_path'):
        csv_path = args.get('--csv_path')
    else:
        csv_path = ''
        
    extract_all_sdf_files(type = type).to_csv(csv_path, index = False)





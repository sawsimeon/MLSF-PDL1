import oddt.pandas as opd
import os
import numpy as np
import deepchem as dc
from deepchem.feat import RdkitGridFeaturizer
from oddt.fingerprints import PLEC
import oddt
import glob
from joblib import Parallel, delaye, delayed
from tqdm import tqdm
import multiprocessing

featurizer = RdkitGridFeaturizer(voxel_width=16.0, feature_types=["ecfp", "splif", "hbond", "salt_bridge"], ecfp_power=9,splif_power=9,flatten=True)
protein = "data/protein/6NM8-receptor.pdb"
ligand_file = "data/compounds/2__1000.sdf"


def extract_grid_feature(ligand_file):
    feature = featurizer._featurize((ligand_file, protein))
    return feature

def extract_plec_feature(ligand_file):
    receptor = next(oddt.toolkit.readfile("pdb", protein))
    receptor.protein = True
    mol = next(oddt.toolkit.readfile('sdf', ligand_file))
    feature = PLEC(mol, receptor, size = 4092, depth_protein = 4, depth_ligand = 2, distance_cutoff = 4.5, sparse = False)
    return feature

def extract_all_sdf_files(sdf_files_path, type):
    
    sdf_files = glob.glob("data/compounds/*.sdf")
    if (type == "GRID"):
        feature = Parallel(n_jobs = multiprocessing.cpu_count(), backend = "multiprocessing")(delayed(extract_grid_feature)(sdf_file) for sdf_file in tqdm(sdf_files))
    else:
        feature = Parallel(n_jobs = multiprocessing.cpu_count(), backend = "multiprocessing")(delayed(extract_plec_feature)(sdf_file) for sdf_file in tqdm(sdf_files))
    return feature




import oddt.pandas as opd
import os
import numpy as np
import tempfile
import deepchem as dc
from deepchem.utils.vina_utils import prepare_inputs
from deepchem.feat import RdkitGridFeaturizer
from oddt.pandas import ChemDataFrame
from oddt.fingerprints import PLEC
import oddt

featurizer = RdkitGridFeaturizer(voxel_width=16.0, feature_types=["ecfp", "splif", "hbond", "salt_bridge"], ecfp_power=9,splif_power=9,flatten=True)
#protein = "data/protein/6NM8-receptor.pdb"
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


grid_feature = extract_grid_feature(ligand_file)
plec_feature = extract_plec_feature(ligand_file)


import oddt.pandas as opd
import os
import numpy as np
import tempfile
import deepchem as dc
from deepchem.utils.vina_utils import prepare_inputs
from deepchem.feat import RdkitGridFeaturizer

featurizer = RdkitGridFeaturizer(voxel_width=16.0, feature_types=["ecfp", "splif", "hbond", "salt_bridge"], ecfp_power=9,splif_power=9,flatten=True)
protein = "protein/6nm8-receptor-preprocessed.pdb"
ligand_file = ""
def extract_grid_feature(ligand_file):
    feature = featurizer._featurize((ligand_file, protein))
    return feature

#extract_grid_feature(ligand_file = "compounds/2--1000.sdf")

feature = featurizer._featurize((ligand_file, protein))
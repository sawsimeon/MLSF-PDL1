import os
import glob
import subprocess
from tqdm import tqdm
from joblib import Parallel, delayed
import multiprocessing


def run_smina(sdf_file):
    sdf_file_name = sdf_file.split('/')[3][:-4]
    receptor_path = 'data/protein/6NM8-receptor.pdb'
    auto_box_path = 'data/protein/6NM8-KSD.pdb'
    output_path = 'data/compounds/docked/' + str(sdf_file_name) + '_docked.sdf'
    input_path = sdf_file
    smina_command = [' smina -r ' + str(receptor_path) + ' --autobox_ligand ' + str(auto_box_path) + 
                ' -l ' + str(input_path) + ' -o ' + output_path  + 
                ' --num_modes 1 --seed 0 --cpu 1 --size_x 30 --size_y 30 --size_z 30 --exhaustiveness 1 ']
    os.system(smina_command[0]) 


sdf_files = glob.glob("data/compounds/raw/*.sdf")

Parallel(n_jobs = multiprocessing.cpu_count(), backend = "multiprocessing")(delayed(run_smina)(sdf_file) for sdf_file in tqdm(sdf_files))
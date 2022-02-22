# Data 

We have prepared different datasets based on different several sources (ZINC, DeepCoy Generator and PubChem).
These datasets match the dataset utilised in our paper, Structure-based virtual screening for PDL1 dimerizers is boosted by inactive-enriched machine-learning models exploiting patent data.

We have also provided several scripts to allow you to utilize your own dataset. 

# To use a provided dataset

To process the provided datasets, run `extract_descriptors.py`. This allows you to extract [PLEC](https://academic.oup.com/bioinformatics/article/35/8/1334/5092926) and [GRID](https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc02664a) which were utilized to build predictive model. The protein structure is provided, which is 6NM8 (PDB ID). This script will only generate descriptors for the PDL1-specific interaction features.

```
python extract_descriptors.py
```

# To use your own dataset

Firstly, you may need to docked pose of your molecules. To dock your molecules using the SMINA, an autodock vina software, you may provide moleculs in the sdf format as an input file. Run `smina_docking.py` to obtained docked posses that will be docked into the compounds folder. The format taken by `smina_docking.py` is 


```
a single sdf file for each molecule
```

For example:

```
24 25  0  0  0  0  0  0  0  0999 V2000
   -1.8183   34.1410   16.5531 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.9505   35.4438   16.3698 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.4811   34.9821   15.9039 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.5591   36.0966   15.9096 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.6668   36.7827   17.2977 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.3099   37.3537   17.8628 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7914   36.1981   17.7684 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.1337   36.6343   18.4539 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.9305   37.2236   19.8751 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8684   38.2304   19.8942 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1144   39.4840   20.3199 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.4631   37.8307   19.3881 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.0581   38.6488   17.0271 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.6532   36.2847   15.2399 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.0361   35.9681   15.0830 O   0  0  0  0  0  0  0  0  0  0  0  0
   -3.1274   35.0378   14.8239 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.1880   36.8448   20.3774 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.8105   36.9536   21.8879 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9894   37.4200   22.8117 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9340   36.7108   24.1958 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8199   38.8129   23.1106 O   0  0  0  0  0  0  0  0  0  0  0  0
    0.9521   38.9522   23.5212 H   0  0  0  0  0  0  0  0  0  0  0  0
    3.2849   37.1216   22.1843 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.3695   36.6515   22.8134 C   0  0  0  0  0  0  0  0  0  0  0  0
  2  1  1  0  0  0
  2  3  1  0  0  0
  2  7  1  0  0  0
  2 14  1  0  0  0
  3  4  1  0  0  0
  4  5  1  0  0  0
  5  6  1  0  0  0
  6  7  1  0  0  0
  6 12  1  0  0  0
  6 13  1  0  0  0
  7  8  1  0  0  0
  8  9  1  0  0  0
  9 10  1  0  0  0
 10 11  2  0  0  0
 10 12  1  0  0  0
 12 17  1  0  0  0
 17 18  1  0  0  0
 18 19  1  0  0  0
 19 20  1  0  0  0
 19 23  1  0  0  0
 19 21  1  0  0  0
 23 24  2  0  0  0
 14 15  1  0  0  0
 21 22  1  0  0  0
 15 16  1  0  0  0
M  END
```
Once you have the docked molecules, you can enrich them to the compounds folder. Thus, the compounds folder will only contain the docked poses. It is important to note that one molecule will need only one docked pose. You may select your docked pose by using PyMol or MOE software. Or you can select the dock pose based on the top score of SMINA (minimizedAffinity).  

# Molecule docking

If you want to prepare your own dataset, run `smina_docking.py` with the following syntax:

```
python smina_docking.py
```

# Featurization

If you want to extract the interaction features, whether PLEC or GRID and save it as a csv file, run `extract_descriptors.py` with the following arguments:

```
# for PLEC features
python extract_descriptors.py --type PLEC --csv_path PLEC_features.csv
# for GRID features
python extract_descriptors.py --type GRID --csv_path GRID_features.csv
```

If you want to know what arguments is needed. you can run `extract_descriptors.py` with the following argument:

```
python extract_descriptors.py --help
```

The format taken by the extract_descriptors is:

```
single docked pose as sdf file
```

There should be no other entries on a line other than the sdf file of the molecule to generate features for.

# Calculated features

We provide calculated features for training and test set files from the Table 1 of the Manuscript. Each file will have as many rows as docked molecules + header. Then there will be the following columns: pIC50, molecule-ID and features (the latter with as many columns as features). Due to GitHub file size constraints, these 24 files (training and  test) X 6 partitions X 2 featurization can be downloded from the [zenodo](https://doi.org/10.5281/zenodo.6226320). 


# Data 

We have prepared different datasets based on different several sources (ZINC, DeepCoy Generator and PubChem).
These datasets match the dataset utilised in our paper, Structure-based virtual screening for PD-L1 dimerizers is boosted by inactive-enriched machine-learning models exploiting patent data.

We have also provided several scripts to allow you to use your own dataset.

# To use a provided dataset

To process the provided datasets, run `extract_descriptors.py`. This allows you to extract PLEC and GRID which were utilized to build predictive model.

```
python extract_descriptors.py
```

# To use your own dataset



The format taken by `extract_descriptors.py` is: 

```
single docked pose as sdf file
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
> <minimizedAffinity>
-6.39995

$$$$
```

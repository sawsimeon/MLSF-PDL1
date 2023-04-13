#!/usr/bin/env python
# coding: utf-8

# ### Load required packages

# In[1]:


import numpy as np
import pandas as pd
import zipfile, pickle
from sklearn.metrics import precision_recall_curve, auc
from convert_pIC50_to_activity import bin_predicted_pIC50, bin_observed_pIC50


# In[2]:


from math import ceil
def enrichment_factor(y_true, y_score, percentage=1, pos_label=None, kind='fold'):
    """Computes enrichment factor for given percentage, i.e. EF_1% is
    enrichment factor for first percent of given samples. This function assumes
    that results are already sorted and samples with best predictions are first.

    Parameters
    ----------
    y_true : array, shape=[n_samples]
        True binary labels, in range {0,1} or {-1,1}. If positive label is
        different than 1, it must be explicitly defined.

    y_score : array, shape=[n_samples]
        Scores for tested series of samples

    percentage : int or float
        The percentage for which EF is being calculated

    pos_label: int
        Positive label of samples (if other than 1)

    kind: 'fold' or 'percentage' (default='fold')
        Two kinds of enrichment factor: fold and percentage.
        Fold shows the increase over random distribution (1 is random, the
        higher EF the better enrichment). Percentage returns the fraction of
        positive labels within the top x% of dataset.

    Returns
    -------
    ef : float
        Enrichment Factor for given percenage in range 0:1
    """
    if pos_label is None:
        pos_label = 1
    labels = y_true == pos_label
    assert labels.sum() > 0, "There are no correct predicions. Double-check the pos_label"
    assert len(labels) > 0, "Sample size must be greater than 0"
    # calculate fraction of positve labels
    n_perc = int(ceil(percentage / 100. * len(labels)))
    out = labels[:n_perc].sum() / n_perc
    if kind == 'fold':
        out /= (labels.sum() / len(labels))
    return out


# In[3]:


def bin_predicted_pIC50(row):
    if row['Predicted_pIC50'] >= 5:
        val = 'Active'
    else:
        val = "Inactive"
    return val

def bin_observed_pIC50(row):
    if row['Observed_pIC50'] >= 5:
        val = 'Active'
    else:
        val = 'Inactive'
    return val


# ### SVM GRID SF Model (Training actives + TrueInactives)

# In[4]:


filename = "../models/GRID_SVM_SFs_training_actives_and_TrueInactives.sav"
GRID_SVM_SF = pickle.load(open(filename, 'rb'))


# ### Load GRID Features

# In[5]:


test_rdkit_grid_features_deepcoys = np.load("../data/test_set/RDKit_Grid_Feature_Test_DeepCoy.zip")
test_rdkit_grid_features_deepcoys = pd.DataFrame(test_rdkit_grid_features_deepcoys['RDKit_Grid_Feature_Test_DeepCoy'])

DeepCoys_Labels = pd.read_csv("../data/test_set/DeepCoy_IDs.csv")


# ### Predict on Test Set

# In[6]:


prediction_test_rdkit_grid_svm = GRID_SVM_SF.predict(test_rdkit_grid_features_deepcoys)


# ### Get AUC-PR 

# In[7]:


svm_rdkit_grid_result = pd.DataFrame({"Predicted_pIC50": prediction_test_rdkit_grid_svm,
                                     "Observed_pIC50": list(DeepCoys_Labels['pIC50'])})
svm_rdkit_grid_result['Predicted_Activity'] = svm_rdkit_grid_result.apply(bin_predicted_pIC50, axis = 1)
svm_rdkit_grid_result['Observed_Activity'] = svm_rdkit_grid_result.apply(bin_observed_pIC50,axis = 1)
svm_rdkit_grid_result['normalized_scores'] = (svm_rdkit_grid_result['Predicted_pIC50'] - svm_rdkit_grid_result['Predicted_pIC50'].min()) / (svm_rdkit_grid_result['Predicted_pIC50'].max() - svm_rdkit_grid_result['Predicted_pIC50'].min())
precision_rdkit_grid_svm, recall_rdkit_grid_svm, threshold_rdkit_grid_svm = precision_recall_curve(svm_rdkit_grid_result['Observed_Activity'], svm_rdkit_grid_result['normalized_scores'], pos_label = 'Active')
svm_rdkit_grid_precision_recall = pd.DataFrame({"Precision": precision_rdkit_grid_svm,
                                               "Recall": recall_rdkit_grid_svm})
print(auc(recall_rdkit_grid_svm, precision_rdkit_grid_svm))


# ### Get EF1% 

# In[8]:


data_active_score = pd.DataFrame(svm_rdkit_grid_result['Predicted_pIC50'])
data_active_score['activity'] = svm_rdkit_grid_result['Observed_Activity']
data_active_score.sort_values('Predicted_pIC50', inplace=True, ascending=False)
enrichment_value= round(enrichment_factor(data_active_score['activity'], data_active_score['Predicted_pIC50'], percentage=1, pos_label='Active'))
enrichment_value


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ### Load required packages

# In[7]:


import numpy as np
import pandas as pd
import zipfile, pickle
from sklearn.metrics import precision_recall_curve, auc


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

# In[2]:


filename = "../models/GRID_SVM_SFs_training_actives_and_TrueInactives.sav"
GRID_SVM_SF = pickle.load(open(filename, 'rb'))


# ### Load GRID Features

# In[6]:


test_rdkit_grid_features_deepcoys = np.load("../data/test_set/RDKit_Grid_Feature_Test_DeepCoy.zip")
test_rdkit_grid_features_deepcoys = pd.DataFrame(test_rdkit_grid_features_deepcoys['RDKit_Grid_Feature_Test_DeepCoy'])

DeepCoys_Labels = pd.read_csv("../data/test_set/DeepCoy_IDs.csv")


# ### Predict on Test Set

# In[4]:


prediction_test_rdkit_grid_svm = GRID_SVM_SF.predict(test_rdkit_grid_features_deepcoys)


# ### Get AUC-PR 

# In[8]:


svm_rdkit_grid_result = pd.DataFrame({"Predicted_pIC50": prediction_test_rdkit_grid_svm,
                                     "Observed_pIC50": list(DeepCoys_Labels['pIC50'])})
svm_rdkit_grid_result['Predicted_Activity'] = svm_rdkit_grid_result.apply(bin_predicted_pIC50, axis = 1)
svm_rdkit_grid_result['Observed_Activity'] = svm_rdkit_grid_result.apply(bin_observed_pIC50,axis = 1)
svm_rdkit_grid_result['normalized_scores'] = (svm_rdkit_grid_result['Predicted_pIC50'] - svm_rdkit_grid_result['Predicted_pIC50'].min()) / (svm_rdkit_grid_result['Predicted_pIC50'].max() - svm_rdkit_grid_result['Predicted_pIC50'].min())
precision_rdkit_grid_svm, recall_rdkit_grid_svm, threshold_rdkit_grid_svm = precision_recall_curve(svm_rdkit_grid_result['Observed_Activity'], svm_rdkit_grid_result['normalized_scores'], pos_label = 'Active')
svm_rdkit_grid_precision_recall = pd.DataFrame({"Precision": precision_rdkit_grid_svm,
                                               "Recall": recall_rdkit_grid_svm})
print(auc(recall_rdkit_grid_svm, precision_rdkit_grid_svm))


# In[ ]:





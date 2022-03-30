#!/usr/bin/env python
# coding: utf-8

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


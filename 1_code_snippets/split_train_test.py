##############################################
###   Split the data into train and test   ###
##############################################

import numpy as np

def split_train_test(data, test_ratio):
    """
    Function to perform train and test split
    param: data - the original dataset
    param: test_ratio - the ratio of data to keep as test
    returns: train data and test data
    """
    # Shuffle the data
    shuffled_indices = np.random.permutation(len(data))
    
    # Size of test set
    test_set_size = int(len(data) * test_ratio)
    
    # Defining the indices
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    
    return data.iloc[train_indices], data.iloc[test_indices]
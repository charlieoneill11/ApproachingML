# stratified kfold for regression

import numpy as np 
import pandas as pd 
from sklearn import datasets
from sklearn import model_selection

def create_folds(data):
    # we create a new column called kfold and fill it with -1
    data['kfold'] = -1

    # randomise the rows of the data
    data = data.sample(frac=1).reset_index(drop=True)

    # calculate number of bins by Sturge's rule
    num_bins = int(np.floor(1 + np.log2(len(data))))

    # bin targets
    data.loc[:, 'bins'] = pd.cut(data['target'], bins = num_bins, labels=False)

    # initiate the kfold class from model_selection module
    kf = model_selection.StratifiedKFold(n_splits=5)

    # fill the new kfold column
    # note that instead of targets we use bins
    for f, (t_, v_) in enumerate(kf.split(X=data, y=data.bins.values)):
        data.loc[v_, 'kfold'] = f 

    # drop the bins column
    data = data.drop("bins", axis=1)
    return data

if __name__ == "__main__":
    # create a sample dataset with 15000 samples
    # 100 features and 1 target
    X, y = datasets.make_regression(n_samples=15000, n_features=100, n_targets=1)

    # create a dataframe out of our numpy arrays
    df = pd.DataFrame(X, columns=[f"f_{i}" for i in range(X.shape[1])])
    df.loc[:, 'target'] = y 
    
    # create folds 
    df = create_folds(df)
    print(np.mean(df['target']))
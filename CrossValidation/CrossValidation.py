import pandas as pd
from sklearn import model_selection

if __name__ == "__main__":

    # get the training data
    df = pd.read_csv('train.csv')

    # create a column called kfold and fill it with -1
    df['kfold'] = -1
    df = df.sample(frac=1).reset_index(drop=True)
    kf = model_selection.KFold(n_splits=5)
    
    # fill the new kfold column
    for fold, (trn_, val_) in enumerate(kf.split(X=df)):
        df.loc[val_, 'kfold'] = fold

    # save the new csv with kfold column
    df.to_csv("train_folds.csv", index=False)
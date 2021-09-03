from Precision import *
from Recall import *
from sklearn import metrics

def f1(y_true, y_pred):
    """
    Function to calculate f1 score
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: f1 score
    """
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * p * r / (p+r)

if __name__ == "__main__":
    y_true = [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]
    y_pred = [0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0]
    print("Using our custom F1 score, we obtain {}".format(f1(y_true, y_pred)))
    print("Using sklearn, we obtain {}".format(metrics.f1_score(y_true, y_pred)))
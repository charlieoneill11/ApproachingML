from TrueFalsePositiveNegative import *

def recall(y_true, y_pred):
    """
    Function to calculate recall
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: recall score
    """
    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    return tp / (tp + fn)

if __name__ == "__main__":
    l1 = [0,1,1,1,0,0,0,1]
    l2 = [0,1,0,1,0,1,0,0]
    print(recall(l1, l2))
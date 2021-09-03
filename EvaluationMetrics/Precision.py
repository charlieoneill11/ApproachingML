from TrueFalsePositiveNegative import true_positive 
from TrueFalsePositiveNegative import false_positive

def precision(y_true, y_pred):
    """
    Function to calculate precision
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: precision score
    """
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    return tp / (tp + fp)

if __name__ == "__main__":
    l1 = [0,1,1,1,0,0,0,1]
    l2 = [0,1,0,1,0,1,0,0]
    print(precision(l1, l2))
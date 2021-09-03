def true_positive(y_true, y_pred):
    """
    Function to calculate true positives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of true positives
    """
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1
    return tp 

def true_negative(y_true, y_pred):
    """
    Function to calculate true negatives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of true negatives
    """
    tn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 0:
            tn += 1
    return tn 

def false_positive(y_true, y_pred):
    """
    Function to calculate false positives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of false positives
    """
    fp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 1:
            fp += 1
    return fp 

def false_negative(y_true, y_pred):
    """
    Function to calculate false negatives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of false negatives
    """
    fn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 0:
            fn += 1
    return fn

def accuracy_v2(y_true, y_pred):
    """
    Function to calculate accuracy using tp/tn/fp/fn
    :param y_true: list of true values
    :param y_pred: list of predicted values
    : return: accuracy score
    """
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    return (tp + tn) / (tp + tn + fp + fn)

if __name__ == "__main__":
    l1 = [0,1,1,1,0,0,0,1]
    l2 = [0,1,0,1,0,1,0,0]
    print(true_positive(l1, l2))
    print(false_positive(l1, l2))
    print(true_negative(l1, l2))
    print(false_negative(l1, l2))
    print(accuracy_v2(l1, l2))
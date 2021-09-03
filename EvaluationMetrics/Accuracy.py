def accuracy(y_true, y_pred):
    """
    Function to calculate accuracy.
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: accuracy score
    """
    # initialise a counter for correct predictions
    correct_counter = 0
    # loop over all elements of y_true and y_pred
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            # if prediction is equal to truth, increase the counter
            correct_counter += 1
    # return accuracy
    return correct_counter / len(y_true)

if __name__ == "__main__":
    y_pred = [1,2,3,4,5,6]
    y_true = [1,3,3,5,6,7]
    print(accuracy(y_true, y_pred))
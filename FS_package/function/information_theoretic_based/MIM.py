import LCSI


def mim(X, y, **kwargs):
    """
    This function implements the mim function
    Input
    ----------
    X: {numpy array}, shape (n_samples, n_features)
        Input data, guaranteed to be a discrete numpy array
    y : {numpy array},shape (n_samples, )
        guaranteed to be a numpy array
    kwargs: {dictionary}
        n_selected_features: {int}
            indicates the number of features to select
    Output
    ----------
    F: {numpy array},shape (n_features, )
        Index of selected features, F(1) is the most important feature.
    """
    if 'n_selected_features' in kwargs.keys():
        n_selected_features = kwargs['n_selected_features']
        F = LCSI.lcsi(X, y, beta=0, gamma=0, n_selected_features=n_selected_features)
    else:
        F = LCSI.lcsi(X, y, beta=0, gamma=0)
    return F

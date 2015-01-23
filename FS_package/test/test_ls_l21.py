import scipy.io
from sklearn import svm
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from FS_package.utility.sparse_learning import *
from FS_package.function.sparse_learning_based import ls_l21


def main():
    # load MATLAB data
    mat = scipy.io.loadmat('../data/ORL.mat')
    X = mat['fea']    # data
    y = mat['gnd']    # label
    y = y[:, 0]
    n_sample, n_feature = X.shape
    X = X.astype(float)
    Y = construct_label_matrix(y)

    # 5-fold cross validation
    num_fea = 20
    ss = cross_validation.ShuffleSplit(n_sample, n_iter=5, test_size=0.2)
    clf = svm.LinearSVC()
    mean_acc = 0

    for train, test in ss:
        W, obj = ls_l21.ls_l21_gradient_descent(X[train], Y[train], 0.1, verbose=False)
        idx = feature_ranking(W)
        selected_features = X[:, idx[0:num_fea]]
        clf.fit(selected_features[train], y[train])
        y_predict = clf.predict(selected_features[test])
        acc = accuracy_score(y[test], y_predict)
        print acc
        mean_acc = mean_acc + acc
    mean_acc /= 5
    print 'mean_acc', mean_acc


if __name__ == '__main__':
    main()
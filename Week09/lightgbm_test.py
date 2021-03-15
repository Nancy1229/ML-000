# coding: utf-8
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import train_test_split
import lightgbm as lgb

def getLabel(x):
    threshold = 0.5
    z = np.where(x>=threshold,1,0)
    return z

def train_gbdt(df_train,df_test):
    y = df_train["loan_status"]
    X = df_train.drop("loan_status", axis=1)

    y_test_pred = df_test["loan_status"]
    X_test_pred = df_test.drop("loan_status", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=2)
    # create dataset for lightgbm
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    # specify your configurations as a dict
    params = {
        'boosting_type': 'gbdt',
        'objective': 'regression',
        'metric': {'l2', 'l1'},
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9,
        'bagging_fraction': 0.8,
        'bagging_freq': 5,
        'verbose': 0
    }

    print('Starting training...')
    # train
    gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=20,
                    valid_sets=lgb_eval,
                    early_stopping_rounds=5)

    print('Saving model...')
    # save model to file
    gbm.save_model('model.txt')

    print('Starting validate...')
    # validate
    y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
    # eval
    print('The rmse of validate is:', mean_squared_error(y_test, y_pred) ** 0.5)
    y_pred_label = getLabel(y_pred)
    print('精确度：',(y_pred_label == y_test).sum() / y_test.size)  # 精准度

    print('Starting predicting...')
    # predict
    y_pred_pred = gbm.predict(X_test_pred, num_iteration=gbm.best_iteration)
    # eval
    print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)
    y_pred_pred_label = getLabel(y_pred_pred)
    print('精确度：',(y_pred_pred_label == y_test_pred).sum() / y_test_pred.size)  # 精准度  


if __name__ == "__main__":
    print('Loading data...')
    # load or create your dataset
    df_train = pd.read_csv('train_final.csv', sep=',')
    df_test = pd.read_csv('test_final.csv', sep=',')
    print("###############")
    print("原始特征")
    train_gbdt(df_train,df_test)


    combine = [df_train,df_test]
    for dataset in combine:
        dataset["monthly"] = dataset["continuous_annual_inc"]/12
    #    dataset["totol_monthly_dabt"] = dataset["continuous_dti"] * dataset["monthly"] * dataset["continuous_loan_amnt"] \
    #        +dataset["continuous_installment"]
    print("###############")
    print("添加一个衍生变量")
    train_gbdt(df_train,df_test)


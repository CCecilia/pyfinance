from collections import Counter
import pandas as pd
import pickle
import numpy as np
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier


def process_data_for_labels(ticker):
    # how many days
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()

    df.fillna(0, inplace=True)
    '''
    day 2 in the future value in percent change
    ((2day future price - todays price) / todays price) * 100
    .shift(-i) = shifting up to the future on the df
    '''
    for i in range(1, hm_days + 1):
    	# create new df column, 7 day percent changes in future
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)

    return tickers, df


def buy_sell_hold(*args):
	cols = [c for c in args]
	# trigger of 2%
	requirement = 0.02

	# crosscheck each against the trigger
	for col in cols:
		# buy
		if col > 0.025:
			return 1
		# sell (stop loss)
		if col < -0.025:
			return -1
	# hold
	return 0

def extract_freature_sets(ticker):
	tickers, df = process_data_for_labels(ticker)

	df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
			df['{}_1d'.format(ticker)],
			df['{}_2d'.format(ticker)],
			df['{}_3d'.format(ticker)],
			df['{}_4d'.format(ticker)],
			df['{}_5d'.format(ticker)],
			df['{}_6d'.format(ticker)],
			df['{}_7d'.format(ticker)],
		))

	vals = df['{}_target'.format(ticker)].values.tolist()
	str_vals = [str(i) for i in vals]

	print('Data Spread:', Counter(str_vals))

	df.fillna(0, inplace=True)
	df = df.replace([np.inf, -np.inf], np.nan)
	# df.dopna(inplace=True)

	df_vals = df[[ticker for ticker in tickers]].pct_change()
	df_vals = df.replace([np.inf, -np.inf], 0)
	df_vals.fillna(0, inplace=True)

	# X = labels, y = featuresets
	X = df_vals.values
	y = df['{}_target'.format(ticker)].values

	return X, y, df


def do_ml(ticker):
	X, y, df = extract_freature_sets(ticker)

	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)

	# clf = neighbors.KNeighborsClassifier()
	clf = VotingClassifier([
		('lsvc', svm.LinearSVC()),
		('knm', neighbors.KNeighborsClassifier()),
		('rfor', RandomForestClassifier())
		])

	clf.fit(X_train, y_train)


	confidence = clf.score(X_test, y_test)
	predictions = clf.predict(X_test)
	print('Accuracy:', confidence)
	print('Predicted Spread:', Counter(predictions))

do_ml('BAC')


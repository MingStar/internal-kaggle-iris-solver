#idea from: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0

import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

DEBUG=True

def debug(*args):
  if DEBUG:
    print(*args)

def test(input_reader):
  features = np.array([row for row in input_reader])
  rf, real_labels = train('data/features.csv', 'data/training_labels.csv')
  debug(real_labels)
  return [get_label(prediction, real_labels) for prediction in rf.predict(features)]

def get_label(prediction, real_labels):
  return real_labels[np.argmax(prediction)].split('_', 1)[1]

def train(features_file, label_file):
  features, labels = read_data(features_file, label_file)
  real_labels = labels.columns
  features, labels = prepare_data(features, labels)
  #train_features, test_features, train_labels, test_labels = \
  #  train_test_split(features, labels, test_size = 0.25, random_state = 42)
  rf = RandomForestRegressor(n_estimators=1000, random_state=42)
  rf.fit(features, labels)
  predictions = rf.predict(features)
  errors = abs(predictions - labels)
  debug('Mean Absolute Error:', round(np.mean(errors), 2))
  return rf, real_labels

def prepare_data(features, labels):
  return np.array(features), np.array(labels)

def read_data(features_file, label_file):
  features = pd.read_csv(features_file, header=None)
  debug(features.head(5))
  labels = pd.read_csv(label_file, header=None)
  labels.rename(columns={0:'label'}, inplace=True)
  labels = pd.get_dummies(labels)
  debug(labels.head(5))
  return features, labels

if __name__=='__main__':
  train('data/features.csv', 'data/training_labels.csv')

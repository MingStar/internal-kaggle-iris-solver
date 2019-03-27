import sys
import csv
import random

ANSWERS = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

def test_iris(input_file, output_file):
  with open(input_file) as csvfile, open(output_file, 'w') as writefile:
    reader = csv.reader(csvfile)
    writer = csv.writer(writefile)
    for _ in reader:
      answer = random.choice(ANSWERS) # RANDOM!!!
      writer.writerow([answer])
      print(answer)

if __name__=="__main__":
  competition = sys.argv[1]
  input_path = sys.argv[2]
  output_path = sys.argv[3]
  test_iris(input_path + '/features.csv', output_path + '/output.csv')

import sys
import csv
import random
import random_forest_solver

def random_output(input_reader):
  ANSWERS = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
  return [random.choice(ANSWERS) for _ in input_reader]

def random_forest(input_reader):
  return random_forest_solver.test(input_reader)

def run(input_path, output_path):
  input_file = input_path + '/features.csv'
  output_file = output_path + '/output.csv'
  #method = random_output
  method = random_forest
  with open(input_file) as csvfile, open(output_file, 'w') as writefile:
    reader = csv.reader(csvfile)
    writer = csv.writer(writefile)
    for prediction in method(reader):
      print(prediction)
      writer.writerow([prediction])

if __name__=="__main__":
  competition = sys.argv[1]
  input_path = sys.argv[2]
  output_path = sys.argv[3]
  run(input_path, output_path)

import os
import csv

response_dirs = ['./round1/', './round2/', './round3/', './round4/']

methods = ['example', 'anchor', 'lime', 'shap']
win = [0,0,0,0,0,0]
lose = [0,0,0,0,0,0]

num_surveys = 0
num_responses = 0

for directory in response_dirs:
	for filename in os.listdir(directory):
		if filename.endswith('.csv'):
			filepath = directory + filename
			# print(filepath)
			num_surveys += 1
			with open(filepath) as csvfile:
				csvreader = csv.reader(csvfile)
				for row in csvreader:
					if row[1] in methods:
						num_responses += 1
						win_index = methods.index(row[1])
						lose_index = methods.index(row[2])
						win[win_index] += 1
						lose[lose_index] += 1

num_people = num_surveys 

methods_print = ['example:', 'anchor:  ', 'lime:    ', 'shap:    ']
for i in range(len(methods)):
	print( "" + methods_print[i] + "\t total: " + str(win[i] + lose[i]) + "\t ratio: " + str(int(1000 * win[i] / (win[i] + lose[i])) / 10.0) + "%")

print("Collected " + str(num_surveys) + " surveys from " + str(num_people) + " people. Received " + str(num_responses) + " responses." )
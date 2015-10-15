import pandas as pd

def make_intervals(value, steps):
	if value < steps[0]:
		return 0
	elif value >= steps[0] and value < steps[1]:
		return 1
	elif value >= steps[1] and value < steps[2]:
		return 2
	elif value >= steps[2] and value < steps[3]:
		return 3
	elif value >= steps[3] and value < steps[4]:
		return 4
	else:
		return 5

if __name__ == '__main__':
	steps = {0: 150, 1: 200, 2: 250, 3: 300, 4: 350}
	df = pd.read_csv('cl_locs_w_predictions.csv')
	df['break_intervals'] = df.break_even.apply(make_intervals, steps=steps)

	df['longitude'] = df['long']
	df.drop('long', axis=1, inplace=True)
	df.to_csv('cl_locs_w_predictions.csv', encoding='utf-8')

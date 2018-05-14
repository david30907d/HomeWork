# HW3 naive-bayes-classifier-from-scratch

[程式碼從這邊參考的:https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)

4103056011 中興資工四 張泰瑋

## RUN

1. wine: `python3 bayes.py wine`
2. gaussian:`python3 bayes.py gaussian`

## Details

1. calculate mean and stdev

```
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)
```

2. then we can calculate gaussian probability density function

```
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
```

3. predict the class label of an input vector by is probability

```
def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
```

## Conclusions

1. wine:
	* accuracy:`94.91525423728814%`
2. use hw2 as data set:
	* accuracy:`51.515151515151516%`


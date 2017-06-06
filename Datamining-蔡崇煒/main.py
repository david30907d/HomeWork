from tree import GradientBoostedTrees
pos_df = spark.read  .format('org.apache.spark.sql.execution.datasources.csv.CSVFileFormat')  .option('header', 'true')  .load('testpos.csv')
neg_df = spark.read  .format('org.apache.spark.sql.execution.datasources.csv.CSVFileFormat')  .option('header', 'true')  .load('testneg.csv')
training_df = neg_df.union(pos_df)

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.evaluation import BinaryClassificationMetrics

def featureExtraction(x):
    vector = []
    if x[0]==u'p':
        vector.append(1)
    else:
        vector.append(0)
    for i in range(1,401):
        vector.append(float(x[i]))
    return vector

def score(PredictionAndLabel):
    # Instantiate metrics object
    metrics = BinaryClassificationMetrics(PredictionAndLabel)
    # Area under ROC curve
    print("Area under ROC = %s" % metrics.areaUnderROC)
    return metrics.areaUnderROC


labelpointRdd = training_df.rdd.map(featureExtraction).map(lambda x: LabeledPoint(x[0],x[1:])).cache()
labelpointRdd, TestlabelpointRdd = labelpointRdd.randomSplit([0.8,0.2])  

adaboost = []
for i in range(1,50,5):
    GBTmodel = GradientBoostedTrees.trainClassifier(labelpointRdd,categoricalFeaturesInfo={}, numIterations=i)
    predictions = GBTmodel.predict(TestlabelpointRdd.map(lambda x: x.features))
    labelsAndPredictions = TestlabelpointRdd.map(lambda lp: lp.label).zip(predictions)
    adaboost.append(score(labelsAndPredictions))


print(adaboost)
print(max(adaboost))
This is a machine learning library developed by Hongsup Oh for CS5350/6350 in University of Utah
# 1. Decision Tree
Please move to Experiment folder, and implement run.sh
## 1.1 Input variables
Sample data (S): It is represented by 2D list/array <br />
label: It is the label of each line of sample. It is represented by 1D list/array <br />
Attributes : It is represented by dictionaly. Key is attribute and it value is values of attribute <br />
Tree: Result tree is saved. It is dictionaly <br />
maxDepth: Tree's maximum depth limit<br />
cur depth: The depth of current depth. The root node is depth 1<br />
parent: Parent node of current node<br />
link: The linked edge between current node and parent node<br />
majority: Majority trend of parent node<br />
## 1.2 Generate Tree
At IG3.py, IG3 function is main function to generate Tree. Tree is dictionaly. Each path from root to current node is used as key of the Tree.
## 1.3 Evaluate data
At IG3.py, predict function helps evaluate data. Generated Tree, test sample, test label and attribute are required
## 1.4 Measure error
At IG3.py, error function works to measure error. Predict answer and label are required

# 2. Ensemble Learning
Please move to Experiment folder, and implement run.sh
## 2.1 AdaBoost
Stumps are generated t times. Current stump affect the weight of the next stump. Based on the new weight, Information gain and majority are maesured. After building t stumps, test data is evaluated with votes. 
## 2.2 Bagging
First, m' size random samples are selected with replacement. Full growth trees are generated t times with random sample.Based on t trees, test data is evaluated with votes. 
## 2.3 Random Forest
First, m' size random samples are selected with replacement. Then, speficied number of feautures are selected. Full growth trees are generated t times with random sample.Based on t trees, test data is evaluated with votes.

# 3. Linear regression
Please move to Experiment folder, and implement run.sh. The code for bias, variance decomposition is located at Experiment folder.
## 3.1 Batch Gradient Descent
It calculates gradient of the cost function by one step and update new weight vector.
## 3.2 Stochastic Gradient Descent
It calculated gradietn of the cost function one by one and immediately update new weight vector.




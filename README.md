This is a machine learning library developed by Hongsup Oh for CS5350/6350 in University of Utah
# 1. Decision Tree
## 1.1 Input variables
Sample data (S): It is represented by 2D list/array
label: It is the label of each line of sample. It is represented by 1D list/array
Attributes : It is represented by dictionaly. Key is attribute and it value is values of attribute
Tree: Result tree is saved. It is dictionaly 
maxDepth: Tree's maximum depth limit
cur depth: The depth of current depth. The root node is depth 1
parent: Parent node of current node
link: The linked edge between current node and parent node
majority: Majority trend of parent node
## 1.2 Generate Tree
At IG3.py, IG3 function is main function to generate Tree. Tree is dictionaly. Each path from root to current node is used as key of the Tree.
## 1.3 Evaluate data
At IG3.py, predict function helps evaluate data. Generated Tree, test sample, test label and attribute are required
## 1.4 Measure error
At IG3.py, error function works to measure error. Predict answer and label are required


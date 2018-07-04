# Backward_Elimination_for_Optimizing_Regression
Eliminates features based on their Chi-squared and Adj. R-squared values<br>
<p>Takes numpy array of train_set, test_set and maximum chi-squared value as arguments<br>
To use the code:<br>from Backward_Elimination import Optimize<br> 
train_set,test_set = Optimize(train_set,test_set,SLM)<br>
Default SLM = 0.05

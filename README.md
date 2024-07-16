# Overview of Logistic regression model.

The logistic regression model, also known as the logit model, estimates the probability of an event occurring based on a given dataset of independent variables. It’s commonly used for classification and predictive analytics.


1. Linear Combination: Logistic regression models the log-odds of an event as a linear combination of one or more independent variables. The coefficients in this linear combination represent the parameters of the model.


2. Logistic Function: To convert the linear combination into a probability, logistic regression uses the logistic function (also called the sigmoid function). This function maps any real-valued set of input variables to a value between 0 and 12. The logistic function is defined as:\
$$ 
P(Y=1)=\frac{1}{1+e^{-z}} 
$$​
where:
* (P(Y=1)) is the probability of the event occurring.
* (z) is the linear combination of independent variables.

3. Binary Dependent Variable: In binary logistic regression, there’s a single binary dependent variable (coded as “0” or “1”). The independent variables can be binary or continuous. The logistic model estimates the coefficients that maximize the likelihood of the observed data.


4. Classification: Although logistic regression itself doesn’t perform statistical classification, it can be used to create a binary classifier. By choosing a cutoff probability value, we classify inputs as one class if the probability exceeds the cutoff and the other class otherwise1.


Remember, logistic regression is a powerful tool for understanding relationships between variables and predicting outcomes
# Hyperparameter of the logistic regression models.
Logistic regression models have several hyperparameters that you can tune to improve their performance. Here are some of the key hyperparameters:

1. **Penalty** : This determines the type of regularization to apply. Options include:\
'l1': L1 regularization (Lasso)\
'l2': L2 regularization (Ridge)\
'elasticnet': Combination of L1 and L2\
None: No regularization\
2. **C** : This is the inverse of regularization strength. Smaller values specify stronger regularization. It’s a positive float, with the default being 1.0.\
Solver: The algorithm to use for optimization. Options include:
    * 'newton-cg'
    * 'lbfgs'
    * 'liblinear'
    * 'sag'
    * 'saga'
3. **Max_iter** : The maximum number of iterations taken for the solvers to converge. The default is 100.
Tol: The tolerance for stopping criteria. The default is {1e-4}.
4. **Fit_intercept**: Specifies if a constant (bias or intercept) should be added to the decision function. The default is True.

# Python Code for Logistic regression model.
```python
class sklearn.linear_model.LogisticRegression(penalty='l2',*,
 dual=False, 
 tol=0.0001,
 C=1.0,
 fit_intercept=True, 
 intercept_scaling=1, 
 class_weight=None, 
 random_state=None, 
 solver='lbfgs', 
 max_iter=100, 
 multi_class='deprecated', 
 verbose=0, 
 warm_start=False, 
 n_jobs=None, 
 l1_ratio=None)
```

Steps to fit a logistic regression model.
1. feature selection 
2. Baseline model fitting with KS AUC Recall Precision results
3. hyperparameter tunning (Randomized search, Grid Search, Bayesian optimization)


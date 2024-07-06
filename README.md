# Python_codes_for_univariate_analysis
 
1. Linear Regression
2. Logistic Regression

   Overview:
   Can be used for binary classification and multi class classification modelling purpose.

   Model Assumptions: -
   - Classes are linearly separable
   - Multicollinearlity not present between the feature variables.
   
   Advantages:
   - Good to use for linearly separable class.

   Disadvantages:
   - Not fit to use for non-linear separable class.
   
   Hyperparameter for logistic regression.
   - solver: {‘lbfgs’, ‘liblinear’, ‘newton-cg’, ‘newton-cholesky’, ‘sag’, ‘saga’}, default=’lbfgs’
   - penalty: {‘l1’, ‘l2’, ‘elasticnet’, None}, default='l2'
   - C: any positive values, default=1.0. Smaller values specify stronger regularization.

   **Python Code**
   ```python
   class sklearn.linear_model.LogisticRegression(penalty='l2', *, dual=False, tol=0.0001, C=1.0, fit_intercept=True,
   intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='deprecated',
   verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
   ```
   Different Methods for tunning the hyperparameter of Logistic regression
   - GridSearchCV
   - Randomised Search CV
   
   **Classification threshold for binary class classification can be selected using AUROC curve where there is maximum difference between False positive rate (FPR) and True Positive Rate**
   Performace Metrics for final model on train and test dataset
   - AUC
   - KS
   - Precision
   - Recall
     
4. SVM (Support Vector Machine)
   - Kernel ( Radial or other non linear or liner kernel)
     
5. Decision Tree (CART (Classification and regression tree)

   Overview:
   Can be used for both classification and regression modelling purpose.
   
   - Entropy of each node (Parent, Child, leaf node)
   - Information Gain 
   - Gini Impuriy of each node

   Hyperparameter of model:
   - max_depth
   - min_child_weight
   - split_criteria
   - 
7. Random Forest
   - Number of tree
   - Depth of tree
   - node size (Minimum number of observation in terminal node)
   - sample size (Proportion of sample to be drawn for each tree)
   - feature size (Number of features to randomly drawn for each tree)
   - splitting rule
8. XGBoost
   - Same parameter as Decision tree
   - learning_rate (Values lies between 0 to 1. Correction to be added by a new tree in the model)
   - gamma (Minimum loss reduction required to make a further splitting on leaf node.Prevents overfitting and puts Regularization parameter. Higher value less will be overfitting (0,inf))
9. Light GBM
   - Gradient Based one side sampling (GOSS)
   - Exclusive feature bundling
   - Histogram based binning of continuous variable.
   - Leaf wise splitting of tree node.
10. CatBoost algorithm
   - Types of features can be used in CatBoost algorithm: -
      - Text Feature
      - Categorical Feature
      - Numerical Feature
   - CatBoost tries to derive maximum information from limited data: -
      - Tends to perform good for small size of data
      - More categorical feature better the model performance
**The Cauchy-Schwarz Inequality**

```math
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
```

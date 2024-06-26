﻿# Python_codes_for_univariate_analysis
 
1. Linear Regression
2. Logistic Regression
   - L1 or L2 regularization parameter
   - Threshold for the classificaiton
3. SVM (Support Vector Machine)
   - Kernel ( Radial or other non linear or liner kernel)
4. Decision Tree (CART (Classification and regression tree)
   - Entropy of each node (Parent, Child, leaf node)
   - Information Gain 
   - Gini Impuriy of each node
5. Random Forest
   - Number of tree
   - Depth of tree
   - node size (Minimum number of observation in terminal node)
   - sample size (Proportion of sample to be drawn for each tree)
   - feature size (Number of features to randomly drawn for each tree)
   - splitting rule
6. XGBoost
   - Same parameter as Decision tree
   - learning_rate (Values lies between 0 to 1. Correction to be added by a new tree in the model)
   - gamma (Minimum loss reduction required to make a further splitting on leaf node.Prevents overfitting and puts Regularization parameter. Higher value less will be overfitting (0,inf))
7. Light GBM
   - Gradient Based one side sampling (GOSS)
   - Exclusive feature bundling
   - Histogram based binning of continuous variable.
   - Leaf wise splitting of tree node.
8. CatBoost algorithm
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

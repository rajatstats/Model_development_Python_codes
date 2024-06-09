# Python_codes_for_univariate_analysis
1. Linear Regression
2. Logistic Regression
   * L1 or L2 regularization parameter
   * Threshold for the classificaiton
4. SVM (Support Vector Machine)
   * Kernel ( Radial or other non linear or liner kernel)
   *  
6. Decision Tree (CART (Classification and regression tree)
   * Entropy of each node (Parent, Child, leaf node)
   * Information Gain 
   * Gini Impuriy of each node
7. Random Forest
   * Number of tree
   * Depth of tree
   * node size (Minimum number of observation in terminal node)
   * sample size (Proportion of sample to be drawn for each tree)
   * feature size (Number of features to randomly drawn for each tree)
   * splitting rule
8. XGBoost
   * Same parameter as Decision tree
   * learning_rate (Values lies between 0 to 1. Correction to be added by a new tree in the model)
   * gamma (Minimum loss reduction required to make a further splitting on leaf node.Prevents overfitting and puts Regularization parameter. Higher value less will be overfitting (0,inf))
10. Light GBM 
   * Gradient Based one side sampling (GOSS)
   * Exclusive feature bundling
   * Histogram based binning of continuous variable.
   * Leaf wise splitting of tree node.
11. CatBoost algorithm
   - Types of features can be used in CatBoost algorithm: -
      * Text Feature
      * Categorical Feature
      * Numerical Feature
   - CatBoost tries to derive maximum information from limited data: -
      * Tends to perform good for small size of data
      * More categorical feature better the model performance.

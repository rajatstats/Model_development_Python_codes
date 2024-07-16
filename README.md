# Python_codes_for_univariate_analysis
 
1. Linear Regression
2. Logistic Regression
   - L1 or L2 regularization parameter
   - Threshold for the classificaiton
3. SVM (Support Vector Machine)
   - Kernel ( Radial or other non linear or liner kernel)
4. Decision Tree (CART (Classification and regression tree))
   
   - Entropy of each node (Parent, Child, leaf node)
   $$
   H = -\sum_{i=1}^{k}p_i*log_2{p_i}
   \newline
   \text{H reresents the entropy of any node and k number of classes in the node.}\\p_i\text{ is the probablity of observation belonging to kth class in belonging to the node}\
   $$

   - Information Gain 
   $$
   Information\_Gain = H - \sum\frac{|H_v|}{|H|}*H_v
   $$
    H: -Entropy of parent node \
    H_v: -Entropy of child node \
    |H|: -Total instance in parent node \
    |H_v|: -Total instance child node\

   - Gini Impuriy of each node
   $$
   Gini\_Impurity = 1-\sum_{j=1}^{k}p_j^2 \newline
   $$
   where k is the number of classes in node 
   
   - Gini Index
   $$
   \sum\frac{|H_v|}{|H|}*Gini(H_v)
   $$
   Gini impurity of child node |H_v|
   
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


# Fitting logistic regression model
reg = LogisticRegression(max_iter=1000, clas_weight="balanced")
pipeline = Pipeline(steps=[('woe',woe_transform),('model',reg)])

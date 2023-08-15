# Model Selection

# Optimizing Classifiers for Different Evaluation Metrics.

# Simple accuracy is often not the right evaluation metric for many real world machine learning tasks.
         
         # False negatives and false positives may need to be treated very differently; make sure you understand the need of your application and choose an evaluation metric that matches your application, user, or business goals.

from sklearn.metrics import SCORERS

print(sorted(list(SCORERS.keys())))

# Model Calibration

# A calibrated model outputs prediction probabilities that are close to real-world observed probabilities.

    # Calibration -- ensuring accurate output probabilities.
    
        # For example a meteorologist's prediction are calibrated if across all the days where the weatherperson predicts it will rain with probability R% (predicted probability), it actually does rain R% of the time (empirical probability).
        
    # Calibration Applied to Machine Learning.
    
        # For a binary classifier given an instance xi with labels 0 or 1, a predictor is calibrated if: Across all the data points where the predictor predicts - belongs to class y=1 - with probability R% the data point actually does belong to class 1 exactly R% of the time. (i.e. predicted probability = empirical probability).
        
# Why is calibration important?

    # Many scenarios depend on having accurate prediction probabilities: decision-making; computing expectations of important quantities; modular probabilistic framework.

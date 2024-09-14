//DATA CLEANING
    -Remove Duplicate Data: Eliminate duplicate rows or entries.
    -Handle Missing Data: Remove or impute missing values.
    -Fix Structural Errors: Correct typos, inconsistent naming, and formatting issues.
    -Filter Outliers: Identify and remove outliers if necessary.
    -Standardize Data Types: Ensure consistent data types across columns (e.g., converting strings to datetime).
    -Handle Inconsistent Data: Resolve inconsistencies in data such as formatting or naming conventions.
    -Address Categorical Data: Convert categorical data to numerical form using encoding techniques.
    -Normalize/Scale Features: Apply normalization or standardization to numerical features.
    -Reduce Data: Remove irrelevant columns or rows that do not add value.
    -Validate Cleaned Data: Check for logical consistency and correctness post-cleaning.

//DATA PREPROCESSING
    -Scaling: Normalize or standardize numeric features to ensure consistency in data range.
    -Encoding Categorical Variables: Convert categorical features into numerical representations    using one-hot encoding, label encoding, or ordinal encoding.
    -Binning: Group continuous variables into discrete bins or intervals.
    -Log/Power Transformations: Apply transformations to reduce skewness or heteroscedasticity.

//FEATURE ENGINEERING
    -Interaction Features: Create new features by combining existing ones (e.g., multiplying or dividing features).
    -Polynomial Features: Generate polynomial combinations of features to capture non-linear relationships.
    -Feature Selection: Use techniques like Correlation, Chi-Square, or Recursive Feature Elimination (RFE) to select important features.
    -Dimensionality Reduction: Use Principal Component Analysis (PCA) or t-SNE to reduce the number of features while retaining important information.

//DATA SPLITTING
    -Train-Test Split: Split data into training and testing sets to avoid overfitting and ensure model generalizability.
    -Cross-Validation: Apply cross-validation (e.g., K-Fold) to assess the model's performance more robustly.
    
//HANDLING IMBALANCED DATA
    -Resampling Techniques: Apply oversampling (e.g., SMOTE) or undersampling to balance the distribution of target classes.
    -Class Weights: Assign weights to the classes to handle imbalance when training models.
    -Synthetic Data Generation: Use synthetic data generation techniques to create more examples of the minority class.
    -Text Augmentation: Apply techniques like synonym replacement or random insertion for NLP tasks.

//MODEL PREPARATION
    -Feature Scaling: Ensure numerical features are appropriately scaled (min-max, z-score) before applying models.
    -Model Selection: Choose models based on the task (e.g., regression, classification, clustering).
    -Hyperparameter Tuning: Use techniques like Grid Search or Random Search to find the best hyperparameters for the model.

//EVALUATION AND VALIDATION
    -Metrics Calculation: Compute performance metrics such as accuracy, precision, recall, F1-score, AUC, etc., depending on the problem type.
    -Confusion Matrix: Visualize the confusion matrix to understand classification performance.
    -ROC/AUC Curve: Use ROC curves to evaluate model performance on binary classification tasks.
    -Model Explainability: Use techniques like SHAP or LIME to interpret and explain model predictions.
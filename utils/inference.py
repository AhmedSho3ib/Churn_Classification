from .CustomerData import CustomerData
import pandas as pd

def predict_new(data : CustomerData, preprocessor, model):
    
    # to Dataframe
    df = pd.DataFrame([data.model_dump()])
    
    # transform
    X_processed = preprocessor.transform(df)
    
    # Predict
    y_pred = model.predict(X_processed)
    y_prob = model.predict_proba(X_processed)
    
    return {
        "Churn_prediction" : bool(y_pred[0]),
        "Churn_probability" : float(y_prob[0][1])
    }
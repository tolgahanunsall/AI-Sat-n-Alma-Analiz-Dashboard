import pandas as pd
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
    
    def fit_predict(self, data):
        predictions = self.model.fit_predict(data)
        return predictions == -1

def lstm_predict(self, X):
    """LSTM prediction"""
    try:
        predictions = self.lstm_model.predict(X)
        return predictions
    except Exception as e:
        print(f"LSTM prediction error: {e}")
        # Fallback to simple prediction
        return np.ones(len(X)) * 500
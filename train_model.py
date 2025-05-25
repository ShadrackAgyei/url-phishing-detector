import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from url_feature_extractor import extract_features

def load_and_prepare_data():
    """
    Load and prepare the phishing dataset.
    For this example, we'll create a small synthetic dataset.
    In a real application, you should use a proper phishing URL dataset.
    """
    # Create synthetic data for demonstration
    legitimate_urls = [
        'https://www.google.com',
        'https://www.amazon.com',
        'https://www.github.com',
        'https://www.microsoft.com',
        'https://www.apple.com'
    ]
    
    phishing_urls = [
        'http://googgle.com.phish.com',
        'http://amazonn-secure.com',
        'http://paypal.com.secure.phishing.com',
        'http://secure-banking.com',
        'http://login.banking-secure.com'
    ]
    
    urls = legitimate_urls + phishing_urls
    labels = [0] * len(legitimate_urls) + [1] * len(phishing_urls)
    
    return urls, labels

def train_model():
    """Train the phishing detection model."""
    print("Loading and preparing data...")
    urls, labels = load_and_prepare_data()
    
    # Extract features
    features_list = []
    feature_names = None
    
    print("Extracting features...")
    for url in urls:
        features, names = extract_features(url)
        features_list.append(features)
        if feature_names is None:
            feature_names = names
    
    X = np.array(features_list)
    y = np.array(labels)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train the model
    print("Training the model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    print("\nModel Evaluation:")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Save the model and feature names
    print("\nSaving the model...")
    joblib.dump(model, 'phishing_detector_model.joblib')
    joblib.dump(feature_names, 'feature_names.joblib')
    
    print("Model training completed and saved!")

if __name__ == "__main__":
    train_model() 
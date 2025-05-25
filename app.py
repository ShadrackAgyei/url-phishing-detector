import streamlit as st
import joblib
import numpy as np
from url_feature_extractor import extract_features
import validators

# Set page config
st.set_page_config(
    page_title="URL Phishing Detector",
    page_icon="🔒",
    layout="centered"
)

@st.cache_resource
def load_model():
    """Load the trained model and feature names."""
    try:
        model = joblib.load('phishing_detector_model.joblib')
        feature_names = joblib.load('feature_names.joblib')
        return model, feature_names
    except:
        st.error("Model files not found. Please train the model first by running train_model.py")
        return None, None

def main():
    # Add custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stAlert {
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("🔒 URL Phishing Detector")
    st.markdown("""
    This application uses machine learning to detect whether a URL is legitimate or potentially phishing.
    Enter a URL below to analyze it.
    """)
    
    # Load model
    model, feature_names = load_model()
    
    if model is None:
        return
    
    # URL input
    url = st.text_input("Enter URL to analyze:", placeholder="https://example.com")
    
    if url:
        # Validate URL format
        if not validators.url(url):
            st.error("Please enter a valid URL format (e.g., https://example.com)")
            return
        
        try:
            # Extract features
            features, _ = extract_features(url)
            
            # Make prediction
            prediction = model.predict([features])[0]
            probability = model.predict_proba([features])[0]
            
            # Display result
            st.markdown("### Analysis Result")
            
            if prediction == 0:
                st.success(f"✅ This URL appears to be legitimate (Confidence: {probability[0]:.2%})")
            else:
                st.error(f"⚠️ This URL appears to be suspicious (Confidence: {probability[1]:.2%})")
            
            # Display feature importance
            if st.checkbox("Show URL Analysis Details"):
                st.markdown("### URL Features Analysis")
                
                # Get feature importance
                importance = model.feature_importances_
                feature_importance = list(zip(feature_names, features, importance))
                feature_importance.sort(key=lambda x: x[2], reverse=True)
                
                # Display top features
                for name, value, imp in feature_importance[:5]:
                    st.write(f"- {name}: {value:.2f} (importance: {imp:.2%})")
        
        except Exception as e:
            st.error(f"Error analyzing URL: {str(e)}")
    
    # Add information about the model
    with st.expander("About this detector"):
        st.markdown("""
        This phishing URL detector uses a Random Forest classifier trained on various URL features including:
        - URL length and structure
        - Domain name characteristics
        - Special character frequency
        - Security indicators (HTTP/HTTPS)
        - And more...
        
        Note: While this tool can help identify suspicious URLs, it should not be the only method used to determine if a URL is safe.
        Always exercise caution when clicking on unknown links.
        """)

if __name__ == "__main__":
    main() 
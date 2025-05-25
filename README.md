# URL Phishing Detector

A machine learning-based web application that detects potential phishing URLs by analyzing various URL features and characteristics.

## Features

- URL feature extraction and analysis
- Machine learning-based classification using Random Forest
- User-friendly web interface built with Streamlit
- Detailed analysis of URL characteristics
- Confidence scores for predictions

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. First, train the model:
```bash
python train_model.py
```

2. Run the web application:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## How it Works

The application uses various features extracted from URLs to determine if they are potentially phishing attempts:

- URL length and structure analysis
- Domain name characteristics
- Special character frequency
- Security indicators (HTTP/HTTPS)
- TLD analysis
- And more...

The machine learning model is trained on these features using a Random Forest classifier, which provides both predictions and confidence scores.

## Note

While this tool can help identify suspicious URLs, it should not be the only method used to determine if a URL is safe. Always exercise caution when clicking on unknown links and use additional security measures when necessary.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
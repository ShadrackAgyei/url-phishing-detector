import re
from urllib.parse import urlparse
from tld import get_tld
import numpy as np

def extract_features(url):
    """Extract features from a given URL."""
    features = {}
    
    # Basic URL properties
    features['length_url'] = len(url)
    features['length_hostname'] = len(urlparse(url).netloc)
    
    # Count special characters
    features['count_dots'] = url.count('.')
    features['count_hyphens'] = url.count('-')
    features['count_at'] = url.count('@')
    features['count_question_mark'] = url.count('?')
    features['count_percent'] = url.count('%')
    features['count_equal'] = url.count('=')
    features['count_slashes'] = url.count('/')
    features['count_and'] = url.count('&')
    features['count_or'] = url.count('|')
    features['count_underscore'] = url.count('_')
    features['count_tilde'] = url.count('~')
    features['count_comma'] = url.count(',')
    features['count_plus'] = url.count('+')
    features['count_asterisk'] = url.count('*')
    features['count_hash'] = url.count('#')
    features['count_dollar'] = url.count('$')
    
    # Binary features
    features['has_ip_address'] = 1 if has_ip_address(url) else 0
    features['has_https'] = 1 if url.startswith('https://') else 0
    features['has_http'] = 1 if url.startswith('http://') else 0
    
    try:
        parsed_url = urlparse(url)
        features['has_port'] = 1 if parsed_url.port is not None else 0
        
        # TLD features
        try:
            tld_info = get_tld(url, as_object=True)
            features['tld_length'] = len(tld_info.tld)
        except:
            features['tld_length'] = 0
            
    except:
        features['has_port'] = 0
        features['tld_length'] = 0
    
    # Convert features to numpy array
    feature_names = sorted(features.keys())
    feature_values = [features[name] for name in feature_names]
    
    return np.array(feature_values), feature_names

def has_ip_address(url):
    """Check if the URL contains an IP address."""
    ipv4_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    ipv6_pattern = r'(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}'
    
    url_parts = urlparse(url)
    hostname = url_parts.netloc
    
    return bool(re.search(ipv4_pattern, hostname) or re.search(ipv6_pattern, hostname)) 
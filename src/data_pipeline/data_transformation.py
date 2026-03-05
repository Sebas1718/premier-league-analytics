# Data Transformation Module

This module is responsible for transforming raw data into a format suitable for analysis in the Premier League analytics project.

## Functions

### 1. clean_data(data)
Removes null values and cleans the dataset.

### 2. normalize_data(data)
Normalizes data ranges for consistent analysis.

### 3. feature_engineering(data)
Extracts relevant features from the dataset.

### Example Usage
```python
import pandas as pd

# Sample data
raw_data = pd.read_csv('raw_data.csv')

# Clean data
cleaned_data = clean_data(raw_data)

# Normalize data
normalized_data = normalize_data(cleaned_data)

# Feature engineering
final_data = feature_engineering(normalized_data)
```

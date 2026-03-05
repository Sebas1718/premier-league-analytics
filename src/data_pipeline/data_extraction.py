# Data Extraction Module

"""
This module includes functions for extracting data from various sources for the Premier League analytics project.
"""


def extract_data_from_api(api_url):
    """
    Extract data from a given API endpoint.
    
    Args:
        api_url (str): The URL of the API endpoint.
    
    Returns:
        dict: Parsed JSON data received from the API.
    """
    import requests
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def extract_data_from_csv(file_path):
    """
    Extract data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        list: List of dictionaries containing the data from the CSV.
    """
    import csv
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


# Example usage:
# data = extract_data_from_api('https://api.football-data.org/v2/competitions/PL/matches')
# print(data)
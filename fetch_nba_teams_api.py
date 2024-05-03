#!/usr/bin/env python
# coding: utf-8

# This is the second part of the NBA Team Data (From balldontlie api)

# In[7]:


get_ipython().system('pip install requests')
import requests
import csv

def fetch_nba_teams(api_key):
    """Fetches NBA team data using the BallDontLie API."""
    url = 'https://api.balldontlie.io/v1/teams'
    headers = {'Authorization': api_key}  
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        return []

def save_teams_to_csv(teams, filename):
    """Saves a list of NBA teams to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Conference', 'Division', 'City', 'Name', 'Full Name', 'Abbreviation'])
        for team in teams:
            writer.writerow([team['id'], team['conference'], team['division'], team['city'], team['name'], team['full_name'], team['abbreviation']])

# Main! 
api_key = '0896690f-8ed5-4825-83d3-b618bf8f883f'  # My api key
nba_teams = fetch_nba_teams(api_key)
if nba_teams:
    save_teams_to_csv(nba_teams, 'nba_teams.csv')





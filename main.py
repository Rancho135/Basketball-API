#importing all packages to flask
from flask import Flask, render_template, request
import requests
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from operator import itemgetter
from datetime import datetime
import time
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np



app = Flask('app')

#This code is commented to aviod a crash
"""
@app.route('/')

def one():
  # Get the data for the year 2021
  url = 'https://www.balldontlie.io/api/v1/games/?seasons[]=2021'
  r = requests.get(url, params = {'page':1})
  
  data = r.json()['data']
  pages = r.json()['meta']['total_pages'] #get the total number of pages
  
  for i in range(2,pages+1):
      r = requests.get(url, params = {'page':i})
      data += r.json()['data']
      time.sleep(1)
  
  home_team = []
  visitor_team = []
  home_team_score = []
  visitor_team_score = []
  for dict_ in data:
      home_team.append(dict_['home_team']['full_name'])
      home_team_score.append(dict_['home_team_score'])
      visitor_team.append(dict_['visitor_team']['full_name'])
      visitor_team_score.append(dict_['visitor_team_score'])
  
  df_2021 = pd.DataFrame({
      "Home team":home_team,
      "Visitor team":visitor_team,
      "Home team score":home_team_score,
      "Visitor team score":visitor_team_score
  })
  

  # Comparing Mean Home Teams Scores and their mean away scores.
  home_score_means = df_2021[['Home team','Home team score']].groupby('Home team')['Home team score'].mean()
  Visitor_score_means = df_2021[['Visitor team','Visitor team score']].groupby('Visitor team')['Visitor team score'].mean()
  
  x = np.arange(len(home_score_means))
  plt.figure(figsize = (13, 6))
  plt.bar(x, home_score_means, width = 0.4,color=['red'])
  plt.bar(x+0.4, Visitor_score_means, width = 0.4,color=['black'])
  plt.xlabel("Mean Visiting and Home scores: 2021")
  plt.xticks(x,labels = list(home_score_means.index), rotation = 60)
  plt.savefig("static/images/mean2021.jpg", bbox_inches = "tight")
  #add the legends
  plt.legend(['home_score_means'], loc='upper left')
  plt.legend(['Visitor_score_means'], loc='upper right')

  return render_template("index.html")
"""

@app.route('/')

def two():
  url2 = "https://www.balldontlie.io/api/v1/season_averages?season=2021&player_ids[]=200&player_ids[]=237"
  r = requests.get(url2).json() 
  #Dumping data in data.json using citys
  filename1 = 'data.json'
  with open(filename1, 'w') as file_object:
    json.dump(r, file_object, indent = 4)
    
  #Reading the data using load
  with open(filename1)as file_object:
   all_eq_data = json.load(file_object)
    
  ext = ["games_played"]
  Lebron_James, Tobias_Harris  =  [], []
  for metric in ext:
    player = all_eq_data['data'][0][metric]
    Lebron_James.append(player)
  for metric in ext:
    player = all_eq_data['data'][1][metric]
    Tobias_Harris.append(player)
  print(Lebron_James)
  print(Tobias_Harris)
  
  
  #Make a random dataset:
  height1 = [47,39]
  bars = ('Lebron_James', 'Tobias_Harris')
  y_pos = np.arange(len(bars))
    
  #Create bars
  plt.bar(y_pos, height1,color=['black', 'red'])
  plt.title("Season Average on Games Played, 2021")
    
  #Create names on the x-axis
  plt.xticks(y_pos, bars)
    
  #Show graphic
  plt.savefig("static/images/nogames.jpg", bbox_inches = "tight")
  return render_template("index.html")


@app.route('/')

def three():
    
  url3 = "https://www.balldontlie.io/api/v1/season_averages?season=2021&player_ids[]=15&player_ids[]=237"
    
  r = requests.get(url3).json()
    
    #Dumping data in data.json using citys
  filename2 = 'data1.json'
  with open(filename2, 'w') as file_object:
    json.dump(r, file_object, indent = 4)
    
    #Reading the data using load
  with open(filename2)as file_object:
    all_eq_data = json.load(file_object)
   
  ext = ["pts"]
    
  Giannis_Antetokounmpo, LeBron_James1  = [], []
  for metric in ext:
    player1 = all_eq_data['data'][0][metric]
    Giannis_Antetokounmpo.append(player1)
  for metric in ext:
    player1 = all_eq_data['data'][1][metric]
    LeBron_James1.append(player1)
    
  print(Giannis_Antetokounmpo)
  print(LeBron_James1)
  
    #Make dataset:
  height2 = [28.96,29.08]
  bars = ('Lebron_James1', 'Giannis_Antetokounmpo')
  y_pos1 = np.arange(len(bars))
      
  # Create bars
  plt.bar(y_pos1, height2,color=['black', 'red'])
  plt.title("Season Average on Points Scored")
      
  # Create names on the x-axis
  plt.xticks(y_pos1, bars)
      
  # Save graphic
  plt.savefig("static/images/avgpoints.jpg", bbox_inches = "tight")

  return render_template("index.html")


@app.route('/')
def four():
    
  url4 = "https://www.balldontlie.io/api/v1/season_averages?season=2021&player_ids[]=15&player_ids[]=237"
    
  r = requests.get(url4).json()
    
    #Dumping data in data.json using citys
  filename3 = 'data2.json'
  with open(filename3, 'w') as file_object:
    json.dump(r, file_object, indent = 4)
    
    #Reading the data using load
  with open(filename3)as file_object:
    all_eq_data = json.load(file_object)
   
  ext = ["fga"]
    
  Giannis_Antetokounmpo1, LeBron_James2  = [], []
  for metric in ext:
    player2 = all_eq_data['data'][0][metric]
    Giannis_Antetokounmpo1.append(player2)
  for metric in ext:
    player2 = all_eq_data['data'][1][metric]
    LeBron_James2.append(player2)
    
  print(Giannis_Antetokounmpo1)
  print(LeBron_James2)

    #Make dataset:
  height2 = [18.32,21.15]
  bars = ('Lebron_James2', 'Giannis_Antetokounmpo1')
  y_pos1 = np.arange(len(bars))
      
  # Create bars
  plt.bar(y_pos1, height2,color=['black', 'red'])
  plt.title("Season Average on Field Goals Attempted, 2021")
      
  # Create names on the x-axis
  plt.xticks(y_pos1, bars)
      
  # Save graphic
  plt.savefig("static/images/avgfga.jpg", bbox_inches = "tight")

  return render_template("index.html")


@app.route('/')
def five():
    
  url4 = "https://www.balldontlie.io/api/v1/season_averages?season=2021&player_ids[]=15&player_ids[]=237"
    
  r = requests.get(url4).json()
    
    #Dumping data in data.json using citys
  filename4 = 'data3.json'
  with open(filename4, 'w') as file_object:
    json.dump(r, file_object, indent = 4)
    
    #Reading the data using load
  with open(filename4)as file_object:
    all_eq_data = json.load(file_object)
   
  ext = ["fgm"]
    
  Giannis_Antetokounmpo2, LeBron_James3  = [], []
  for metric in ext:
    player3 = all_eq_data['data'][0][metric]
    Giannis_Antetokounmpo2.append(player3)
  for metric in ext:
    player3 = all_eq_data['data'][1][metric]
    LeBron_James3.append(player3)
    
  print(Giannis_Antetokounmpo2)
  print(LeBron_James3)

    #Make dataset:
  height2 = [9.91,11.03]
  bars = ('Lebron_James3', 'Giannis_Antetokounmpo2')
  y_pos1 = np.arange(len(bars))
      
  # Create bars
  plt.bar(y_pos1, height2,color=['black', 'red'])
  plt.title("Season Average on Field Goals Made 2021")
      
  # Create names on the x-axis
  plt.xticks(y_pos1, bars)
      
  # Save graphic
  plt.savefig("static/images/avgfgm.jpg", bbox_inches = "tight")

  return render_template("index.html")
  

app.run(host='0.0.0.0', port=8080)

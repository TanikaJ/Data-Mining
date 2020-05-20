## Dataset
t20.csv

## Dataset consists of the following columns:
mid - A unique number for each match
date - Date when the match took place
venue - Name of the Stadium
bat_team - Batting team
bowl_team - Bowling team
batsman - Batsman
bowler - Bowler
runs - Runs scored by the team at that point of time
wickets - Wickets lost at that point of time
overs - Number of overs bowled at that point of time
runs_last_5 - Runs scored in last 5 overs
wickets_last_5 - Wickets lost in last 5 overs
striker - max(runs scored by striker, runs scored by non-striker)
non-striker - min(runs scored by striker, runs scored by non-striker)
total - Total runs scored by team after innings

## Prediction Algorithm and Accuracy
Algorithms Used - Linear Regression
Features: [runs,wickets,overs,striker,non-striker]
Label: [total]
Accuracy in terms of [R Square Value,Custom Accuracy]
R Square Value- 52.53
Accuracy- 72.31
Accuracy is defined on the basis of difference between the predicted score and actual score. If this difference falls below a particular thresold, we count it as a correct prediction.
Thresold: 20

## Requirements
numpy==1.16.2
pandas==0.24.1
python-dateutil==2.8.0
pytz==2018.9
scikit-learn==0.20.3
scipy==1.2.1
six==1.12.0
sklearn==0.0
flask

## To Run
git clone https://github.com/KeyaShukla/Data-Mining
pip3 install -r Requirements
pip install pandas
pip install flask

For Windows:
set environment variable FLASK_APP=server.py
For tutorial: https://www.schrodinger.com/kb/1842
Variable name is FLASK_APP
Value is server.py

For Linux:
first go to directory where repository is placed
To set an environment variable on Linux, enter the following command at a shell prompt, according to which shell you are using:

setenv variable value
export variable=value

where variable is the name of the environment variable (here, FLASK_APP) and value is the value you want to assign to the variable, (here, server.py). To find out what environment variables are set, use the env command.

For MacOS:
first go to directory where repository is placed
type in the following commands:

export FLASK_APP=server.py
flask run


Copy the url provided in the terminal and paste it in the browser to run the app.

# bebobot

Discord bot connected to the Riot API that provides updates on the ranked status of the summoner b3b0.

# Initial Set Up

An additional config.py is necessary for bot functionality. This configuration file must include:
 - A Riot API Key: (variable name: api_key)
 - A Discord bot token: (variable name: discordToken)
 
To install the required packages into a python venv, use the following command:

    pip install -r requirements.txt

# Commands:

!LOL - gives the current ranked status of b3b0 in solo/duo  

!TFT - gives the current ranked status of b3b0 in ranked TFT

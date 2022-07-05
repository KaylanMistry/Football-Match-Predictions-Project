import os
import glob
import pandas as pd
import numpy as np

Season = {'Team': [], 'Home_Wins': [], 'Away_Wins': [], 'Home_Draws': [], 'Away_Draws': []}

class Football_prediction:
    def __init__(self, directory=str, team=str):
        self.directory = directory
        self.team = team

    def choose_league(self, league):
        '''
        This function specifies the league you want to collect data from and converts this to a pandas dataframe.

        The directory must be directed to the 'Results' folder, containing the results for all the leagues.
        '''
        os.chdir(f'{self.directory}{league}')
        files = glob.glob('*.csv')
        self.combined_csv = pd.concat([pd.read_csv(file) for file in files ])
        return self.combined_csv

    def find_num_of_teams(self, year=str):
        '''
        This function finds the number of teams in a certain league for a particular season.  

        To use this, requires you to use 'choose league' function before. 

        To use this fucntion, insert a specific year you require in non-string format.

        '''
        df = self.combined_csv[(self.combined_csv['Season'] == year)]
        num_of_teams = df.drop_duplicates('Home_Team', keep='first')
        for team in num_of_teams['Home_Team'].values:
            Season['Team'].append(team)
        print(len(num_of_teams.index))
    
    def choose_year(self, year=str):
        '''
        This fucntion creates a new dataframe based on the year the user chooses.

        To use this function type in the year you would like (Non-string).

        This function 'Home_Score'also creates two new coloumns to show the Home Score and Away Score.
        
        '''

        df_new = self.combined_csv[(self.combined_csv['Season'] == year)]
        self.your_df = df_new.join(df_new['Result'].str.split('-', 1, expand=True).rename(columns={0:'Home_Score', 1:'Away_Score'}))
        return self.your_df

    def who_wins(self):
        '''
        This function is used to create three extra columns depending on which team won eg. Home_Wins, Away_Wins

        User needs to activate this to calculate the number of Home and Away wins a team has.        
        '''
        self.your_df['Home_Wins'] = np.where(self.your_df['Home_Score'] > self.your_df['Away_Score'],1, np.nan)
        self.your_df['Away_Wins'] = np.where(self.your_df['Home_Score'] < self.your_df['Away_Score'],1, np.nan)
        self.your_df['Draw'] = np.where(self.your_df['Home_Score'] == self.your_df['Away_Score'],1, np.nan)
        return self.your_df
    
    def find_home_wins(self, team=str):
        '''
        This function shows the user how many Home wins a team has.

        Insert the team you would like to find the number of Home Wins for.
        '''
        teams_df = self.your_df[(self.your_df['Home_Team'] == team)]
        self.num_of_home_wins = teams_df.loc[:, 'Home_Wins'].sum()    
        print(self.num_of_home_wins)
        return self.num_of_home_wins
    
    def find_away_wins(self, team=str):
        '''
        This function shows the user how many Away wins a team has.

        Insert the team you would like to find the number of Away Wins for.
        '''
        teams_df = self.your_df[(self.your_df['Away_Team'] == team)]
        self.num_of_away_wins = teams_df.loc[:, 'Away_Wins'].sum()    
        print(self.num_of_away_wins)
        return self.num_of_away_wins
        
    def find_draws(self, team=str):
        '''
        This function shows the user how many Draws a team has.

        Insert the team you would like to find the number of Draws for.
        '''
        hometeams_df = self.your_df[(self.your_df['Home_Team'] == team)]
        num_of_homedraws = hometeams_df.loc[:, 'Draw'].sum()
        awayteams_df = self.your_df[(self.your_df['Away_Team'] == team)]
        num_of_awaydraws = awayteams_df.loc[:, 'Draw'].sum()
        self.combined_draws =  num_of_homedraws + num_of_awaydraws
        print(self.combined_draws)
        return self.combined_draws
    
    def find_losses(self):
        '''
        
        '''
        num_of_games = self.your_df['Round'].max()
        num_of_losses =  num_of_games - self.combined_draws - self.num_of_away_wins - self.num_of_home_wins
        print(num_of_losses)



if __name__ == '__main__':
    bot = Football_prediction(r'/home/kaylanm/Desktop/Football_Project/Football/Results/')
    bot.choose_league('primera_division')
    bot.find_num_of_teams(1990)
    bot.choose_year(1990)
    bot.who_wins()
    bot.find_away_wins('Athletic')
    bot.find_home_wins('Athletic')
    bot.find_draws('Athletic')
    bot.find_losses()
    




arrays = Season['Team'], Season['Home_Wins'], Season['Away_Wins'], Season['Home_Draws'], Season['Away_Draws']
max_length = 0
for array in arrays:
        max_length = max(max_length, len(array))
for array in arrays:
        array += ['NA'] * (max_length - len(array))
prezzie = pd.DataFrame(Season)
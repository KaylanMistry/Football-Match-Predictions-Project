import os
import glob
import pandas as pd


class Footabll_prediction:
    def __init__(self, directory=str):
        self.directory = directory

    def choose_league(self, league):
        '''
        This function specifies the league you want to collect data from and converts this to a pandas dataframe.

        The directory must be directed to the 'Results' folder, containing the results for all the leagues.
        '''
        os.chdir(f'{self.directory}{league}')
        files = glob.glob('*.csv')
        self.combined_csv = pd.concat([pd.read_csv(file) for file in files ])
        return self.combined_csv


    def find_num_of_teams(self, year):
        '''
        This function finds the number of teams in a certain league for a particular season.  

        To use this, requires you to use 'choose league' function before. 

        To use this fucntion, insert a specific year you require.

        '''

        df = self.combined_csv[(self.combined_csv['Season'] == year)]
        num_of_teams = df.drop_duplicates('Home_Team', keep='first')
        print(len(num_of_teams.index))
    



if __name__ == '__main__':
    bot = Footabll_prediction(r'/home/kaylanm/Desktop/Football_Project/Football/Results/')
    bot.choose_league('primera_division')
    bot.find_num_of_teams(1990)

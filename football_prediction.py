import os
import glob
import pandas as pd

os.chdir(r'/home/kaylanm/Desktop/Football_Project/Football/Results/2_liga')

files = glob.glob('*.csv')

combined_csv = pd.concat([pd.read_csv(file) for file in files ]).reset_index()
from pydoc import classname
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup


# I pledge to uphold the principles of honesty and responsibility at our university. ~ Trevor Seibert


# Dataframe
df1 = pd.read_csv('source\datasets\SASS_99_00_S2a_v1_0.csv', low_memory=False) # Public Principle --S2A
df2 = pd.read_csv('source\datasets\SASS_99_00_S4a_v1_0.csv', low_memory=False) # Public Teacher -- S4A
df3 = pd.read_csv('source\datasets\SASS_99_00_S3a_v1_0.csv', low_memory=False) # Public School -- S3A

def dataDescription():
    # Public Principal Variables and Observations
    public_principal_oberservation = df1.shape[0]
    public_principal_variables = df1.shape[1]
    print()
    print(f'The amount of observations that the Public Principal Data has is: {public_principal_oberservation}')
    print(f'The amount of variables that the Public Principad Data has is: {public_principal_variables}')
    print('The Control Numbers for the Public Principal Data is "CNTLNUM" which is the Principal Control Number and "SCHCNTL" which is the School Control Number.')
    print()
    # Public Teacher Variables and Observations
    public_teacher_observations = df2.shape[0]
    public_teacher_variables = df2.shape[1]
    print(f'The amount of Observations that the Public Teacher Data has is {public_teacher_observations}')
    print(f'The amount of Variables that the Public Teacher Data has is {public_teacher_variables}')
    print('The Control Numbers for the Public Teacher Data is "CNTLNUM" which is the Teacher Control Number and "SCHCNTL" which is the School Control Number.')
    print()

def dataProcessing():
    # Question 4 
    public_school_principals = df1.shape[0]
    male_principal = df1[(df1['A0227']==1)]
    male_principal_shape = male_principal.shape[0]
    female_principal = df1[(df1['A0227']==2)]
    female_principal_shape = female_principal.shape[0]
    print('Question 4: How many public school principals are there? How many of them are male versus female principals?')
    print(f'The number of public school principals are {public_school_principals}')
    print(f'The number of male principals are {male_principal_shape}')
    print(f'The number of female principals are {female_principal_shape}')
    print()
    # Question 5
    american_indian_principal = df1[(df1['RACETH_P']==1)]
    american_indian_principal_shape = american_indian_principal.shape[0]
    asian_principal = df1[(df1['RACETH_P']==2)]
    asian_principal_shape = asian_principal.shape[0]
    black_principal = df1[(df1['RACETH_P']==3)]
    black_principal_shape = black_principal.shape[0]
    white_principal = df1[(df1['RACETH_P']==4)]
    white_principal_shape = white_principal.shape[0]
    hispanic_principal = df1[(df1['RACETH_P']==5)]
    hispanic_principal_shape = hispanic_principal.shape[0]
    print('Question 5: How many of them are White, Black, Asian, and Hispanic principals?')
    print(f'The number of American Indian Principals are {american_indian_principal_shape}')
    print(f'The number of Asian Principals are {asian_principal_shape}')
    print(f'The number of Black Principals are {black_principal_shape}')
    print(f'The number of White Principals are {white_principal_shape}')
    print(f'The number of Hispanic Principals are {hispanic_principal_shape}')
    print()
    # Question 6
    under_forty = df1[(df1['AGE_P']==1)]
    under_forty_shape = under_forty.shape[0]
    forty_to_44 = df1[(df1['AGE_P']==2)]
    forty_to_44_shape = forty_to_44.shape[0]
    fortyfive_to_49 = df1[(df1['AGE_P']==3)]
    fortyfive_to_49_shape = fortyfive_to_49.shape[0]
    fifty_to_54 = df1[(df1['AGE_P']==4)]
    fifty_to_54_shape = fifty_to_54.shape[0]
    fiftyfive_and_over = df1[(df1['AGE_P']==5)]
    fiftyfive_and_over_shape = fiftyfive_and_over.shape[0]
    print('Question 6: What is the age distribution for these principals?')
    print(f'The number of principals that are under forty years old are {under_forty_shape}')
    print(f'The number of principals that are between 40 and 44 years old are {forty_to_44_shape}')
    print(f'The number of principals that are between 45 to 49 years old are {fortyfive_to_49_shape}')
    print(f'The number of principals that are between 50 to 54 years old are {fifty_to_54_shape}')
    print(f'The number of principals that are over 55 years old are {fiftyfive_and_over_shape}')
    print()
    # Question 7
    elementary_principals = df1[(df1['SCHLEVEL']==1)]
    elementary_principals_shape = elementary_principals.shape[0]
    secondary_school_principals = df1[(df1['SCHLEVEL']==2)]
    secondary_school_principals_shape = secondary_school_principals.shape[0]
    combined_school_principals = df1[(df1['SCHLEVEL']==3)]
    combined_school_principals_shape = combined_school_principals.shape[0]
    print('Question 7: What school levels are these principals worked at? Say elementary, middle, or high school.')
    print(f'The amount of elementary principals are {elementary_principals_shape}')
    print(f'The amount of secondary school principals are {secondary_school_principals_shape}')
    print(f'The amount of combined school principals are {combined_school_principals_shape}')
    print()
    # Question 8
    minority_one = df1[(df1['MINENR']==1)]
    minority_one_shape = minority_one.shape[0]
    minority_two = df1[(df1['MINENR']==2)]
    minority_two_shape = minority_two.shape[0]
    minority_three = df1[(df1['MINENR']==3)]
    minority_three_shape = minority_three.shape[0]
    minority_four = df1[(df1['MINENR']==4)]
    minority_four_shape = minority_four.shape[0]
    minority_not_avaliable = df1[(df1['MINENR']==-9)]
    minority_not_avaliable_shape = minority_not_avaliable.shape[0]
    summary_stats_minority = df1[['MINENR']]
    cleaning_summary_stats_minority = summary_stats_minority[(summary_stats_minority['MINENR']!=-9)]
    frequency_distribution_stats = cleaning_summary_stats_minority.describe()
    print('Question 8: Provide a frequency distribution of the schools minority student enrollment.')
    print(f'Fewer than 5 percent students: {minority_one_shape}')
    print(f'5 - 19 percent students: {minority_two_shape}')
    print(f'20 - 49 percent students: {minority_three_shape}')
    print(f'50 or more percent students: {minority_four_shape}')
    print(f'Not available because school was a noninterview: {minority_not_avaliable_shape}')
    print(frequency_distribution_stats)
    print()

def dataMerge():
    # Question 9 
    public_principal_oberservation = df1.shape[0]
    public_school_observations = df3.shape[0]
    print('Question 9: Before the merge, provide the number of observations in each file for public principal and public school data.')
    print(f'Before the merge, the number of obersvations in the Public Principal Data is {public_principal_oberservation}')
    print(f'Before the merge, the number of observations in the Public School Data is {public_school_observations}')
    print()
    # Question 10 
    merging_datasets = pd.merge(df1, df3, on="SCHCNTL")
    merging_datasets.to_csv('source\datasets\datamerge.csv')
    df4 = pd.read_csv('source\datasets\datamerge.csv', low_memory=False)
    merge_observations = df4.shape[0]
    incorrectly_merged = (public_principal_oberservation + public_school_observations - merge_observations)
    print('Question 10: After the merge, provide the number of observations that correctly merged. How many of these observations failed to merge? Explain what the cause of failure may be to merge')
    print(f'The amount of observations that correctly merged is {merge_observations}')
    print(f'The amount of observations that failed to merge is {incorrectly_merged}')
    print()
    print('There are many reasons that some observations failed to merge. Such as...')
    print(' * There are some variables that do not corrisond or left blank on their control numbers')
    print(' * Some of the schools are probably closed.')
    print(' * Some teachers volunteered their responses while there principals they worked in did not.')
    print(' * Some teachers and principals worked at multiple schools.')
    print(' * Or even some schools closed')

dataDescription()
dataProcessing()
dataMerge()


# These are wrong below. I thought we are merging the public principal with public teachers. Discard the last bit of the video. 


# pandas data merge left_on="CNTLNUM"', right_on="SCHCNTL" gives 29100 correctly merged observations
# pandas data merge on="CNTLNUM" gives 7273 correctly merged observations
# pandas data merge on="SCHCNTL" gives 39214 correctly merged observations
# pandas data merge on=["CNTLNUM","SCHCNTL"] gives 1 correctly merged observations
# Verification with SAS merge
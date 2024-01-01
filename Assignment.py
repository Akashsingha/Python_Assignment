import pandas as pd
import numpy as np
from itertools import combinations


df = pd.read_csv("Homo sapiens_9056.csv")  #read the csv convert to data frame


df = df.ffill(axis = 0) # Replaces NULL values with the value from the previous row


homo_sapiens = df['Source Organism'].str.contains('Homo sapiens') # return a df where homo sapiens are true and others are false

new_df = df[homo_sapiens]#boolean indexing to filter rows where 'Source organism' is true


#now we have new_df which all entry id is filled with the previous row, we only have Homo sapiens
result_df = new_df.groupby('Entry ID')['Accession Code(s)'].agg(list).reset_index() # here we grouping by entry id with aggregating list of accession code 

cleaned_df = result_df.drop(index=range(6)) #cleaning the unwanted data upto index 6

filtered_df = cleaned_df[cleaned_df['Accession Code(s)'].apply(lambda x: 3 == len(x))].reset_index(drop=True)

filtered_df.to_csv('cleaned_data.csv',index = False) # here we are creating a cleaned data.csv without indexing


def generate_combinations(lst):
    return [list(combination) for combination in combinations(lst, 2)]


filtered_df['Combination list']=filtered_df['Accession Code(s)'].apply(generate_combinations)
print(filtered_df) #print the result 

filtered_df.to_csv("Final_Result.csv",index = False) #Make a csv file
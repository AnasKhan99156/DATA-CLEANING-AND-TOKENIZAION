# import pandas library
import pandas as pd 

# read the file using read_cs()
df= pd.read_csv("file_name.csv")

# loop to each column in the dataset 
for column in df.columns:
    # use \W to find non-word characters in the dataset
    df[column] = df[column].str.replace(r'\W'," ")


# save the cleaned dataset
df.to_csv("file_name_for_saving.csv")
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Download the necessary dataset
# nltk.download('punkt')

# Load the dataset into a pandas DataFrame
data =pd.read_csv("file_name.csv")
df = pd.DataFrame(data)

# Define a function to tokenize the text
def tokenize_text(text):
    return word_tokenize(text)

# Apply the tokenize_text function to the text column of the DataFrame
df['tokenized_text'] = df['text'].apply(tokenize_text)

# Save the tokenized data to a CSV file
df.to_csv('file_name_to_tokenize.csv', index=False)

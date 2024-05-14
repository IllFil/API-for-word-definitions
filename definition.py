import pandas

class Definition:
    def __init__(self, term):
        self.term = term

    # Method to retrieve the definition of the term from a CSV file
    def get(self):
        df = pandas.read_csv("DataForAPI/data.csv")
        # Filter the DataFrame to find the row where the 'word' column matches the term, then retrieve its 'definition' value
        return tuple(df.loc[df['word']==self.term]['definition'])
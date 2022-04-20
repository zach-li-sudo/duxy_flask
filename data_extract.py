import pandas as pd

def fetchAll():
    data = pd.read_excel('data/data.xlsx', index_col=0)
    return data




if __name__ == "__main__":
    data = fetchAll()
    print(data.to_html())
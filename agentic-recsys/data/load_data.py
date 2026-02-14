import pandas as pd
#Load data of users, items and interactions
def load_data():
    users = pd.read_csv("data/users.csv")
    items = pd.read_csv("data/items.csv")
    interactions = pd.read_csv("data/interactions.csv")
    return users, items, interactions


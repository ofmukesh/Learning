import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame()
    x=orders['customerId'].unique()
    df['Customers']=customers[~customers['id'].isin(x)][['name']]
    return df

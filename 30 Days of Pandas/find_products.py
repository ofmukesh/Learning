import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    f_r=products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    return f_r[['product_id']]

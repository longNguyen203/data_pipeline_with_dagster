from dagster import asset, AssetExecutionContext
from etl.resources.db_conn import get_sql_connect
import pandas as pd
import logging


# Extract data from sql server
@asset(group_name="ProductCategory", compute_kind="pandas", io_manager_key="file_io")
def extract_dim_product_category(context: AssetExecutionContext) -> pd.DataFrame:
    """ Extract data from SQL server """
    with get_sql_connect() as connect:
        df = pd.read_sql_query("select * from dbo.DimProductCategory", connect)
        context.log.info(df.head())
        return df
    
# Load data
@asset(group_name="ProductCategory", compute_kind="pandas")
def dim_product_category(context: AssetExecutionContext, extract_dim_product_category: pd.DataFrame) -> pd.DataFrame:
    """ Tranform and Stage Data into Postgres """
    try:
        context.log.info(extract_dim_product_category.head())
        df = extract_dim_product_category[['ProductCategoryKey', 'EnglishProductCategoryName']]
        df = df.rename(columns={'EnglishProductCategoryName': 'ProductCategoryName'})
        return df
    except Exception as e:
        context.log.info(str(e))
    
    
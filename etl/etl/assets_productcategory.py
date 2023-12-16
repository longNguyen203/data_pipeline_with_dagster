from dagster import asset, AssetExecutionContext
from etl.resources.db_conn import get_sql_connect
import pandas as pd
import logging


# Extract data from sql server
@asset()
def extract_dim_product_category(context: AssetExecutionContext) -> pd.DataFrame:
    
    """ Extract data from SQL server """
    with get_sql_connect() as connect:
        df = pd.read_sql_query("selct * from dbo.DimProductCategory", connect)
    
from dagster import AssetKey, IOManager, io_manager, AssetExecutionContext
from pandas import DataFrame
import pandas as pd
import os


class LocalFileSystemIOManager(IOManager):
    """ Translates between Pandas DataFrames and CSVs on the local filesystem """
    
    def _get_fs_path(self, asset_key: AssetKey) -> str:
        rpath = os.path.join( "warehouse_location\\result", *asset_key.path) + ".csv"
        return os.path.abspath(rpath)
    
    def handle_output(self, context: AssetExecutionContext, obj: DataFrame):
        """ This saves the dataframe as a CSV. """
        fpath = self._get_fs_path(context.asset_key)
        context.add_output_metadata({"file path ": fpath})
        obj.to_csv(fpath)
        
    def load_input(self, context: AssetExecutionContext):
        """ This reads a dataframe from a CSV """
        fpath = self._get_fs_path(context.asset_key)      
        return pd.read_csv(fpath)
        
@io_manager
def csv_io_manager():
    return LocalFileSystemIOManager()
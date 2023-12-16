from dagster import Definitions, load_assets_from_modules

from . import assets_productcategory
from .io import file_io

all_assets = load_assets_from_modules([assets_productcategory])

defs = Definitions(
    assets=all_assets,
    resources={
        "file_io": file_io.LocalFileSystemIOManager(),
    }
)

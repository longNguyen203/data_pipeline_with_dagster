from dagster import Definitions, load_assets_from_modules

from . import assets_productcategory

all_assets = load_assets_from_modules([assets_productcategory])

defs = Definitions(
    assets=all_assets,
)

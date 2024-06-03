import requests
from io import BytesIO
from typing import List

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(): 

    
    response = requests.get(
        'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet'
    )

    # if response.status_code != 200:
    #     raise Exception(response.text)

    df = pd.read_parquet(BytesIO(response.content))
    # dfs.append(df)

    return df

@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
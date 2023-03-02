import tarfile

import pandas as pd
import requests
from rescript.types._format import CARDDatabaseFormat


def fetch_card_data(version: str = '3.2.6') -> pd.DataFrame:
    url = f"https://card.mcmaster.ca/download/0/broadstreet-v{version}.tar.bz2"
    response = requests.get(url, stream=True)
    with tarfile.open(fileobj=response.raw, mode="r|bz2") as tar:
        tar.extractall(path=f"/Users/vinzent/Desktop/bokulich_project/Code/RESCRIPt/rescript/types/tests/data/card_data_{version}")
    card_df = pd.read_json(f'/Users/vinzent/Desktop/bokulich_project/Data/card_data_{version}/card.json').transpose()
    return card_df

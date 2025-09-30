import os
import pandas as pd

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_metadata(records, out_csv):
    df = pd.DataFrame(records)
    df.to_csv(out_csv, index=False)

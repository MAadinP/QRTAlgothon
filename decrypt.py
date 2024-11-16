import cryptpandas as cp
import pandas as pd


def decrypt(filepath, pwd):
    decrypted_df = cp.read_encrypted(path=filepath, password=pwd)
    return decrypted_df

def 



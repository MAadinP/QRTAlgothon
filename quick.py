import pandas as pd
from decrypt import decrypt


def quickavg(df):
    column_names = df.columns.values.tolist()
    print(len(column_names))
    pos = 1 / float(len(column_names))
    return pos

print(quickavg(decrypt(r"release_3547.crypt", pwd="oUFtGMsMEEyPCCP6")))
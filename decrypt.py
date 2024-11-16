import cryptpandas as cp
import pandas as pd

decrypted_df = cp.read_encrypted(path=r"C:\Users\maadi\Documents\Data Science\Datathon_Prep\algothon\release_3547.crypt", password='oUFtGMsMEEyPCCP6')

print(decrypted_df)


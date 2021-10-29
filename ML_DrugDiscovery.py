# importing libraries 
import pandas as pd
from chembl_webresource_client.new_client import new_client

# search for target protein in Chembl database
target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)

# display df
# print(targets)

# select / retrieve ID for bioactivity of target protein:
# SARS cor. 3C-like proteinase
selected_target = targets.target_chembl_id[4]
# print(selected_target)

# retrieve actual activity data
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type='IC50')

df = pd.DataFrame.from_dict(res)
print(df.head(10))
print('hi')

import requests
import pandas as pd
import pycountry
df = pd.read_csv('institutional_use_counts_global.csv')

for index, row in df.iterrows():
    code = row['instCode']
    url = 'https://api.gbif.org/v1/grscicoll/institution?code='+code
    req = requests.get(url)
    if req.status_code == 200:
        res = req.json()['results']
        print("GBIF RESULTS")
        print(res)
        if len(res) > 0:
            instName = res[0].get('name')
            instType = res[0].get('type')
            address = res[0].get('mailingAddress')
            if address is not None:
                country = address.get('country')
                df.loc[index, 'country'] = country
            if instName is not None:
                df.loc[index, 'name'] = instName
            if instType is not None:
                df.loc[index, 'type'] = instType
    else:
        url = 'https://api.gbif.org/v1/grscicoll/institution?alternativeCode='+code
        req = requests.get(url)
    if req.status_code == 200:
        res = req.json()['results']
        if len(res) > 0:
            instName = res[0].get('name')
            instType = res[0].get('type')
            address = res[0].get('mailingAddress')
            if address is not None:
                country = address.get('country')
                df.loc[index, 'country'] = country
            if instName is not None:
                df.loc[index, 'name'] = instName
            if instType is not None:
                df.loc[index, 'type'] = instType
df.to_csv('institutional_use_counts_global_countries.csv', index=False)

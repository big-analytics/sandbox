
# coding: utf-8

# In[1]:

import googlemaps
import json
import pandas
import re
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBfp09visaSvIFh8hFt1yzI-wAhgs4v7uU')

df = pandas.read_csv('/Users/gratiel/Documents/work/house_location/sales.txt')
df.info()


# In[5]:

test_df = df[(df['POSTAL_CODE']==1800) & (df['BEDROOMS'].isin([3,4,5]))].head(600)

test_df["G_LOCATION"] = ''
test_df["G_LAT"] = ''
test_df["G_LNG"] = ''

#test_df.LOCATION


# In[12]:

num_location = 0
for idx, row in test_df.iterrows():
    print row
    #print "before="+row["LOCATION"]
    geocode_result = json.dumps(gmaps.geocode(row["LOCATION"]), sort_keys=True, indent=4)
    #print geocode_result
    
    #print "==================="
    
    if geocode_result.count('\n') == 0:
        formatted_address = ''
        lat = ''
        lng = ''
    else:
        parsed_result = geocode_result.split("{", 1)[1:]
        parsed_result = "{"+''.join(parsed_result)
        parsed_result = parsed_result.split("\n")[:-1]
        parsed_result = ''.join(parsed_result)
        
        #print type(parsed_result)
        #print parsed_result
        
        parsed_result = json.loads(parsed_result)
        #print parsed_result
        formatted_address = parsed_result['formatted_address']
        lat = parsed_result['geometry']['location']['lat']
        lng = parsed_result['geometry']['location']['lng']
    
    #print "after="+formatted_address
    #print lat
    #print lng
    
    test_df.G_LOCATION[idx] = formatted_address
    test_df.G_LAT[idx] = lat
    test_df.G_LNG[idx] = lng
    
#test_df


# In[ ]:

test_df

test_df.to_csv(r'/Users/gratiel/Documents/work/house_location/g_sales.txt', header=True, index=None, sep=',', mode='w')


# In[ ]:




# In[ ]:




# In[ ]:




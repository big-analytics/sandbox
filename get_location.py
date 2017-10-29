
# coding: utf-8

# In[1]:

import googlemaps
import json
import pandas

gmaps = googlemaps.Client(key='AIzaSyBfp09visaSvIFh8hFt1yzI-wAhgs4v7uU')
#gmaps = googlemaps.Client(key='AIzaSyCc2OUYIGQ7Af51hpPRJ8TeEvHKPb4yeC4')

# Read sales file and filter on a code or more
df = pandas.read_csv('/Users/gratiel/Documents/work/sandbox/sales.txt')

key = df['POSTAL_CODE'].value_counts()
print(key)

#df = df[(df['POSTAL_CODE'].isin([1081,3090,1853,1083,1780,1850,1700,1930]))]
#df = df[df['POSTAL_CODE']]
df.info()

# Read target file 
g_df = pandas.read_csv('/Users/gratiel/Documents/work/sandbox/g_sales.txt')
g_df.info()

# Match files that are not already in the target file
df = df[df["ID"].isin(g_df["ID"]) == False].head(2500)
df.info()

# In[5]:

#test_df = df[(df['POSTAL_CODE'].isin([1800,1120,1853,1020,1830])) & (df['BEDROOMS'].isin([3,4,5]))]
#test_df = df[(df['POSTAL_CODE'].isin([1800,1120,1853,1020,1830,1850]))]
#test_df = df[(df['POSTAL_CODE'].isin([1830]))]
#test_df = df[(df['POSTAL_CODE'].notnull()) & (df['BEDROOMS'].isin([3,4,5]))]

#df.info()

df["G_LOCATION"] = ''
df["G_LAT"] = ''
df["G_LNG"] = ''

#test_df.LOCATION


# In[12]:

num_location = 0
for idx, row in df.iterrows():
    #sys.stdout.write(row)
    #print (idx, row["LOCATION"])
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
        parsed_result = "{"+''.join(parsed_result).encode('utf-8')
        parsed_result = parsed_result.split("\n")[:-1]
        parsed_result = ''.join(parsed_result).encode('utf-8')
        
        #print type(parsed_result)
        #print parsed_result
        try:
            parsed_result = json.loads(parsed_result)
            formatted_address = parsed_result['formatted_address']
            lat = parsed_result['geometry']['location']['lat']
            lng = parsed_result['geometry']['location']['lng']
            #print parsed_result
        
        except:
            print "Something happened"
            pass
    
    print (idx, row["LOCATION"], " => ", formatted_address)
    
    df.G_LOCATION[idx] = formatted_address
    df.G_LAT[idx] = lat
    df.G_LNG[idx] = lng
    
#test_df


# In[ ]:

df.info()

df.to_csv(r'/Users/gratiel/Documents/work/sandbox/g_sales.txt', header=False, index=None, sep=',', mode='a', encoding='utf-8')

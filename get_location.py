
# coding: utf-8

# In[1]:

import googlemaps
import json
import pandas

gmaps = googlemaps.Client(key='AIzaSyBfp09visaSvIFh8hFt1yzI-wAhgs4v7uU')

df = pandas.read_csv('sales.txt')
df.info()


# In[5]:

#test_df = df[(df['POSTAL_CODE'].isin([1800,1120,1853,1020,1830])) & (df['BEDROOMS'].isin([3,4,5]))]
test_df = df[(df['POSTAL_CODE'].isin([1800,1120,1853,1020,1830,1850]))]
#test_df = df[(df['POSTAL_CODE'].notnull()) & (df['BEDROOMS'].isin([3,4,5]))]

test_df.info()

test_df["G_LOCATION"] = ''
test_df["G_LAT"] = ''
test_df["G_LNG"] = ''

#test_df.LOCATION


# In[12]:

num_location = 0
for idx, row in test_df.iterrows():
    #sys.stdout.write(row)
    print (idx, row["LOCATION"])
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
            
    #print "after="+formatted_address
    #print lat
    #print lng
    
    test_df.G_LOCATION[idx] = formatted_address
    test_df.G_LAT[idx] = lat
    test_df.G_LNG[idx] = lng
    
#test_df


# In[ ]:

test_df.info()

test_df.to_csv(r'g_sales.txt', header=True, index=None, sep=',', mode='w', encoding='utf-8')

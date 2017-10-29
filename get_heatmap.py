
# coding: utf-8

# *Import all the required libraries*

# In[77]:
import pandas
import folium
from folium.plugins import HeatMap

pandas.options.mode.chained_assignment = None

g_df = pandas.read_csv('/Users/gratiel/Documents/work/sandbox/g_sales.txt')
g_df = g_df[(g_df['G_LAT'].notnull()) & (g_df['G_LNG'].notnull()) & (g_df['PRICE'].notnull())]
#g_df.info()

g_df['WEIGHT'] = g_df.PRICE / g_df.BEDROOMS / 1000000
data = g_df.reset_index()[['G_LAT', 'G_LNG', 'WEIGHT']].values.astype(float).tolist()

g_df['WEIGHT'] = g_df.BEDROOMS / 10
data_2 = g_df.reset_index()[['G_LAT', 'G_LNG', 'WEIGHT']].values.astype(float).tolist()

g_df['WEIGHT'] = g_df.LIVING_AREA / 1000
g_df['WEIGHT'] = g_df['WEIGHT'].fillna(0)
data_3 = g_df.reset_index()[['G_LAT', 'G_LNG', 'WEIGHT']].values.astype(float).tolist()

g_df['WEIGHT']
#data = [[50.884218,4.3580002], [50.9244945,4.4511351]]

#print data
#print type(data)

# In[171]:

m = folium.Map(location=[50.907657, 4.373416], zoom_start=14)
HeatMap(data, radius=20).add_to(m)
m.save('/Users/gratiel/Documents/work/sandbox/heat_map_bedrooms_price.html')

m = folium.Map(location=[50.907657, 4.373416], zoom_start=14)
HeatMap(data_2, radius=20).add_to(m)
m.save('/Users/gratiel/Documents/work/sandbox/heat_map_bedrooms.html')

m = folium.Map(location=[50.907657, 4.373416], zoom_start=14)
HeatMap(data_3, radius=20).add_to(m)
m.save('/Users/gratiel/Documents/work/sandbox/heat_map_la_price.html')


# In[ ]:


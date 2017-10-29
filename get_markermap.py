
# coding: utf-8

# *Import all the required libraries*

# In[77]:
import pandas
import folium

pandas.options.mode.chained_assignment = None

g_df = pandas.read_csv('g_sales.txt')
g_df = g_df[(g_df['G_LAT'].notnull()) & (g_df['G_LNG'].notnull())]
g_df.info()


# In[171]:

m = folium.Map(
    location=[50.907657, 4.373416],
    zoom_start=14
)

#marker_cluster = MarkerCluster().add_to(m)

for idx, row in g_df.iterrows():
    infoLabel=str(row["BEDROOMS"]) + " bedrooms<br>" + str(row["LIVING_AREA"]) + " living area<br>" + str(row["LAND"]) + " land<br>" + str(row["PRICE"])
    #infoLabel=str(row["G_LAT"])
    #print infoLabel
    
    #print [row.loc["G_LAT"], row.loc["G_LNG"]]
    #print infoLabel.decode("utf8")
    
    folium.Marker(
        location=[row.loc["G_LAT"], row.loc["G_LNG"]],
        popup=infoLabel.decode("utf8"),
        icon=folium.Icon(color='red', icon='fa-home', prefix='fa')
    ).add_to(m)  

m.save('marker_map.html')
# In[ ]:


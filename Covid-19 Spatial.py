#!/usr/bin/env python
# coding: utf-8

# In[114]:


import sys
get_ipython().system('{sys.executable} --version')


# #### import necessary libraries

# In[50]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# #### for interactive visuals,prefer plotly

# In[53]:


import plotly.express as px


# In[54]:


dir(px)


# In[ ]:


get_ipython().system('pip install plotly')


# In[55]:


import plotly
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import init_notebook_mode, plot, iplot


# In[117]:


dir(plotly)


# In[116]:


print(plotly.__version__)


# In[59]:


current_data = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
current_data.head()


# In[ ]:


'''current_data.to_csv('F:/Spatial Analysis/current_covid_29Sep_data')'''


# In[65]:


type(current_data)


# In[ ]:





# ## plotting of confirmed cases

# ##### animation_frame--> Values from this column or array_like are used to assign marks to animation frames.

# #### to map country to map-assign locations='Country' & locationmode='country names' ,    
#      to assign confirmed cases of each country on map and I want colorbar as well u have to asisgn color='Confirmed'

# In[67]:


# Choropleth Map of the World
fig = px.choropleth(current_data,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date')
fig.update_layout(title='Choropleth Map of Confirmed Cases -till today',template="plotly_dark")
fig.show()


# ##### Above, We created the World Map but if we want to make a specific map for a continent we will use the scope.Let's see it by two examples of Asia and Europe.

# In[68]:


# Continent Map using Choropleth
fig = px.choropleth(current_data,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date',scope='europe')
fig.update_layout(title='Choropleth Map of Confirmed Cases - Europe till today',template="plotly_dark")
fig.show()


# In[69]:


fig = px.choropleth(current_data,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date',scope='asia')
fig.update_layout(title='Choropleth Map of Confirmed Cases - Asia on 28-09-2020',template="plotly_dark")
fig.show()


# ##### Spread over Time

# In[70]:


fig = px.scatter_geo(current_data,locations='Country',locationmode='country names',color='Confirmed',size='Confirmed',hover_name="Country",animation_frame='Date',title='Spread over Time')
fig.update(layout_coloraxis_showscale=False,layout_template="plotly_dark")
fig.show()


# #### The spread is very fast. It started in China and spread to the complete world

# #### plotting of Recovered cases

# In[71]:


fig = px.choropleth(current_data,locations='Country',locationmode='country names',color='Recovered',animation_frame='Date')
fig.update_layout(title='Choropleth Map of Recovered Cases -till today',template="plotly_dark")
fig.show()


# #### Similar to Choropleth maps, we have another cool interactive map called ‘Scatter Plot

# In[72]:


fig = px.scatter_geo(current_data,locations='Country',locationmode='country names',color='Recovered',size='Recovered',hover_name="Country",animation_frame='Date',title='Recovery over Time')
fig.update(layout_coloraxis_showscale=False,layout_template="plotly_dark")
fig.show()


# #### From above interactive map we can say that recovery is very slow as compared to the spread.

# ### The only thing we can do is prevention. We have to follow some precautions:
# 
#     1.WE have to wash our hands
#     2.WE have to cover our face with fask
#     3.We dont have to touch our face
#     4.Mainntain Social Distancing
#     5.HOME Stay if you can

# ##### plotting of Deaths

# In[73]:


fig = px.choropleth(current_data,locations='Country',locationmode='country names',color='Deaths',animation_frame='Date')
fig.update_layout(title='Choropleth Map of Deaths -till today',template="plotly_dark")
fig.show()


# In[111]:


worldometer = pd.read_csv('F:/Spatial Analysis/archive (1)/worldometer_data.csv')
worldometer.head()


# #### highlighting maximum values

# In[112]:


worldometer_new.style.background_gradient(cmap='RdPu')


# In[ ]:





# #### function For Comparison that will compare different stuffs

# In[75]:


def plot(df,x,y,xaxis_label,yaxis_label,title):
    fig = px.bar(worldometer.head(10), y=y,x=x,color='WHO Region')
    fig.update_layout(title=title,xaxis_title=xaxis_label,yaxis_title=yaxis_label)
    fig.show()


# ##### Comparison of Deaths/Million of 10 Most Affected Countries'

# In[76]:


plot(worldometer.head(10),'Country/Region','Deaths/1M pop','Country','Deaths/Million','Comparison of Deaths/Million of 10 Most Affected Countries')


# ##### Comparison of Tests/Million of 10 Most Affected Countries

# In[77]:


plot(worldometer.head(10),'Country/Region','Tests/1M pop','Country','Tests/M pop','Comparison of Tests/Million of 10 Most Affected Countries')


# In[78]:


'''
fig = go.Figure()
fig.add_trace(go.Bar(x=worldometer['Country/Region'].head(10), y=worldometer['TotalTests'].head(10)))
fig.update_layout(
    title="Plot Title",
    xaxis_title="X Axis Title",
    yaxis_title="X Axis Title")
fig.show()
'''


# In[79]:


'''
fig = px.bar(worldometer.head(10), y='Deaths/1M pop',x='Country/Region',color='WHO Region',height=400)
fig.update_layout(title='Comparison of Deaths/Million of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Deaths/Million')
fig.show()'''


# In[ ]:





# #### extract latitudes & longtidues of locations

# In[81]:


import geopy
from geopy.geocoders import Nominatim


# In[83]:


geolocator=Nominatim(user_agent="app")


# In[84]:


location = geolocator.geocode("USA")
print(location.latitude)


# In[85]:


location.longitude


# In[86]:


latest_data.head()


# In[87]:


df=latest_data.copy()


# In[88]:


df.head()


# In[89]:


df.shape


# In[90]:


df[df['Country']=='Afghanistan']


# In[91]:


df2=df.groupby(['Country'])[['Confirmed','Recovered','Deaths']].max().reset_index()


# In[92]:


df2.head()


# In[93]:


df2[df2['Country']=='India']


# In[94]:


lat_lon=[]
geolocator=Nominatim(user_agent="app")
for location in df2['Country']:
    location = geolocator.geocode(location)
    if location is None:
        lat_lon.append(np.nan)
    else:    
        geo=(location.latitude,location.longitude)
        lat_lon.append(geo)


# In[95]:


lat_lon


# In[96]:


df2['geo_loc']=lat_lon


# In[97]:


#### unzip it
lat,lon=zip(*np.array(df2['geo_loc']))


# In[98]:


df2['lat']=lat
df2['lon']=lon


# In[99]:


df2.head()


# In[100]:


df2.drop(['geo_loc'],axis=1,inplace=True)


# In[101]:


df2.head()


# In[102]:


df2.to_csv('F:/Spatial Analysis/Spatial_data.csv')


# ##### We have found out latitude and longitude of each location listed in the dataset using geopy.
# ##### This is used to plot maps.

# In[ ]:





# ## places which cases are Confirmed recently through the world in the past day alone¶

# Plotting Markers on the Map
#   Folium gives a folium.Marker() class for plotting markers on a map
#   Just pass the latitude and longitude of the location, mention the popup and tooltip and add it to the map.
# 
# #### Plotting markers is a two-step process.
#     1) you need to create a base map on which your markers will be placed
#     2) and then add your markers to it:

# In[1]:


import folium


# In[121]:


folium.Map(tiles='openstreetmap', zoom_start=2)


# In[104]:


# Create a map
m = folium.Map(location=[54, 15], tiles='openstreetmap', zoom_start=2)

# Add points to the map
for id,row in df2.iterrows():
    folium.Marker(location=[row['lat'],row['lon']], popup=row['Confirmed']).add_to(m)

# Display the map
m


# ##### These are places which cases are Confirmed recently through the world in the past day alone

# In[105]:


m = folium.Map(location=[54, 15], tiles='openstreetmap', zoom_start=2)

# Add points to the map
for idx, row in df2.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['Recovered']).add_to(m)

# Display the map
m


# In[ ]:





# In[106]:


m = folium.Map(location=[54, 15], tiles='openstreetmap', zoom_start=2)

# Add points to the map
for idx, row in df2.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['Deaths']).add_to(m)

# Display the map
m


# ##### Deaths are from these marked placesin the past day alone

# In[ ]:





# In[107]:


m = folium.Map(location=[54,15], tiles='cartodbpositron', zoom_start=2)

# Add points to the map
from folium.plugins import MarkerCluster
mc = MarkerCluster()
for idx, row in df2.iterrows():
    mc.add_child(folium.Marker([row['lat'], row['lon']],popup=row['Confirmed']))
m.add_child(mc)

# Display the map
m


# ##### These are the Total number cases registered till date in respective regions through out the world

# In[108]:


from folium.plugins import HeatMap


# In[109]:


df2.head()


# In[110]:


# Create map with overall cases registered
m = folium.Map(location=[54,15], zoom_start=2)
HeatMap(data=df2[['lat', 'lon','Confirmed']], radius=15).add_to(m)

# Show the map
m


# #### In these regions the effect of corona virus is more till date. Countries like Brazil,India & US are suffering a lot.

# In[ ]:





# In[ ]:





# In[ ]:





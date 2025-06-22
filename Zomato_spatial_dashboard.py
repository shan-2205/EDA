


# first use below code in jupyter notebook to store data in ::
    
# rest_loc.to_csv(r'R:\All_Datasets\Spatial_Analysis\1.. Zomato/Zomato_Bengalore_rest_coordinates.csv', index = False)  #3rd session
# df.to_csv(r"R:\All_Datasets\Spatial_Analysis\1.. Zomato/processed_Zomato.csv" , index = False)  #8th session




import streamlit as st
import pandas as pd

import folium
from folium.plugins import HeatMap, FastMarkerCluster

import warnings

# Suppress warnings
warnings.filterwarnings('ignore')


df = pd.read_csv(r'R:\All_Datasets\Spatial_Analysis\1.. Zomato/processed_Zomato.csv')
rest_loc = pd.read_csv(r'R:\All_Datasets\Spatial_Analysis\1.. Zomato/Zomato_Bengalore_rest_coordinates.csv')






# --- Streamlit App ---

## set_page_config() : configure the basic settings of your web application page.
## page_title = "Bitcoin Dashboard":
## This sets the title that appears in your browser tab or window..
## layout = "wide": , ie  your content is arranged horizontally on the page.
## ie  you're telling Streamlit to make your content stretch across almost the entire width of the browser window
# --- Configuration ---
st.set_page_config(
    page_title="Zomato Bangalore Restaurants Dashboard",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Zomato Bangalore Restaurants Dashboard")
st.write("Explore restaurant distribution and ratings in Bangalore based on the Zomato dataset.")
st.markdown("---")



# --- Generate Base Map ---
def generate_basemap(location=[12.97, 77.59], zoom_start=12):
    """Generates a Folium base map centered on Bangalore."""
    basemap = folium.Map(location=location, zoom_start=zoom_start)
    return basemap

    st.markdown("---")



# --- Section 1: Where are most number of restaurants located? --
st.header("📍 Restaurant Distribution Analysis")
st.write("This section visualizes the density of restaurants across Bangalore.")

st.subheader("Top Locations by Number of Restaurants:")
Rest_locations = df['location'].value_counts().reset_index()
Rest_locations.columns = ['Name' , 'count']

Beng_rest_locations = Rest_locations.merge(rest_loc , on = "Name")
st.dataframe(Beng_rest_locations.sort_values(by='count', ascending=False).head(10))
## st.dataframe() : Its a way to show tabular data



# HeatMap for Restaurant Density
st.subheader("Heatmap of Restaurant Density")
st.write("Areas with higher restaurant density will appear brighter.")
basemap_density = generate_basemap()
HeatMap(Beng_rest_locations[['lat', 'lon', 'count']].values.tolist()).add_to(basemap_density)

st_folium_density = basemap_density._repr_html_()
## _repr_html_() : converts the Folium map (basemap_density) into HTML code that can be displayed in a browser.

st.components.v1.html(st_folium_density, height=500)
# This tells Streamlit to show raw HTML content (like a custom web page).
# It displays the HTML map inside the Streamlit app.
# height=500 sets the height of the map in pixels.

# st – This is the Streamlit module.
# components – sub-module for adding custom web components
# v1 – Version 1 of the component API.
# html(...) – A method that takes raw HTML code and renders it in your app.


## Summary : Take the map, turn it into a web format (HTML), and show that HTML inside the Streamlit app..



# Marker Cluster Map of : Where are most number of restaurants located ?
st.subheader("Marker Cluster Map of Restaurants")
st.write("Zoom in to see individual restaurant locations. Clusters indicate high density.")
basemap_marker = generate_basemap()

# Ensure data for FastMarkerCluster is just lat/lon pairs
FastMarkerCluster(Beng_rest_locations[['lat', 'lon']].values.tolist()).add_to(basemap_marker)
st_folium_marker = basemap_marker._repr_html_()
st.components.v1.html(st_folium_marker, height=500)


st.markdown("---")






# --- Section 2 : Plotting all the markers of places of Bangalore !


# Add points to the map

st.subheader("All restaurant Markers in Bangalore")
m = generate_basemap() ## it will generate basemap

for index , row in Beng_rest_locations.iterrows():
    popup_text = "<b>Place:</b> " + str(row['Name']) + "<br><b>Restaurants:</b> " + str(row['count'])
    folium.Marker(location = [row['lat'] , row['lon']] , popup = popup_text , 
                  icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
markers = m._repr_html_()
st.components.v1.html(markers, height=500)
st.write("Each marker represents a location with the number of restaurants in that area.")






# --- Section 3 : Highest Rated Restaurants Analysis ---
st.header("⭐ Top-Rated Restaurants Analysis")
st.write("This section shows the locations with high average restaurant ratings.")

# Group by location for average rating and total orders
grp_df = df.groupby(['location'] , as_index=False).agg({'rating':'mean' , 'name':'size'})
grp_df.columns = ['Name' , 'avg_rating' , 'count']

st.subheader("Filter for Top-Rated Locations")
min_orders_threshold = st.slider(
        "Minimum Number of Orders (to consider a location for rating analysis):",
        min_value=100,
        max_value=2000,
        value=400,
        step=50
    )

## st.slider() will create a slider 

temp_df_filtered = grp_df[grp_df['count'] >= min_orders_threshold]

# Merge with geocoded locations
ratings_locations = temp_df_filtered.merge(rest_loc, on='Name', how='inner')

st.subheader(f"Locations with Average Rating (Min. {min_orders_threshold} Orders):")
st.dataframe(ratings_locations.sort_values(by='avg_rating', ascending=False).head(10))


# HeatMap for Highest Rated Restaurants : 
st.subheader("Heatmap of Average Restaurant Ratings")
st.write("Areas with higher average ratings will appear brighter. Filtered by minimum orders.")
basemap_ratings = generate_basemap()

# Ensure the third parameter for HeatMap is the 'value' (avg_rating)
HeatMap(ratings_locations[['lat', 'lon', 'avg_rating']].values.tolist()).add_to(basemap_ratings)
st_folium_ratings = basemap_ratings._repr_html_()
st.components.v1.html(st_folium_ratings, height=500)



# In[ ]:


## (base) : indicates that you're working in the base Conda environment.
## PS : Stands for PowerShell, which is the shell (command-line interface) you're using in Windows.
## It's saying you're currently in the C:\Users\shant folder

# Summary : (base) PS C:\Users\shant> =>> You're using PowerShell [PS] (in base Conda environment)






## open powershell prompt : 
## cd "R:\3.. Entire_Spatial_Analysis_Projects\1.. Zomato_use_case\2.. Current_Spatial_Zomato_Udemy"
## streamlit run Zomato_spatial_dashboard.py









# In[ ]:

#What Happens Next?
#Once you run the command, streamlit run SP_500_dashbaording.py :

#Launches a local web server.

#Opens the app in your default browser (or gives you a local URL like http://localhost:8501).

#Renders the dashboard defined in your SP_500_dashbaording.py







import pandas as pd # data pre-processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt ## data viz libraries 
import seaborn as sns


df = pd.read_csv(r'R:\All_Datasets\Data_Analysis_Projects\Bitcoin/bitcoin_price_Training - Training.csv')
df['Date'] = df['Date'].astype('datetime64[ns]')
df.sort_values(by = "Date")
data = df.sort_index(ascending=False).reset_index()
data.drop('index' , axis=1 , inplace=True)



bitcoin_sample = data[0:50]





import plotly.graph_objs as go

import plotly.express as px

from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot

import cufflinks as cf


cf.go_offline()


# In[32]:


init_notebook_mode(connected=True)


data.set_index('Date' , inplace=True)


data['Close_price_pct_change'] = data['Close'].pct_change()*100





# In[ ]:



import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np


# In[71]:


# --- Streamlit App ---

## set_page_config() : configure the basic settings of your web application page.
## page_title="Bitcoin Dashboard":
## This sets the title that appears in your browser tab or window..
## layout="wide": , ie  your content is arranged horizontally on the page.
## ie  you're telling Streamlit to make your content stretch across almost the entire width of the browser window

st.set_page_config(page_title="Bitcoin Dashboard", layout="wide")
st.title("📈 Comprehensive Bitcoin Price Analysis Dashboard")

# --- Candlestick Chart ---
st.subheader("Bitcoin Candlestick Chart (First 100 Days)") ## smaller heading (a subheader) in your web application  , 
                                                         ## like H2 heading in HTMLl
bitcoin_sample = data.iloc[0:100]
fig_candle = go.Figure(data=[
    go.Candlestick(
        x=bitcoin_sample.index,
        open=bitcoin_sample['Open'],
        high=bitcoin_sample['High'],
        low=bitcoin_sample['Low'],
        close=bitcoin_sample['Close']
    )
])
fig_candle.update_layout(xaxis_rangeslider_visible=False, template='plotly_white')
st.plotly_chart(fig_candle, use_container_width=True)

# --- Daily Percentage Change ---
st.subheader("Daily Percentage Change in Closing Price")
fig_pct = go.Figure([
    go.Scatter(
        x=data.index,
        y=data['Close_price_pct_change'],
        mode='lines',
        line=dict(color='#2ecc71')
    )
])
fig_pct.update_layout(
    xaxis_title='Date',
    yaxis_title='Percentage Change (%)',
    template='plotly_white'
)
st.plotly_chart(fig_pct, use_container_width=True)

# --- Dropdown for Historical Price Trends ---
st.subheader("Bitcoin Price Trends Over Time")
price_type = st.selectbox("Select Price Type:", options=['Open', 'High', 'Low', 'Close'], index=3)
fig_trend = go.Figure([
    go.Scatter(
        x=data.index,
        y=data[price_type],
        mode='lines',
        line=dict(color='#3498db')
    )
])
fig_trend.update_layout(
    title = price_type + " Price Over Time",
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    template='plotly_white'
)
st.plotly_chart(fig_trend, use_container_width=True)




# --- Aggregated Charts: Yearly, Quarterly, Monthly ---
col1, col2, col3 = st.columns(3)
## ie I want to divide the horizontal space on my webpage into three equal-sized vertical sections (or columns).
## Give me a variable(containers) for each of these sections so I can put stuff like plots ,texts etc.. inside them."


## with keyword here is saying for col1 , put all these operations !
with col1:
    st.subheader("Yearly Average Close Price")
    yearly_avg = data['Close'].resample('YE').mean()

    fig_year = px.bar(
        x=yearly_avg.index.strftime('%Y'), # Extract year as string for x-axis
        y=yearly_avg.values,              # Use the values of the Series for y-axis
        labels={'x': 'Year', 'y': 'Average Value'}, # Optional: customize axis labels
        title='Yearly Average Trend' )    # Optional: add a title
    st.plotly_chart(fig_year, use_container_width=True)


with col2:
    st.subheader("Quarterly Average Close Price")
    quarterly_avg = data['Close'].resample('QE').mean()
    fig_quarter = px.bar(
            x=quarterly_avg.index.strftime('%Y-Q%q'),
            y=quarterly_avg.values, # Use .values to pass the Series data
            labels={'x': 'Quarter', 'y': 'Average Price'}, # Customize axis labels
            title='Quarterly Average Bitcoin Price') # Add a title

    st.plotly_chart(fig_quarter, use_container_width=True)


with col3:
    st.subheader("Monthly Average Close Price")
    monthly_avg = data['Close'].resample('ME').mean()

    fig_month = px.line(x=monthly_avg.index, y=monthly_avg,
                    labels={'x': 'Month', 'y': 'Average Price'},
                    title='Monthly Average Bitcoin Price Trend')
    st.plotly_chart(fig_month, use_container_width=True)



# --- Closing Price: Normal vs Log ---
col4, col5 = st.columns(2)

with col4:
    st.subheader("Closing Price (Normal Scale)")
    # Using plotly.express for normal scale
    fig_normal = px.line(data, x=data.index, y='Close',
                         labels={'x': 'Date', 'Close': 'Closing Price'},
                         title='Bitcoin Closing Price Trend (Normal Scale)')
    st.plotly_chart(fig_normal, use_container_width=True)

with col5:
    st.subheader("Closing Price (Log Scale)")
    # Using plotly.express for log scale
    # Apply log1p directly to the 'Close' column for plotting
    fig_log = px.line(data, x=data.index, y=np.log1p(data['Close']),
                      labels={'x': 'Date', 'y': 'log(Closing Price + 1)'}, # Label y-axis appropriately
                      title='Bitcoin Closing Price Trend (Log Scale)')
    st.plotly_chart(fig_log, use_container_width=True)


# In[ ]:


## (base) : indicates that you're working in the base Conda environment.
## PS : Stands for PowerShell, which is the shell (command-line interface) you're using in Windows.
## It's saying you're currently in the C:\Users\shant folder

# Summary : (base) PS C:\Users\shant> =>> You're using PowerShell [PS] (in base Conda environment)




# In[ ]:

## open anaconda powershell prompt : 
## cd "R:\1.. Entire_Data_Analytics_Project\Bitcoin"
## streamlit run bitcoin_analysis_dashboard.py



# In[ ]:

#What Happens Next?
#Once you run the command, streamlit run SP_500_dashbaording.py :

#Launches a local web server.

#Opens the app in your default browser (or gives you a local URL like http://localhost:8501).

#Renders the dashboard defined in your SP_500_dashbaording.p




# In[ ]:





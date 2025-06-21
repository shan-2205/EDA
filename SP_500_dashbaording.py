








import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import glob



files = [
        r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\AAPL_data.csv',
        r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\AMZN_data.csv',
        r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\GOOG_data.csv',
        r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\MSFT_data.csv'
    ]

def load_data():
    df = pd.DataFrame()
    for file in files:
        temp = pd.read_csv(file)
        df = pd.concat([df , temp] , ignore_index=True)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Load data
df = load_data()









# --- Streamlit App ---

## set_page_config() : configure the basic settings of your web application page.
## page_title="Bitcoin Dashboard":
## This sets the title that appears in your browser tab or window..
## layout="wide": , ie  your content is arranged horizontally on the page.
## ie  you're telling Streamlit to make your content stretch across almost the entire width of the browser window
st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")
st.title("📊 Tech Stocks Analysis Dashboard")



tech_list = df['Name'].unique()

# Sidebar
st.sidebar.title("Choose a Company")
selected_company = st.sidebar.selectbox("Select a stock", tech_list)

# Filter data for selected company
company_df = df[df['Name'] == selected_company]
company_df.sort_values('date', inplace=True)




# --- Section 1: Stock Price over Time ---
st.subheader(f"1. 📈 Closing Price of {selected_company} Over Time") 
## smaller heading (a subheader) in your web application , ## like H2 heading in HTMLl

fig1 = px.line(company_df, x='date', y='close', title=selected_company + " Closing Price Over Time")
st.plotly_chart(fig1, use_container_width=True)
## st.plotly_chart() : to display an interactive Plotly chart in your Streamlit app.
## use_container_width=True : to make chart automatically adjust its width to fit the full width of the container



# --- Section 2: Moving Averages ---
st.subheader("2. 🧮 Moving Averages (10, 20, 50 days)")

ma_day = [10, 20, 50]
for ma in ma_day :
    company_df['close_' + str(ma)] = company_df['close'].rolling(ma).mean()

fig2 = px.line(company_df, x='date', y=['close', 'close_10', 'close_20', 'close_50'],
               title=selected_company + " Closing Price with Moving Averages")
st.plotly_chart(fig2 , use_container_width=True)



# --- Section 3: Daily Returns ---
st.subheader("3. 📉 Daily Returns for " + selected_company)
company_df['Daily Return (%)'] = company_df['close'].pct_change() * 100
fig3 = px.line(company_df, x='date', y='Daily Return (%)', title='Daily Return (%)')
st.plotly_chart(fig3, use_container_width=True)



# --- Section 4: Resampled Data ---
st.subheader("4. ⏱️ Resampled Closing Price (Monthly / Quarterly / Yearly)")

company_df.set_index('date', inplace=True)

## it creates a radio button UI where the user can select only one option from a list.
resample_option = st.radio("Select Resample Frequency", ['Monthly', 'Quarterly', 'Yearly'])

if resample_option == 'Monthly':
    resampled = company_df['close'].resample('ME').mean()
elif resample_option == 'Quarterly':
    resampled = company_df['close'].resample('QE').mean()
else:
    resampled = company_df['close'].resample('YE').mean()

fig4 = px.line(resampled, title=selected_company + ' ' + resample_option + ' Average Closing Price')

st.plotly_chart(fig4, use_container_width=True)

company_df.reset_index(inplace=True)  # restore index for next use




# --- Section 5: Correlation Heatmap ---
st.subheader("5. 📌 Correlation Between Companies (Closing Prices)")


app = pd.read_csv(files[0])
amzn = pd.read_csv(files[1])
google = pd.read_csv(files[2])
msft = pd.read_csv(files[3])

closing_price = pd.DataFrame()

closing_price['apple_close'] = app['close']
closing_price['amzn_close'] = amzn['close']
closing_price['goog_close'] = google['close']
closing_price['msft_close'] = msft['close']

fig5, ax = plt.subplots()
sns.heatmap(closing_price.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig5)




# # --- Section 6: Daily Return Correlation ---
# st.subheader("6. 🔁 Daily Return Correlation Between Stocks")

# @st.cache_data
# def get_daily_return_corr():
#     file_paths = {
#         'apple_close': r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\AAPL_data.csv',
#         'amzn_close': r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\AMZN_data.csv',
#         'goog_close': r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\GOOG_data.csv',
#         'msft_close': r'R:\All_Datasets\3.. S_&_P\Datasets\individual_stocks_5yr\\MSFT_data.csv'
#     }
#     daily_return = pd.DataFrame()
#     for col, path in file_paths.items():
#         df_temp = pd.read_csv(path)
#         daily_return[col + '_pct'] = df_temp['close'].pct_change() * 100
#     return daily_return.corr()

# fig6, ax2 = plt.subplots()
# sns.heatmap(get_daily_return_corr(), annot=True, cmap='YlGnBu', ax=ax2)
# st.pyplot(fig6)



st.markdown("---")
st.markdown("📌 **Note:** This dashboard provides basic technical analysis of major tech stocks using Python and Streamlit.")





## (base) : indicates that you're working in the base Conda environment.
## PS : Stands for PowerShell, which is the shell (command-line interface) you're using in Windows.
## It's saying you're currently in the C:\Users\shant folder


# Summary : (base) PS C:\Users\shant> =>> You're using PowerShell [PS] (in base Conda environment) 




## open powershell prompt : 
## cd "R:\1.. Entire_Data_Analytics_Project\S & P 500"
## streamlit run SP_500_dashbaording.py # This is a command used to launch a Streamlit app from a Python file.





#What Happens Next?
#Once you run the command, streamlit run SP_500_dashbaording.py :

#Launches a local web server.

#Opens the app in your default browser (or gives you a local URL like http://localhost:8501).

#Renders the dashboard defined in your SP_500_dashbaording.p









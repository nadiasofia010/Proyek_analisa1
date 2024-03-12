import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='white')
st.set_option('deprecation.showPyplotGlobalUse', False)


df = pd.read_csv("hour_cleaned.csv")


def season(df):
    season_data = df.groupby(['Season'])['Total_rental'].sum().reset_index()
    return season_data

def weekday(df):
    weekday_data = df.groupby(['Weekday'])['Total_rental'].sum().reset_index()
    return weekday_data


season_data = season(df)
weekday_data = weekday(df)

# Sidebar filter
with st.sidebar:
    st.image("https://example.com/image.jpg")
    weekday_select = st.multiselect("Filter weekdays", weekday_data['Weekday'].unique(), default=weekday_data['Weekday'].unique())

st.header(':bike: Bicycle Rental Analysis')
st.subheader(':bike: Total Customers')

columns = st.columns(1)


with columns[0]:
    total_rental_sum = df['Total_rental'].sum()
    st.metric('Total Customers', total_rental_sum)


with st.container():
    st.subheader('Distribusi penyewaan sepeda berdasarkan waktu pada hari kerja dan hari libur:')
filtered_season = season_data[season_data['Season'].isin(selected_season)]

if filtered_season.empty:
    st.write("No data available for the selected seasons.")
else:
    sns.barplot(x='Season', y='Total_rental', data=filtered_season)
    plt.xlabel('Season')
    plt.ylabel('Total Bicycle Rentals')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot()


# Container for weekday filter
with st.container():
    st.subheader('Perbedaan pola penyewaan sepeda antara hari kerja dan hari libur:')
    filtered_weekday = df[df['Weekday'].isin(weekday_select)]

    if not filtered_weekday.empty:
        weekday_plot = filtered_weekday.groupby('Weekday')['Total_rental'].sum().reset_index()
        sns.barplot(x='Weekday', y='Total_rental', data=weekday_plot)
        plt.xlabel('Weekday')
        plt.ylabel('Total Bicycle Rentals')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()
    else:
        st.write("Please select at least one filter.")


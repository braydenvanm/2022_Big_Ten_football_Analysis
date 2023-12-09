import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('2022_data.csv')

df = df
df['Logo'] = "Logos/" + df['Team'] + '.png'
team_colors = {
    "Illinois": '#E84A27',
    "Indiana": '#990000',
    "Iowa": '#FFCD00',
    "Maryland": '#E03A3E',
    "Michigan State": '#18453B',
    "Michigan": '#FFCB05',
    "Minnesota": '#7A0019',
    "Nebraska": '#E41C38',
    "Northwestern": '#4E2A84',
    "Ohio State": '#BB0000',
    "Penn State": '#041E42',
    "Purdue": '#CEB888',
    "Rutgers": '#000000',
    "Wisconsin": '#C5050C',
}

st.title('Big Ten Football Stats and Analysis')
st.text('Vizualizations of common statistics for Big Ten Football Teams in 2022')

st.header('Top Defensive Teams by Season')
Year_Select = st.selectbox('Season',[2019,2020,2021,2022,2023])
Defense_Select = st.selectbox('Metric Select',['interceptions','interceptionTDs','sacks','tacklesForLoss'])

Year_df = df[df.Season == Year_Select]

Defense = sns.barplot(Year_df, y="Team", x=Defense_Select, legend=False, palette= team_colors)
for i in Defense.containers:
    Defense.bar_label(i,fontsize=8)
# Offense = alt.Chart(Year_df, title = '2022 Big Ten Best Offenses').mark_circle(
#     width=30,
#     height=30
# ).encode(
#     alt.X('rushingYards:Q').scale(zero=False),
#     alt.Y('netPassingYards').scale(zero=False)
# ).interactive()
st.text(f"Top teams by {Defense_Select} for the {Year_Select} season.")
st.pyplot(Defense.get_figure())

# Logos_Teams = alt.Chart(df, title = '2022 Big Ten Best Offenses').mark_image(
#     width=30,
#     height=30
# ).encode(
#     alt.X('rushingYards:Q').scale(zero=False),
#     alt.Y('netPassingYards').scale(zero=False),
#     url='Logo',
#     tooltip=['Season','Team','rushingYards','netPassingYards']
# ).interactive()

# st.altair_chart(Logos_Teams, use_container_width= True)
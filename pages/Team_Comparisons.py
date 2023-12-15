import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data/2022_data.csv')

st.title('Big Ten Football Stats and Analysis')
st.text('Side by Side Team Comparisons')

st.text('It is important to note that the 2020 Season was shortened due to the pandemic')

Team_Stats = df.groupby(['Season','Team'], as_index=False).sum()

Team_Stats = Team_Stats.astype({"Season": str,"Team": str})

Team_1_Selection = st.selectbox('Team 1 Select',['Illinois','Indiana','Iowa','Maryland','Michigan','Michigan State','Minnesota','Nebraska','Northwestern','Ohio State','Penn State','Purdue','Rutgers','Wisconsin'])
Team_2_Selection = st.selectbox('Team 2 Select',['Illinois','Indiana','Iowa','Maryland','Michigan','Michigan State','Minnesota','Nebraska','Northwestern','Ohio State','Penn State','Purdue','Rutgers','Wisconsin'])

Team_1_Stats = Team_Stats[Team_Stats.Team == Team_1_Selection]
Team_2_Stats = Team_Stats[Team_Stats.Team == Team_2_Selection]

Metric_Select = st.selectbox('Metric Select',['firstDowns','fourthDownConversions','fourthDowns','fumblesLost','fumblesRecovered','games',
                                              'interceptions','interceptionTDs','interceptionYards','kickReturns','kickReturnTDs','kickReturnYards',
                                              'netPassingYards','passAttempts','passCompletions','passesIntercepted','passingTDs','penalties','penaltyYards',
                                              'possessionTime','puntReturns','puntReturnTDs','puntReturnYards','rushingAttempts','rushingTDs','rushingYards','sacks',
                                              'tacklesForLoss','thirdDownConversions','thirdDowns','totalYards','turnovers'])

col1, col2 = st.columns(2)

Team_1_Stats_Chart = alt.Chart(Team_1_Stats, title = (f"Total {Team_1_Selection} stats")).mark_line(
    width=30,
    height=30,
    point = alt.OverlayMarkDef(filled=False, fill="red")
).encode(
    alt.X('Season').scale(zero=False),
    alt.Y(Metric_Select).scale(zero=False),
    text = Metric_Select,
    tooltip=['Season', Metric_Select]
).interactive()

with col1:
    st.altair_chart(Team_1_Stats_Chart, use_container_width= True)

Team_2_Stats_Chart = alt.Chart(Team_2_Stats, title = (f"Total {Team_2_Selection} stats")).mark_line(
    width=30,
    height=30,
    point = alt.OverlayMarkDef(filled=False, fill="blue")
).encode(
    alt.X('Season').scale(zero=False),
    alt.Y(Metric_Select).scale(zero=False),
    text = Metric_Select,
    tooltip=['Season', Metric_Select]
).interactive()

with col2:
    st.altair_chart(Team_2_Stats_Chart, use_container_width= True)
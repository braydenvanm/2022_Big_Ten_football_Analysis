import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data/2022_data.csv')

st.title('Big Ten Football Stats and Analysis')
st.text('Total Conference Stats by Season')

st.text('It is important to note that the 2020 Season was shortened due to the pandemic')

seasons_only = df.drop(["Team"], axis = 1)

Conference_Stats = seasons_only.groupby(['Season'], as_index=False).sum()

Conference_Stats = Conference_Stats.astype({"Season": str})

All_Stats = list(Conference_Stats)

Metric_Select = st.selectbox('Metric Select',['firstDowns','fourthDownConversions','fourthDowns','fumblesLost','fumblesRecovered','games',
                                              'interceptions','interceptionTDs','interceptionYards','kickReturns','kickReturnTDs','kickReturnYards',
                                              'netPassingYards','passAttempts','passCompletions','passesIntercepted','passingTDs','penalties','penaltyYards',
                                              'possessionTime','puntReturns','puntReturnTDs','puntReturnYards','rushingAttempts','rushingTDs','rushingYards','sacks',
                                              'tacklesForLoss','thirdDownConversions','thirdDowns','totalYards','turnovers'])

Conference_Stats_Chart = alt.Chart(Conference_Stats, title = 'Total Conference Stats').mark_line(
    width=30,
    height=30,
    point = alt.OverlayMarkDef(filled=False, fill="blue")
).encode(
    alt.X('Season').scale(zero=False),
    alt.Y(Metric_Select).scale(zero=False),
    text = Metric_Select,
    tooltip=['Season', Metric_Select]
).interactive()

st.altair_chart(Conference_Stats_Chart, use_container_width= True)
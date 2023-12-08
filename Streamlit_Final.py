import pandas as pd
import streamlit as st
import numpy as np
import altair as alt


df = pd.read_csv('2022_data.csv')
df['Logo'] = 'Logos/' + df['Team'] + '.png'
df.head()

def getLogo(Logo):
    return OffsetImage(plt.imread(Logo),zoom = .35, alpha = 1)

offenses = alt.Chart(df, title = '2022 Big Ten Best Offenses').mark_image(
    width=30,
    height=30
).encode(
    alt.X('rushingYards:Q').scale(zero=False),
    alt.Y('netPassingYards').scale(zero=False),
    url='Logo',
    tooltip=['Season','Team','rushingYards','netPassingYards']
).interactive()

st.write(offenses)
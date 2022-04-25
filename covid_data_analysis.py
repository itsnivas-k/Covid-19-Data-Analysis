import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px ### for plotting the data on india map

path = 'https://raw.githubusercontent.com/itsnivas-k/covid19india/main/Book%204.csv'
df = pd.read_csv(path)
df.head(36)

india = df.groupby("State/UT")['Confirmed Cases','Active Cases','Cured','Death'].sum().reset_index()
india.head(36)
top_20 = india.sort_values(by=['Confirmed Cases'], ascending=False).head(20)

### Generate a Barplot
plt.figure(figsize=(12,10))
plot = sns.barplot(top_20['Confirmed Cases'], top_20['State/UT'])
for i,(value,name) in enumerate(zip(top_20['Confirmed Cases'],top_20['State/UT'])):
  plot.text(value,i-0.05,f'{value:,.0f}',size=10)
plt.show()

top_5 = india.sort_values(by=['Confirmed Cases'], ascending=False).head()

### Generate a Barplot
plt.figure(figsize=(15,5))
active  = sns.barplot(top_5['Active Cases'], top_5['State/UT'], color = 'red', label='Active Cases')

### Adding Texts for barplots
for i,(value,name) in enumerate(zip(top_5['Active Cases'],top_5['State/UT'])):
   active.text(value,i-0.05,f'{value:,.0f}',size=9)

plt.legend(loc=4)
plt.show()

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("https://raw.githubusercontent.com/itsnivas-k/active-cases/main/active%20cases2022.csv")

fig = go.Figure(data=go.Choropleth(
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locationmode='geojson-id',
    locations=df['state'],
    z=df['active cases'],

    autocolorscale=False,
    colorscale='Reds',
    marker_line_color='peachpuff',

    colorbar=dict(
        title={'text': "Active Cases"},

        thickness=15,
        len=0.35,
        bgcolor='rgba(255,255,255,0.6)',

        tick0=0,
        dtick=500,
        xanchor='left',
        x=0.01,
        yanchor='bottom',
        y=0.05
    )
))

fig.update_geos(
    visible=False,
    projection=dict(
        type='conic conformal',
        parallels=[12.472944444, 35.172805555556],
        rotation={'lat': 24, 'lon': 80}
    ),
    lonaxis={'range': [68, 98]},
    lataxis={'range': [6, 38]}
)
fig.update_layout(
    title=dict(
        text="Active COVID-19 Cases in India by State as of April 22, 2022",
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    height=550,
    width=550
)

fig.show()
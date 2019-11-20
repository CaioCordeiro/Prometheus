import pandas as pd
import numpy as np
import math
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def AlvoDecil(data, casasDecimais):
    bin = [0,10,20,30,40,50,60,70,80,90,100]
    df = data.groupby(pd.cut(data.SCORE, bins = bin)).mean()
    tratado = df.loc[:,['ALVO']]
    label = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    tratado.ALVO = tratado.ALVO.apply(lambda x: round(x, casasDecimais))
    fig = go.Figure()
    
    #Add bar chart
    fig.add_trace(
        go.Bar(x=label, y=tratado.ALVO, name="Bar")
    )

    #Add line chart
    fig.add_trace(
        go.Scatter(x=label, y=tratado.ALVO, name="Line")
    )

    #Add títulos
    fig.update_layout(
        title= {
            'text': "Percentual de Maus Pagadores por Décil de Score",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title = "Faixa de Score",
        yaxis_title = "Percentual de Maus Pagadores"
    )

    fig.show()

    return fig

def main():
    file = "./BASE_CREDITO.txt";
    dataframe = pd.read_csv(file, delimiter= '\t')
    AlvoDecil(dataframe, 3)

if __name__ == '__main__':
    main()
    
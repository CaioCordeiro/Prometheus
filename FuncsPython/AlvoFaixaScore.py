import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def AlvoFaixaScore(data, casasDecimais):
    bin = [0,10,20,30,40,50,60,70,80,90,100]
    df = data.groupby(pd.cut(data.SCORE, bins = bin)).mean()
    tratado = df.loc[:,['ALVO']]
    label = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    tratado.ALVO = tratado.ALVO.apply(lambda x: round(x, casasDecimais))

    # Texto da Tabela descrevendo gráfico
    desc = "A taxa de maus pagadores diminui consideravelmente à medida que a faixa de score aumenta, indicando <b>clientes mais confiáveis</b> nestas áreas."

    #fig = go.Figure()

    # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
    fig = make_subplots(
    rows=1, cols=3,
    specs= [[{"type": "table"},{"colspan": 2},None]]
    )

    # Add Table
    fig.add_trace(
    go.Table(
        header=dict(
            values=["Descrição"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[desc],
            align = "left")
    ),
    row=1, col=1
    )

    #Add bar chart
    fig.add_trace(
        go.Bar(x=label, y=tratado.ALVO, name="Bar"), row=1, col=2
    )

    #Add line chart
    fig.add_trace(
        go.Scatter(x=label, y=tratado.ALVO, name="Line"), row=1, col=2
    )

    fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
    fig.update_yaxes(title_text="Percentual de Maus Pagadores", row=1, col=2)

    #Add títulos
    fig.update_layout(
        title= {
            'text': "Percentual de Maus Pagadores por Décil de Score",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    fig.show()

    return fig

def main():
    file = "./BASE_CREDITO.txt";
    dataframe = pd.read_csv(file, delimiter= '\t')
    AlvoFaixaScore(dataframe, 3)

if __name__ == '__main__':
    main()
    
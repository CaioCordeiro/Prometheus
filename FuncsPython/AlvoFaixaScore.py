import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def AlvoFaixaScore(data, casasDecimais, flag):
    bin = [0,10,20,30,40,50,60,70,80,90,100]
    colors=["rgba(0, 33, 64,1)", "rgba(206, 21, 67,1)"]

    df = data.groupby(pd.cut(data.SCORE, bins = bin)).mean()
    df2 = data.groupby(pd.cut(data.SCORE, bins = bin)).count()
    tratado = df.loc[:,['ALVO']]
    tratado2 = df2.loc[:,['ALVO']]
    label = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    tratado.ALVO = tratado.ALVO.apply(lambda x: round(x, casasDecimais))

    flag = flag.strip().lower()

    # Texto da Tabela descrevendo gráfico
    static_desc = "A taxa de maus pagadores diminui consideravelmente à medida que a faixa de score aumenta, indicando <b>clientes mais confiáveis</b> nestas áreas."

    if flag == "no":

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
                values=[static_desc],
                align = "left")
        ),
        row=1, col=1
        )

        #Add bar chart
        fig.add_trace(
            go.Bar(x=label, y=tratado2.ALVO, customdata= tratado2.ALVO,
            hovertemplate = "Total de pessoa na faixa: %{customdata}",
            marker_color=colors[0], name="Quantidade"), row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=label, y=(tratado.ALVO*tratado2.ALVO),
            customdata= tratado.ALVO, hovertemplate = "Percentual de maus Pagadores %{customdata}",
            marker_color=colors[1], name="Percentual de Maus Pagadores"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(title_text="Contagem de Pessoas", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Percentual de Maus Pagadores por Faixa de Score",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        fig.show()

        return fig

    if flag == "yes":

        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        pre_fig = make_subplots(
        rows=1, cols=2,
        specs= [[{"colspan": 2},None]]
        )

        #Add bar chart
        pre_fig.add_trace(
            go.Bar(x=label, y=tratado2.ALVO, customdata= tratado2.ALVO, 
            hovertemplate = "Total de pessoa na faixa: %{customdata}", 
            marker_color=colors[0], name="Contagem"), row=1, col=1
        )

        #Add line chart
        pre_fig.add_trace(
            go.Scatter(x=label, y=(tratado.ALVO*tratado2.ALVO), 
            customdata= tratado.ALVO, hovertemplate = "Percentual de maus Pagadores %{customdata}",
            marker_color=colors[1], name="Percentual de Maus Pagadores"), row=1, col=1
        )

        pre_fig.update_xaxes(title_text="Faixa de Score", row=1, col=1)
        pre_fig.update_yaxes(title_text="Contagem de Pessoas", row=1, col=1)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "Percentual de Maus Pagadores por Faixa de Score",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        pre_fig.show()

        Titulo = "0"
        while(Titulo != "1" and Titulo != "2" and Titulo != "3"):
            Titulo = str(input("Tipo da Descrição [1 - Oportunidade], [2 - Alerta], [3 - Risco]: "))
        
        analise = str(input("digite a descrição desejada: "))

        if Titulo == "1":
            Titulo = "Oportunidade"
            headerColor = 'lightgreen'

        elif Titulo == "2":
            Titulo = "Alerta"
            headerColor = 'yellow'

        elif Titulo == "3":
            Titulo = "Risco"
            headerColor = 'red'

        fig = make_subplots(
        rows=1, cols=3,
        specs= [[{"type": "table"},{"colspan": 2},None]]
        )

        fig.add_trace(                   
        go.Table(
            header=dict(
                values=[["Descrição do Gráfico"],[Titulo]],
                font=dict(size=12),
                line_color='darkslategray',
                fill=dict(color=['white',headerColor]),
                align="left"
            ),
            cells=dict(
                values=[[static_desc],[analise]],
                line_color='darkslategray',
                fill=dict(color=['white',headerColor]),
                align ="left"
                )
        ),
        row=1, col=1
        )

        #Add bar chart
        fig.add_trace(
            go.Bar(x=label, y=tratado2.ALVO, customdata= tratado2.ALVO,
            hovertemplate = "Total de pessoa na faixa: %{customdata}",
            marker_color=colors[0], name="Quantidade"), row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=label, y=(tratado.ALVO*tratado2.ALVO), 
            customdata= tratado.ALVO, hovertemplate = "Percentual de maus Pagadores %{customdata}",
            marker_color=colors[1], name="Percentual de Maus Pagadores"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(title_text="Contagem de Pessoas", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Percentual de Maus Pagadores por Faixa de Score",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        fig.show()

        return fig

    else:
        raise Exception ("Flag invalida, por favor digite yes ou no")

def main():
    file = "./BASE_CREDITO.txt"
    dataframe = pd.read_csv(file, delimiter= '\t')
    AlvoFaixaScore(dataframe, 3,"yes")

if __name__ == '__main__':
    main()
    
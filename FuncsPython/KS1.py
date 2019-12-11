import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def KS1(data, flag):
    colors=["rgba(0, 33, 64,1)", "rgba(206, 21, 67,1)"]

    # Texto da Tabela descrevendo gráfico
    static_desc = "Quanto menor o KS1, melhor. O padrão é considerar a população aderente quanto o KS1 for inferior a 100%"


    flag = flag.strip().lower()

    if flag == "no":

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

        #Add bar chart Modelagem
        fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.MODELAGEM,
            hovertemplate = "Total de pessoa na faixa: %{y}",
            marker_color=colors[0], name="Distribuição % - Modelagem"), row=1, col=2
        )

        #Add bar chart Out of Time
        fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.OUT_OF_TIME,
            hovertemplate = "Total de pessoa na faixa: %{y}",
            marker_color=colors[1], name="Distribuição % - Out of Time"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(tickformat=".2%", title_text="Distribuição %", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Distribuição dos Escores",
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

                #Add bar chart Modelagem
        pre_fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.MODELAGEM,
            hovertemplate = "Total de pessoa na faixa: %{y}",
            marker_color=colors[0], name="Distribuição % - Modelagem"), row=1, col=1
        )

        #Add bar chart Out of Time
        pre_fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.OUT_OF_TIME,
            hovertemplate = "Total de pessoa na faixa: %{y}",
            marker_color=colors[1], name="Distribuição % - Out of Time"), row=1, col=1
        )

        pre_fig.update_xaxes(title_text="Faixa de Score", row=1, col=1)
        pre_fig.update_yaxes(tickformat=".2%", title_text="Distribuição %", row=1, col=1)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "Distribuição dos Escores",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        pre_fig.show()

        # Texto da Tabela descrevendo gráfico
        
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



        #Add bar chart Modelagem
        fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.MODELAGEM,
            hovertemplate = "Total de pessoa na faixa: %{y}",
            marker_color=colors[0], name="Distribuição % - Modelagem"), row=1, col=2
        )

        #Add bar chart Out of Time
        fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.OUT_OF_TIME,
            hovertemplate = "Total de pessoa na faixa: %{y}",
            marker_color=colors[1], name="Distribuição % - Out of Time"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(tickformat=".2%", title_text="Distribuição %", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Distribuição dos Escores",
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
    lst = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    lst2 = [0.04,0.06,0.07,0.07,0.08,0.09,0.10,0.11,0.15,0.24]
    lst3 = [0.04,0.06,0.06,0.07,0.08,0.09,0.10,0.11,0.15,0.25]
    dataframe = pd.DataFrame(list(zip(lst,lst2,lst3)),columns=['FAIXA_SCORE','MODELAGEM','OUT_OF_TIME'])
    KS1(dataframe, "yes")

if __name__ == '__main__':
    main()
    
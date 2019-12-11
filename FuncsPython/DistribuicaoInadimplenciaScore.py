import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def distInadimplenciaScore(data, flag):
    colors=["rgba(0, 33, 64,1)", "rgba(206, 21, 67,1)"]

     # Texto da Tabela descrevendo gráfico
    desc = "Podemos observar nas barras em azul a representatividade de cada faixa de score. Nas bolas em vermelho, obervamos a taxa de inadimplência dentro se cada faixa de score."

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
                values=[desc],
                align = "left")
        ),
        row=1, col=1
        )

        #Add bar chart
        fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.DISTRIBUICAO,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['DISTRIBUICAO']], index = data.DISTRIBUICAO),
            hovertemplate = "Distribuição da faixa: %{customdata}",
            marker_color=colors[0], name="Distribuição"), row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=data.FAIXA_SCORE, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência na faixa: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(tickformat=".2%",title_text="Percentual", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Distribuição e Taxa de Inadimplência por Faixa de Score",
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
            go.Bar(x=data.FAIXA_SCORE, y=data.DISTRIBUICAO,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['DISTRIBUICAO']], index = data.DISTRIBUICAO),
            hovertemplate = "Distribuição da faixa: %{customdata}",
            marker_color=colors[0], name="Distribuição"), row=1, col=1
        )

        #Add line chart
        pre_fig.add_trace(
            go.Scatter(x=data.FAIXA_SCORE, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência na faixa: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), row=1, col=1
        )

        pre_fig.update_xaxes(title_text="Faixa de Score", row=1, col=1)
        pre_fig.update_yaxes(tickformat=".2%",title_text="Percentual", row=1, col=1)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "Distribuição e Taxa de Inadimplência por Faixa de Score",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        pre_fig.show()


        Titulo = str(input("Tipo da Descrição: "))
        analise = str(input("digite a descrição desejada: "))

        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        fig = make_subplots(
        rows=1, cols=3,
        specs= [[{"type": "table"},{"colspan": 2},None]]
        )

        # Add Table
        fig.add_trace(
        go.Table(
            header=dict(
                values=[Titulo],
                font=dict(size=10),
                align="left"
            ),
            cells=dict(
                values=[[desc,analise]],
                align = "left")
        ),
        row=1, col=1
        )

                #Add bar chart
        fig.add_trace(
            go.Bar(x=data.FAIXA_SCORE, y=data.DISTRIBUICAO,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['DISTRIBUICAO']], index = data.DISTRIBUICAO),
            hovertemplate = "Distribuição da faixa: %{customdata}",
            marker_color=colors[0], name="Distribuição"), row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=data.FAIXA_SCORE, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência na faixa: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(tickformat=".2%",title_text="Percentual", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Distribuição e Taxa de Inadimplência por Faixa de Score",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        fig.show()

        return fig

    else:
        raise "Flag invalida, por favor digite yes ou no"

def main():
    lst = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    lst2 = [0.02,0.06,0.07,0.08,0.08,0.09,0.10,0.12,0.15,0.23]
    lst3 = [0.544,0.343,0.223,0.157,0.11,0.08,0.053,0.034,0.017,0.005]
    dataframe = pd.DataFrame(list(zip(lst,lst2,lst3)),columns=['FAIXA_SCORE','DISTRIBUICAO','TAXA_INADIMPLENCIA'])
    distInadimplenciaScore(dataframe,"yes")

if __name__ == '__main__':
    main()
    
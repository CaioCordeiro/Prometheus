import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def distInadimplenciaScore(data, flag):
    colors=["rgba(0, 33, 64,1)", "rgba(206, 21, 67,1)"]

     # Texto da Tabela descrevendo gráfico
    static_desc = "No gráfico de distribuição e taxa de inadimplência por safra observamos nas barras em azul a representatividade de cada mês utilizado na análise. A taxa em vermelho significa a inadimplência referente a cada mês."

    flag = flag.strip().lower()

    if flag == "no":
        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        fig = make_subplots(
        rows=1, cols=3,
        specs= [[{"type": "table"},{"secondary_y": True,"colspan": 2},None]]
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
            go.Bar(x=data.MES_ANO, y=data.SAFRA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['SAFRA']], index = data.SAFRA),
            marker_color=colors[0], name="Safra"), secondary_y = False, row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=data.MES_ANO, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência no período: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), secondary_y = True, row=1, col=2
        )

        fig.update_xaxes(title_text="Período", row=1, col=2)

        # Double Y Axis
        fig.update_yaxes(tickformat=".2%",title_text="Safra", secondary_y = False, row=1, col=2)
        fig.update_yaxes(tickformat=".2%",title_text="Taxa de Inadimplência", secondary_y = True, row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Distribuição e Taxa de Inadimplência por Safra",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        fig.show()

        return fig

    if flag == "yes":

        pre_fig = make_subplots(
        rows=1, cols=3,
        specs= [[{"type": "table"},{"secondary_y": True,"colspan": 2},None]]
        )

        # Add Table
        pre_fig.add_trace(
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
        pre_fig.add_trace(
            go.Bar(x=data.MES_ANO, y=data.SAFRA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['SAFRA']], index = data.SAFRA),
            marker_color=colors[0], name="Safra"), secondary_y = False, row=1, col=2
        )

        #Add line chart
        pre_fig.add_trace(
            go.Scatter(x=data.MES_ANO, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência no período: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), secondary_y = True, row=1, col=2
        )

        pre_fig.update_xaxes(title_text="Período", row=1, col=2)

        # Double Y Axis
        pre_fig.update_yaxes(tickformat=".2%",title_text="Safra", secondary_y = False, row=1, col=2)
        pre_fig.update_yaxes(tickformat=".2%",title_text="Taxa de Inadimplência", secondary_y = True, row=1, col=2)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "Distribuição e Taxa de Inadimplência por Safra",
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
        specs= [[{"type": "table"},{"secondary_y": True,"colspan": 2},None]]
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

        fig = make_subplots(
        rows=1, cols=3,
        specs= [[{"type": "table"},{"secondary_y": True,"colspan": 2},None]]
        )

        #Add bar chart
        fig.add_trace(
            go.Bar(x=data.MES_ANO, y=data.SAFRA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['SAFRA']], index = data.SAFRA),
            marker_color=colors[0], name="Safra"), secondary_y = False, row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=data.MES_ANO, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência no período: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), secondary_y = True, row=1, col=2
        )

        fig.update_xaxes(title_text="Período", row=1, col=2)

        # Double Y Axis
        fig.update_yaxes(tickformat=".2%",title_text="Safra", secondary_y = False, row=1, col=2)
        fig.update_yaxes(tickformat=".2%",title_text="Taxa de Inadimplência", secondary_y = True, row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Distribuição e Taxa de Inadimplência por Safra",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        fig.show()

        return fig

    else:
        raise Exception("Flag invalida, por favor digite yes ou no")

def main():
    lst = ["jan/18","fev/18","mar/18","abr/18","mai/18","jun/18","jul/18","ago/18","set/18","out/18","nov/18","dez/18","jan/19","fev/19","mar/19"]
    lst2 = [0.06,0.07,0.07,0.07,0.07,0.07,0.06,0.07,0.07,0.07,0.07,0.07,0.06,0.07,0.07]
    lst3 = [0.15,0.15,0.14,0.14,0.12,0.13,0.13,0.13,0.14,0.15,0.16,0.17,0.17,0.13,0.16]
    dataframe = pd.DataFrame(list(zip(lst,lst2,lst3)),columns=['MES_ANO','SAFRA','TAXA_INADIMPLENCIA'])
    distInadimplenciaScore(dataframe,"yes")

if __name__ == '__main__':
    main()
    
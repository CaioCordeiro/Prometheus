import pandas as pd
import numpy as np
import math
#import plotly.io as pio
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def ComparativoRenda(data, flag):
    colors=["rgba(0, 33, 64,0.5)", "rgba(0, 33, 64,1)","rgba(206, 21, 67,0.5)", "rgba(206, 21, 67,1)"]
    
    flag = flag.strip().lower()

    if flag == "no":

        # Texto da Tabela descrevendo gráfico
        desc = "Lorem Ipsum"
 
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
                font=dict(size=10),
                align = "left")
        ),
        row=1, col=1
        )

        #Add Barras
        fig.add_trace(
             go.Bar(y=data.PERCENT,
               x= data.COMPARATIVO_RENDA,
               name='Percentual da População',
               customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['PERCENT']], index = data.PERCENT),
               text = np.repeat("Percentual de pessoas com Renda Inferior a média da Região: " + "{0:.2f}%".format(data.loc[data.COMPARATIVO_RENDA<0].PERCENT.sum() * 100) + "<br>" + "Percentual de pessoas com Renda Superior a média da Região: " + "{0:.2f}%".format(data.loc[data.COMPARATIVO_RENDA>0].PERCENT.sum() * 100),9),
               hovertemplate= "Valor do eixo: %{y}<br>Média: %{customdata}<br>%{text}",
               marker_color=colors[1]
               ), row=1, col=2
        )

        fig.update_xaxes(title_text="Comparativo Renda", row=1, col=2)
        fig.update_yaxes(tickformat=".2%",title_text="Percentual da População", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Comparativo Renda",
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

        #Add Barras
        pre_fig.add_trace(
             go.Bar(y=data.PERCENT,
               x= data.COMPARATIVO_RENDA,
               name='Percentual da População',
               customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['PERCENT']], index = data.PERCENT),
               text = np.repeat("Percentual de pessoas com Renda Inferior a média da Região: " + "{0:.2f}%".format(data.loc[data.COMPARATIVO_RENDA<0].PERCENT.sum() * 100) + "<br>" + "Percentual de pessoas com Renda Superior a média da Região: " + "{0:.2f}%".format(data.loc[data.COMPARATIVO_RENDA>0].PERCENT.sum() * 100),9),
               hovertemplate= "Valor do eixo: %{y}<br>Média: %{customdata}<br>%{text}",
               marker_color=colors[1]
               ), row=1, col=1
        )

        pre_fig.update_xaxes(title_text="Comparativo Renda", row=1, col=1)
        pre_fig.update_yaxes(tickformat=".2%",title_text="Percentual da População", row=1, col=1)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "Comparativo Renda",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        pre_fig.show()

        Titulo = str(input("Tipo da Descrição: "))
        desc = str(input("digite a descrição desejada: "))
 
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
                values=[desc],
                font=dict(size=10),
                align = "left")
        ),
        row=1, col=1
        )

        #Add Barras
        fig.add_trace(
             go.Bar(y=data.PERCENT,
               x= data.COMPARATIVO_RENDA,
               name='Percentual da População',
               customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['PERCENT']], index = data.PERCENT),
               text = np.repeat("Percentual de pessoas com Renda Inferior a média da Região: " + "{0:.2f}%".format(data.loc[data.COMPARATIVO_RENDA<0].PERCENT.sum() * 100) + "<br>" + "Percentual de pessoas com Renda Superior a média da Região: " + "{0:.2f}%".format(data.loc[data.COMPARATIVO_RENDA>0].PERCENT.sum() * 100),9),
               hovertemplate= "Valor do eixo: %{y}<br>Média: %{customdata}<br>%{text}",
               marker_color=colors[1]
               ), row=1, col=2
        )

        fig.update_xaxes(title_text="Comparativo Renda", row=1, col=2)
        fig.update_yaxes(tickformat=".2%",title_text="Percentual da População", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Comparativo Renda",
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
    lis = [-4,-3,-2,-1,0,1,2,3,4]
    lis2 = [0,0,0.01,0.03,0.43,0.16,0.07,0.01,0]
    dataframe = pd.DataFrame(list(zip(lis,lis2)),columns=['COMPARATIVO_RENDA','PERCENT'])
    ComparativoRenda(dataframe, "yes")

if __name__ == '__main__':
    main()
    
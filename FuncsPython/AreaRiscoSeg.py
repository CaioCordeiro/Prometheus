import pandas as pd
import numpy as np
import math
#import plotly.io as pio
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def PiramideEtaria(data, flag):
    colors=["rgba(0, 33, 64,0.5)", "rgba(0, 33, 64,1)","rgba(206, 21, 67,0.5)", "rgba(206, 21, 67,1)"]

    flag = flag.strip().lower()

    if flag == "no":

        # Texto da Tabela descrevendo gráfico
        desc = "Lorem Ipsum"
        
        
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
                font=dict(size=10),
                align = "left")
        ),
        row=1, col=1
        )

        #Add Segurança
        fig.add_trace(
           go.Bar(
               y= data.CLASSE_SOCIAL,
               x= -1* data.SEG,
               orientation='h',
               name='Áreas de Segurança',
               customdata= pd.Series(["{0:.1f}%".format(val * 100) for val in data['SEG']], index = data.SEG),
               hovertemplate= "Percentual de Área Segurança da Classe: %{customdata}",
               marker_color=colors[1]
               ), row=1, col=2
        )

        #Add Risco
        fig.add_trace(
           go.Bar(
               y= data.CLASSE_SOCIAL,
               x= data.RISCO,
               orientation='h',
               name='Áreas de Risco',
               customdata= pd.Series(["{0:.1f}%".format(val * 100) for val in data['RISCO']], index = data.RISCO),
               hovertemplate= "Percentual de Área Risco da Classe: %{customdata}",
               marker_color=colors[3]
               ), row=1, col=2
        )


        xaxisTickPre = list(np.arange(-1,+1,0.1))

        xaxisTick = []

        for num in xaxisTickPre:
            xaxisTick.append(round(num/0.1,3)*0.1)

        xaxisTickText = [abs(i) for i in xaxisTick]

        fig.update_xaxes(title_text="Percentual de Segurança x Percentual de Risco", row=1, col=2)
        fig.update_xaxes(
            tickvals= xaxisTick,
            ticktext= ["{0:.2f}%".format(val * 100) for val in xaxisTickText],
            row=1, col=2
        )
        fig.update_yaxes(title_text="Classe Social", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "ÁREA DE RISCO X SEGURANÇA",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            barmode = 'overlay'
        )

        fig.show()

        return fig

    if flag == "yes":

        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        pre_fig = make_subplots(
        rows=1, cols=2,
        specs= [[{"colspan": 2},None]]
        )

        #Add Segurança
        pre_fig.add_trace(
           go.Bar(
               y= data.CLASSE_SOCIAL,
               x= -1* data.SEG,
               orientation='h',
               name='Áreas de Segurança',
               customdata= pd.Series(["{0:.1f}%".format(val * 100) for val in data['SEG']], index = data.SEG),
               hovertemplate= "Percentual de Área Segurança da Classe: %{customdata}",
               marker_color=colors[1]
               ), row=1, col=1
        )

        #Add Risco
        pre_fig.add_trace(
           go.Bar(
               y= data.CLASSE_SOCIAL,
               x= data.RISCO,
               orientation='h',
               name='Áreas de Risco',
               customdata= pd.Series(["{0:.1f}%".format(val * 100) for val in data['RISCO']], index = data.RISCO),
               hovertemplate= "Percentual de Área Risco da Classe: %{customdata}",
               marker_color=colors[3]
               ), row=1, col=1
        )


        xaxisTickPre = list(np.arange(-1,+1,0.1))

        xaxisTick = []

        for num in xaxisTickPre:
            xaxisTick.append(round(num/0.1,3)*0.1)

        xaxisTickText = [abs(i) for i in xaxisTick]

        pre_fig.update_xaxes(title_text="Percentual de Segurança x Percentual de Risco", row=1, col=1)
        pre_fig.update_xaxes(
            tickvals= xaxisTick,
            ticktext= ["{0:.2f}%".format(val * 100) for val in xaxisTickText],
            row=1, col=1
        )
        pre_fig.update_yaxes(title_text="Classe Social", row=1, col=1)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "ÁREA DE RISCO X SEGURANÇA",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            barmode = 'overlay'
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
                align = "left")
        ),
        row=1, col=1
        )

        #Add Segurança
        fig.add_trace(
           go.Bar(
               y= data.CLASSE_SOCIAL,
               x= -1* data.SEG,
               orientation='h',
               name='Áreas de Segurança',
               customdata= pd.Series(["{0:.1f}%".format(val * 100) for val in data['SEG']], index = data.SEG),
               hovertemplate= "Percentual de Área Segurança da Classe: %{customdata}",
               marker_color=colors[1]
               ), row=1, col=2
        )

        #Add Risco
        fig.add_trace(
           go.Bar(
               y= data.CLASSE_SOCIAL,
               x= data.RISCO,
               orientation='h',
               name='Áreas de Risco',
               customdata= pd.Series(["{0:.1f}%".format(val * 100) for val in data['RISCO']], index = data.RISCO),
               hovertemplate= "Percentual de Área Risco da Classe: %{customdata}",
               marker_color=colors[3]
               ), row=1, col=2
        )


        xaxisTickPre = list(np.arange(-1,+1,0.1))

        xaxisTick = []

        for num in xaxisTickPre:
            xaxisTick.append(round(num/0.1,3)*0.1)

        xaxisTickText = [abs(i) for i in xaxisTick]

        fig.update_xaxes(title_text="Percentual de Segurança x Percentual de Risco", row=1, col=2)
        fig.update_xaxes(
            tickvals= xaxisTick,
            ticktext= ["{0:.2f}%".format(val * 100) for val in xaxisTickText],
            row=1, col=2
        )
        fig.update_yaxes(title_text="Classe Social", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "ÁREA DE RISCO X SEGURANÇA",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            barmode = 'overlay'
        )

        fig.show()

        return fig
    
    else:
        raise "Flag invalida, por favor digite yes ou no"

def main():
    lis = ["A","B","C","D","E"]
    lis2 = [0.004,0.018,0.149,0.258,0.571]
    lis3 = [0.003,0.014,0.132,0.272,0.580]
    dataframe = pd.DataFrame(list(zip(lis,lis2,lis3)),columns=['CLASSE_SOCIAL','SEG','RISCO'])
    html = PiramideEtaria(dataframe, "no")

if __name__ == '__main__':
    main()
    
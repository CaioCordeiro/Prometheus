import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def PiramideEtaria(data, flag):
    bin = [10,20,30,40,50,float("inf")]


    df = data.groupby([data.SEXO,pd.cut(data.IDADE, bins = bin)]).count()
    tratado = df.loc[:,['IDADE']]
    tratado.IDADE = tratado.IDADE / tratado.IDADE.groupby(level=0).sum()
    label = ["10-20","20-30","30-40","40-50",">50"]

    #print(tratado.groupby('SEXO').get_group("F"))
    y = list(range(0, 100, 10))

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
                align = "left")
        ),
        row=1, col=1
        )

        #Add chart
        fig.add_trace(
           go.Bar(y=y,
               x= tratado.groupby('SEXO').get_group("M").IDADE,
               orientation='h',
               name='Masculino',
               hoverinfo='x',
               marker=dict(color='powderblue')
               ), row=1, col=2
        )

        #Add line chart
        fig.add_trace(
             go.Bar(y=y,
               x= -1 * tratado.groupby('SEXO').get_group("F").IDADE,
               orientation='h',
               name='Feminino',
               text= -1 * tratado.groupby('SEXO').get_group("F").IDADE,
               hoverinfo='text',
               marker=dict(color='seagreen')
               ), row=1, col=2
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

    if flag == "yes":

        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        pre_fig = make_subplots(
        rows=1, cols=2,
        specs= [[{"colspan": 2},None]]
        )

        #Add bar chart
        pre_fig.add_trace(
            go.Bar(x=label, y=tratado2.ALVO, customdata= tratado2.ALVO, hovertemplate = "Total de pessoa na faixa: %{customdata}", name=""), row=1, col=1
        )Contagem

        #Add line chart
        pre_fig.add_trace(
            go.Scatter(x=label, y=(tratado.ALVO*tratado2.ALVO), customdata= tratado.ALVO, hovertemplate = "Percentual de maus Pagadores %{customdata}", name="Percentual de Maus Pagadores"), row=1, col=1
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
            go.Bar(x=label, y=tratado2.ALVO, customdata= tratado2.ALVO, hovertemplate = "Total de pessoa na faixa: %{customdata}", name="Pessoas na Faixa"), row=1, col=2
        )

        #Add line chart
        fig.add_trace(
            go.Scatter(x=label, y=(tratado.ALVO*tratado2.ALVO), customdata= tratado.ALVO, hovertemplate = "Percentual de maus Pagadores %{customdata}", name="Percentual de Maus Pagadores"), row=1, col=2
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

def main():
    file = "./BASE_CREDITO.txt";
    dataframe = pd.read_csv(file, delimiter= '\t')
    PiramideEtaria(dataframe, "no")

if __name__ == '__main__':
    main()
    
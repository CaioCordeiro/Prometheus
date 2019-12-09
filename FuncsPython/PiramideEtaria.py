import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def PiramideEtaria(data, flag):
    colors=["rgba(0, 33, 64,0.5)", "rgba(0, 33, 64,1)","rgba(206, 21, 67,0.5)", "rgba(206, 21, 67,1)"]
    bin = [10,20,30,40,50,float("inf")]


    df = data.groupby([data.SEXO,pd.cut(data.IDADE, bins = bin)]).count()
    tratado = df.loc[:,['IDADE']]
    totalPessoas = tratado.IDADE.groupby(level=0).sum()
    tratado["IDADEPERCENTUAL"] = tratado.IDADE / tratado.IDADE.groupby(level=0).sum()
    label = ["10-20","20-30","30-40","40-50",">50"]

    #print(tratado.groupby('SEXO').get_group("F"))

    flag = flag.strip().lower()

    if flag == "no":

        # Texto da Tabela descrevendo gráfico
        desc = "Pirâmide etária ou pirâmide demográfica, consiste num histograma que mostra a distribuição de diferentes grupos etários numa população, em que normalmente se cria a forma de uma pirâmide cuja altura é proporcional à quantidade que representa a estrutura da população por sexo e idade, designado de cortes."
        
        
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

        #Add Masculino Total
        fig.add_trace(
           go.Bar(y=label,
               x= np.repeat(totalPessoas.get("M"),5),
               orientation='h',
               name='Masculino Total',
               customdata= np.repeat(totalPessoas.get("M"),5),
               text=tratado.groupby('SEXO').get_group("M").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[0]
               ), row=1, col=2
        )

        #Add Masculino Total por Faixa Etaria
        fig.add_trace(
           go.Bar(y=label,
               x= tratado.groupby('SEXO').get_group("M").IDADE,
               orientation='h',
               name='Masculino por Faixa',
               customdata= np.repeat(totalPessoas.get("M"),5),
               text=tratado.groupby('SEXO').get_group("M").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[1]
               ), row=1, col=2
        )

        #Add Feminino Total
        fig.add_trace(
           go.Bar(y=label,
               x= np.repeat(-1*totalPessoas.get("F"),5),
               orientation='h',
               name='Feminino Total',
               customdata= np.repeat(totalPessoas.get("F"),5),
               text=tratado.groupby('SEXO').get_group("F").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[2]
               ), row=1, col=2
        )

        #Add Feminino Total por Faixa Etaria
        fig.add_trace(
             go.Bar(y=label,
               x= -1 * tratado.groupby('SEXO').get_group("F").IDADE,
               orientation='h',
               name='Feminino por Faixa',
               customdata= np.repeat(totalPessoas.get("F"),5),
               text=tratado.groupby('SEXO').get_group("F").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[3]
               ), row=1, col=2
        )

        xaxisTickPre = list(range(-1*totalPessoas.get("F")-100,totalPessoas.get("M")+100,50))

        xaxisTick = []

        for num in xaxisTickPre:
            xaxisTick.append(round(num/100)*100)

        xaxisTickText = [abs(i) for i in xaxisTick] 

        fig.update_xaxes(title_text="Contagem de Pessoas", row=1, col=2)
        fig.update_xaxes(
            tickvals= xaxisTick,
            ticktext= xaxisTickText,
            row=1, col=2
        )
        fig.update_yaxes(title_text="Faixa Etária", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Contagem de Pessoas por Faixa Etária e Sexo",
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

         #Add Masculino Total
        pre_fig.add_trace(
           go.Bar(y=label,
               x= np.repeat(totalPessoas.get("M"),5),
               orientation='h',
               name='Masculino Total',
               customdata= np.repeat(totalPessoas.get("M"),5),
               text=tratado.groupby('SEXO').get_group("M").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[0]
               ), row=1, col=1
        )

        #Add Masculino Total por Faixa Etaria
        pre_fig.add_trace(
           go.Bar(y=label,
               x= tratado.groupby('SEXO').get_group("M").IDADE,
               orientation='h',
               name='Masculino por Faixa',
               customdata= np.repeat(totalPessoas.get("M"),5),
               text=tratado.groupby('SEXO').get_group("M").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[1]
               ), row=1, col=1
        )

        #Add Feminino Total
        pre_fig.add_trace(
           go.Bar(y=label,
               x= np.repeat(-1*totalPessoas.get("F"),5),
               orientation='h',
               name='Feminino Total',
               customdata= np.repeat(totalPessoas.get("F"),5),
               text=tratado.groupby('SEXO').get_group("F").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[2]
               ), row=1, col=1
        )

        #Add Feminino Total por Faixa Etaria
        pre_fig.add_trace(
             go.Bar(y=label,
               x= -1 * tratado.groupby('SEXO').get_group("F").IDADE,
               orientation='h',
               name='Feminino por Faixa',
               customdata= np.repeat(totalPessoas.get("F"),5),
               text=tratado.groupby('SEXO').get_group("F").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[3]
               ), row=1, col=1
        )

        xaxisTickPre = list(range(-1*totalPessoas.get("F")-100,totalPessoas.get("M")+100,50))

        xaxisTick = []

        for num in xaxisTickPre:
            xaxisTick.append(round(num/100)*100)

        xaxisTickText = [abs(i) for i in xaxisTick] 

        pre_fig.update_xaxes(title_text="Contagem de Pessoas", row=1, col=2)
        pre_fig.update_xaxes(
            tickvals= xaxisTick,
            ticktext= xaxisTickText,
            row=1, col=2
        )
        pre_fig.update_yaxes(title_text="Faixa Etária", row=1, col=2)

        #Add títulos
        pre_fig.update_layout(
            title= {
                'text': "Contagem de Pessoas por Faixa Etária e Sexo",
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

        #Add Masculino Total
        fig.add_trace(
           go.Bar(y=label,
               x= np.repeat(totalPessoas.get("M"),5),
               orientation='h',
               name='Masculino Total',
               customdata= np.repeat(totalPessoas.get("M"),5),
               text=tratado.groupby('SEXO').get_group("M").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[0]
               ), row=1, col=2
        )

        #Add Masculino Total por Faixa Etaria
        fig.add_trace(
           go.Bar(y=label,
               x= tratado.groupby('SEXO').get_group("M").IDADE,
               orientation='h',
               name='Masculino por Faixa',
               customdata= np.repeat(totalPessoas.get("M"),5),
               text=tratado.groupby('SEXO').get_group("M").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[1]
               ), row=1, col=2
        )

        #Add Feminino Total
        fig.add_trace(
           go.Bar(y=label,
               x= np.repeat(-1*totalPessoas.get("F"),5),
               orientation='h',
               name='Feminino Total',
               customdata= np.repeat(totalPessoas.get("F"),5),
               text=tratado.groupby('SEXO').get_group("F").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[2]
               ), row=1, col=2
        )

        #Add Feminino Total por Faixa Etaria
        fig.add_trace(
             go.Bar(y=label,
               x= -1 * tratado.groupby('SEXO').get_group("F").IDADE,
               orientation='h',
               name='Feminino por Faixa',
               customdata= np.repeat(totalPessoas.get("F"),5),
               text=tratado.groupby('SEXO').get_group("F").IDADE,
               hovertemplate= "Total de pessoas do sexo: %{customdata}<br> Total de pessoas do sexo na faixa: %{text}",
               marker_color=colors[3]
               ), row=1, col=2
        )

        xaxisTickPre = list(range(-1*totalPessoas.get("F")-100,totalPessoas.get("M")+100,50))

        xaxisTick = []

        for num in xaxisTickPre:
            xaxisTick.append(round(num/100)*100)

        xaxisTickText = [abs(i) for i in xaxisTick] 

        fig.update_xaxes(title_text="Contagem de Pessoas", row=1, col=2)
        fig.update_xaxes(
            tickvals= xaxisTick,
            ticktext= xaxisTickText,
            row=1, col=2
        )
        fig.update_yaxes(title_text="Faixa Etária", row=1, col=2)

        #Add títulos
        fig.update_layout(
            title= {
                'text': "Contagem de Pessoas por Faixa Etária e Sexo",
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
    file = "./BASE_CREDITO.txt"
    dataframe = pd.read_csv(file, delimiter= '\t')
    PiramideEtaria(dataframe, "yes")

if __name__ == '__main__':
    main()
    
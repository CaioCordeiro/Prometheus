import pandas as pd
import numpy as np
import math
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def Ks2(data,flag):
    # Bin que vai permitir agrupar os valores por score
    bin = [0,10,20,30,40,50,60,70,80,90,100]

    #Contar o total de ocorrências de bons e mals pagadores
    dfTotal = data.ALVO.value_counts().to_frame()
    dfTotal = dfTotal.rename(index={0: "Bom", 1: "Mal"})
    totais = dfTotal.T #totais.at['ALVO','Bom'] e totais.at['ALVO','Mal']
    
    #Contando por percentual de decil
    df = data.groupby(pd.cut(data.SCORE, bins = bin))['ALVO'].value_counts()

    # Desempilhando o Dataframe
    df = df.unstack()

    # Calculando o percentual do decil comparado ao valor total
    df["PercentualBom"] = (df[0] / totais.at['ALVO','Bom'])
    df["PercentualMal"] = (df[1] / totais.at['ALVO','Mal'])

    # Calculando o Cumulativo
    df["PercentualBomAcc"] = df['PercentualBom'].rolling(min_periods=1,window=10).sum()
    df["PercentualMalAcc"] = df['PercentualMal'].rolling(min_periods=1,window=10).sum()

    # Calculando o ks2 por decil
    df['KS2'] = abs(df["PercentualBomAcc"] - df["PercentualMalAcc"])
    
    # Label
    label = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]


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
        
        # Add linha de Bom
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualBomAcc, name="Bom")
        )

        # Add linha de Mal
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualMalAcc, name="Mal"), row=1, col=2
        )

        # Add linha de KS2
        fig.add_trace(
            go.Scatter(x=label, y=df.KS2, name="KS2"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(title_text="% População (AC)", row=1, col=2)
        fig.update_yaxes(tickformat=".3%", row=1, col=2)

        #Add Formatação do Gráfico
        fig.update_layout(
            title= {
                'text': "KS2",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
        )

        fig.show()

        return fig
    
    else:
                

        pre_fig= make_subplots(
        rows=1, cols=2,
        specs= [[{"colspan": 2},None]]
        )
        
        # Add linha de Bom
        pre_fig.add_trace(
            go.Scatter(x=label, y=df.PercentualBomAcc, name="Bom")
        )

        # Add linha de Mal
        pre_fig.add_trace(
            go.Scatter(x=label, y=df.PercentualMalAcc, name="Mal"), row=1, col=1
        )

        # Add linha de KS2
        pre_fig.add_trace(
            go.Scatter(x=label, y=df.KS2, name="KS2"), row=1, col=1
        )

        pre_fig.update_xaxes(title_text="Faixa de Score", row=1, col=1)
        pre_fig.update_yaxes(title_text="% População (AC)", row=1, col=1)
        pre_fig.update_yaxes(tickformat=".3%", row=1, col=1)

        #Add Formatação do Gráfico
        pre_fig.update_layout(
            title= {
                'text': "KS2",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
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
        
        # Add linha de Bom
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualBomAcc, name="Bom")
        )

        # Add linha de Mal
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualMalAcc, name="Mal"), row=1, col=2
        )

        # Add linha de KS2
        fig.add_trace(
            go.Scatter(x=label, y=df.KS2, name="KS2"), row=1, col=2
        )

        fig.update_xaxes(title_text="Faixa de Score", row=1, col=2)
        fig.update_yaxes(title_text="% População (AC)", row=1, col=2)
        fig.update_yaxes(tickformat=".3%", row=1, col=2)

        #Add Formatação do Gráfico
        fig.update_layout(
            title= {
                'text': "KS2",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
        )

        fig.show()

        return fig
        

def main():
    file = "./BASE_CREDITO.txt";
    dataframe = pd.read_csv(file, delimiter= '\t')
    Ks2(dataframe,"yes")

if __name__ == '__main__':
    main()
    
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

def AreaRiscoSeg(data, flag):
    colors=["rgba(0, 33, 64,0.5)", "rgba(0, 33, 64,1)","rgba(206, 21, 67,0.5)", "rgba(206, 21, 67,1)"]

    flag = flag.strip().lower()

    static_desc = """No gráfico podemos observar a frequência de indivíduos em áreas de risco (em vermelho) 
        e área de segurança (em azul) em cada classe social."""

    if flag == "no":

        # Texto da Tabela descrevendo gráfico
        static_desc = "No gráfico podemos observar a frequência de indivíduos em áreas de risco (em vermelho) e área de segurança (em azul) em cada classe social."
        
        
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
        raise Exception ("Flag invalida, por favor digite yes ou no")

def ComparativoRenda(data, flag):
    colors=["rgba(0, 33, 64,0.5)", "rgba(0, 33, 64,1)","rgba(206, 21, 67,0.5)", "rgba(206, 21, 67,1)"]
    
    flag = flag.strip().lower()

    static_desc = "Lorem Ipsum"

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
        raise Exception ("Flag invalida, por favor digite yes ou no")

def CurvaRoc(data,flag):
    # Cores pro gráfico
    colors = ["rgb(0, 33, 64)", "rgb(206, 21, 67)", "rgb(212, 175, 55)"]

    # Texto da Tabela descrevendo gráfico
    static_desc = """A curva ROC mostra o quão bom o modelo criado pode distinguir entre duas coisas (já que é utilizado para classificação). Essas duas coisas podem ser 0 ou 1, ou positivo e negativo. Os melhores modelos conseguem distinguir com precisão o binômio"""

    # Calcular Area Under the Curve
    auc = np.trapz(data.TPR,data.FPR)

    print(auc)

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
        
        # Add linha de Curva Roc
        fig.add_trace(
            go.Scatter(x=data.FPR, y=data.TPR, name=("Curva ROC, AUC = "+str(round(-1*auc,2))), marker_color=colors[0]), row=1, col=2
        )

        fig.update_xaxes(title_text="1-Especificidade", row=1, col=2)
        fig.update_yaxes(title_text="Sensibilidade", row=1, col=2)

        #Add Formatação do Gráfico
        fig.update_layout(
            title= {
                'text': "Performance - Roc",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            showlegend = True
        )

        fig.show()

        return fig
    
    elif flag == "yes":
                

        pre_fig= make_subplots(
        rows=1, cols=2,
        specs= [[{"colspan": 2},None]]
        )
        
       # Add linha de Curva Roc
        pre_fig.add_trace(
            go.Scatter(x=data.FPR, y=data.TPR, name=("Curva ROC, AUC = "+str(round(-1*auc,2))), marker_color=colors[0]),
            row=1, col=1
        )

        pre_fig.update_xaxes(title_text="1-Especificidade", row=1, col=1)
        pre_fig.update_yaxes(title_text="Sensibilidade", row=1, col=1)

        #Add Formatação do Gráfico
        pre_fig.update_layout(
            title= {
                'text': "Performance - Roc",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            showlegend = True
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
    
        # Add linha de Curva Roc
        fig.add_trace(
            go.Scatter(x=data.FPR, y=data.TPR, name=("Curva ROC, AUC = "+str(round(-1*auc,2))), marker_color=colors[0]), row=1, col=2
        )

        fig.update_xaxes(title_text="1-Especificidade", row=1, col=2)
        fig.update_yaxes(title_text="Sensibilidade", row=1, col=2)

        #Add Formatação do Gráfico
        fig.update_layout(
            title= {
                'text': "Performance - Roc",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            showlegend = True
        )

        fig.show()

        return fig
    
    else:
        raise Exception(" Flag invalida, por favor digite 'YES' ou 'NO' ")
        
def distInadimplenciaSafra(data, flag):
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

        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        pre_fig = make_subplots(
        rows=1, cols=2,
        specs= [[{"secondary_y": True,"colspan": 2},None]]
        )

                #Add bar chart
        pre_fig.add_trace(
            go.Bar(x=data.MES_ANO, y=data.SAFRA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['SAFRA']], index = data.SAFRA),
            marker_color=colors[0], name="Safra"), secondary_y = False, row=1, col=1
        )

        #Add line chart
        pre_fig.add_trace(
            go.Scatter(x=data.MES_ANO, y=data.TAXA_INADIMPLENCIA,
            customdata= pd.Series(["{0:.2f}%".format(val * 100) for val in data['TAXA_INADIMPLENCIA']], index = data.TAXA_INADIMPLENCIA),
            hovertemplate = "Taxa de Inadimplência no período: %{customdata}",
            marker_color=colors[1], name="Taxa de Inadimplência"), secondary_y = True, row=1, col=1
        )

        pre_fig.update_xaxes(title_text="Período", row=1, col=1)

        # Double Y Axis
        pre_fig.update_yaxes(tickformat=".2%",title_text="Safra", secondary_y = False, row=1, col=1)
        pre_fig.update_yaxes(tickformat=".2%",title_text="Taxa de Inadimplência", secondary_y = True, row=1, col=1)

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

def distInadimplenciaScore(data, flag):
    colors=["rgba(0, 33, 64,1)", "rgba(206, 21, 67,1)"]

    # Texto da Tabela descrevendo gráfico
    static_desc = "Podemos observar nas barras em azul a representatividade de cada faixa de score. Nas bolas em vermelho, obervamos a taxa de inadimplência dentro se cada faixa de score."

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
        raise Exception("Flag invalida, por favor digite yes ou no")

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

def Ks2(data,flag):
    # Cores pro gráfico
    colors = ["rgb(0, 33, 64)", "rgb(206, 21, 67)", "rgb(212, 175, 55)"]

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

    static_desc = """O KS2 é uma métrica utilizada para sabermos quanto o modelo discrimina os bons dos maus clientes. 
        Seu valor é a maior diferença das distribuições acumuladas dos dois públicos analisados. 
        Quanto maior o KS2, melhor será a discriminação dos dois públicos pelo modelo em análise."""

    flag = flag.strip().lower()

    if flag == "no":

        # Texto da Tabela descrevendo gráfico
        static_desc = static_desc

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
        
        # Add linha de Bom
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualBomAcc, hovertemplate="%{x},%{y}" , name="Bom", marker_color=colors[0]), row=1,col=2
        )

        # Add linha de Mal
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualMalAcc,hovertemplate="%{x},%{y}" , name="Mal", marker_color=colors[1]), row=1, col=2
        )

        # Add linha de KS2
        fig.add_trace(
            go.Scatter(x=label, y=df.KS2, name="KS2", marker_color=colors[2]), row=1, col=2
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
    
    elif flag == "yes":
                

        pre_fig= make_subplots(
        rows=1, cols=2,
        specs= [[{"colspan": 2},None]]
        )
        
        # Add linha de Bom
        pre_fig.add_trace(
            go.Scatter(x=label, y=df.PercentualBomAcc, hovertemplate= "%{x},%{y}", name="Bom", marker_color=colors[0]), row=1,col=1
        )

        # Add linha de Mal
        pre_fig.add_trace(
            go.Scatter(x=label, y=df.PercentualMalAcc, name="Mal", hovertemplate= "%{x},%{y}", marker_color=colors[1]), row=1, col=1
        )

        # Add linha de KS2
        pre_fig.add_trace(
            go.Scatter(x=label, y=df.KS2, name="KS2", marker_color=colors[2]), row=1, col=1
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
            
        # Add linha de Bom
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualBomAcc, hovertemplate="%{x},%{y}" , name="Bom", marker_color=colors[0]), row=1,col=2
        )

        # Add linha de Mal
        fig.add_trace(
            go.Scatter(x=label, y=df.PercentualMalAcc, hovertemplate="%{x},%{y}" , name="Mal", marker_color=colors[1]), row=1, col=2
        )

        # Add linha de KS2
        fig.add_trace(
            go.Scatter(x=label, y=df.KS2, name="KS2", marker_color=colors[2]), row=1, col=2
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
        raise Exception(" Flag invalida, por favor digite 'YES' ou 'NO' ")
        
def PiramideEtaria(data, flag):
    colors=["rgba(0, 33, 64,0.5)", "rgba(0, 33, 64,1)","rgba(206, 21, 67,0.5)", "rgba(206, 21, 67,1)"]
    bin = [10,20,30,40,50,float("inf")]


    df = data.groupby([data.SEXO,pd.cut(data.IDADE, bins = bin)]).count()
    tratado = df.loc[:,['IDADE']]
    totalPessoas = tratado.IDADE.groupby(level=0).sum()
    tratado["IDADEPERCENTUAL"] = tratado.IDADE / tratado.IDADE.groupby(level=0).sum()
    label = ["10-20","20-30","30-40","40-50",">50"]

    #print(tratado.groupby('SEXO').get_group("F"))

    static_desc = "Pirâmide etária ou pirâmide demográfica, consiste num histograma que mostra a distribuição de diferentes grupos etários numa população, em que normalmente se cria a forma de uma pirâmide cuja altura é proporcional à quantidade que representa a estrutura da população por sexo e idade, designado de cortes."


    flag = flag.strip().lower()

    if flag == "no":

        # Texto da Tabela descrevendo gráfico
        static_desc = static_desc
        
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
                font=dict(size=10),
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
                'text': "Pirâmide Etária",
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
                'text': "Pirâmide Etária",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            barmode = 'overlay'
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
                'text': "Pirâmide Etária",
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
        raise Exception("Flag invalida, por favor digite yes ou no")

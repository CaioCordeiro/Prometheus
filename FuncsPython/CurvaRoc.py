import pandas as pd
import numpy as np
import math
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

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

        static_desc = static_desc
        Titulo = str(input("Tipo da Descrição [1 - Oportunidade], [2 - Alerta], [3 - Risco]: "))
        analise = str(input("digite a descrição desejada: "))

        # Fazendo os subplots para colocar a descrição e o gráfico na mesma imagem
        if Titulo == "1":
            Titulo = "Oportunidade"

            fig = make_subplots(
            rows=1, cols=3,
            specs= [[{"type": "table"},{"colspan": 2},None]]
            )

            # Add Table
            fig.add_trace(                   
            go.Table(
                header=dict(
                    values=["Descrição do Gráfico"],
                    font=dict(size=12),
                    align="left"
                ),
                cells=dict(
                    values=[static_desc],
                    line_color='darkslategray',
                    align = "left")
            ),
            row=1, col=1
            )

            fig.add_trace(                   
            go.Table(
                  columnorder = [1,2],
                  columnwidth = [80,400],
                header=dict(
                    values=[Titulo],
                    font=dict(size=12),
                    line_color='darkslategray',
                    fill=dict(color=['lightgreen']),
                    align="left"
                ),
                cells=dict(
                    values=[analise],
                    line_color='darkslategray',
                    fill=dict(color=['lightgreen']),
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

        elif Titulo == "2":
            Titulo = "Alerta"

            fig = make_subplots(
            rows=1, cols=3,
            specs= [[{"type": "table"},{"colspan": 2},None]]
            )

            # Add Table
            fig.add_trace(                   
            go.Table(
                header=dict(
                    values=["Descrição do Gráfico"],
                    font=dict(size=12),
                    align="left"
                ),
                cells=dict(
                    values=[static_desc],
                    line_color='darkslategray',
                    align = "left")
            ),
            row=1, col=1
            )

            fig.add_trace(                   
            go.Table(
                  columnorder = [1,2],
                  columnwidth = [80,400],
                header=dict(
                    values=[Titulo],
                    font=dict(size=12),
                    line_color='darkslategray',
                    fill=dict(color=['yellow']),
                    align="left"
                ),
                cells=dict(
                    values=[analise],
                    line_color='darkslategray',
                    fill=dict(color=['yellow']),
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
        
        elif Titulo == "2":
            Titulo = "Risco"

            fig = make_subplots(
            rows=1, cols=3,
            specs= [[{"type": "table"},{"colspan": 2},None]]
            )

            # Add Table
            fig.add_trace(                   
            go.Table(
                header=dict(
                    values=["Descrição do Gráfico"],
                    font=dict(size=12),
                    align="left"
                ),
                cells=dict(
                    values=[static_desc],
                    line_color='darkslategray',
                    align = "left")
            ),
            row=1, col=1
            )

            fig.add_trace(                   
            go.Table(
                  columnorder = [1,2],
                  columnwidth = [80,400],
                header=dict(
                    values=[Titulo],
                    font=dict(size=12),
                    line_color='darkslategray',
                    fill=dict(color=['red']),
                    align="left"
                ),
                cells=dict(
                    values=[analise],
                    line_color='darkslategray',
                    fill=dict(color=['red']),
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
        

def main():
    lis = [1,0.865344899,0.635498908,0.458299404,0.324505812,0.223178144,0.142302472,0.083507405,0.040254912,0.011836903,0]
    lis2 = [1,0.988813841,0.945120322,0.883916351,0.812689834,0.730966186,0.638938756,0.534794745,0.41235282,0.251699134,0]
    dataframe = pd.DataFrame(list(zip(lis,lis2)),columns=['FPR','TPR'])
    CurvaRoc(dataframe,"yes")

if __name__ == '__main__':
    main()
    
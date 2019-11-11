import pandas as pd
import numpy as np
import math
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def AlvoDecil(data, casasDecimais):
    bin = [0,10,20,30,40,50,60,70,80,90,100]
    df = data.groupby(pd.cut(data.SCORE, bins = bin)).mean()
    tratado = df.loc[:,['ALVO']]
    label = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    tratado.ALVO = tratado.ALVO.apply(lambda x: round(x, casasDecimais))
    fig = px.line(x=tratado.ALVO, y=label, title='Decil Alvo')
    fig.show()
    print(tratado)
    #print(data.groupby(pd.qcut(data.SCORE, 10)).to_string())
    return

def main():
    file = "./BASE_CREDITO.txt";
    dataframe = pd.read_csv(file, delimiter= '\t')
    AlvoDecil(dataframe, 3)

if __name__ == '__main__':
    main()
    
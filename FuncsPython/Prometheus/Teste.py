import pandas as pd
import Prometheus as pro

def main():
    file = "../BASE_CREDITO.txt"
    dataframe = pd.read_csv(file, delimiter= '\t')
    pro.AlvoFaixaScore(dataframe, 2,"yes")

if __name__ == '__main__':
    main()
    
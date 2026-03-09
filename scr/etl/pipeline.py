from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():

    df = extract_data("data/raw/dados_bancarios_ficticios.csv")
    df = transform_data(df)
    load_data(df)
    print("Pipeline executado com sucesso")

if __name__ == "__main__":
    run_pipeline()
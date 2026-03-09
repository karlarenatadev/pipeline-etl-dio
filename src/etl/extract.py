import pandas as pd

def extract_data(path: str) -> pd.DataFrame:
    print("Extraindo dados do arquivo...")

    df = pd.read_csv(path)
    print(f"{len(df)} registros carregados")

    return df
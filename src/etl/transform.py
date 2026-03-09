import pandas as pd

def mask_card(card):
    return "****-****-****-" + card[-4:]

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Transformando dados...")
    df = df.drop_duplicates() # remove duplicados
    df["Nome"] = df["Nome"].str.title() # padroniza nomes 
    df["Cartao_Mascarado"] = df["Cartão"].apply(mask_card) # mascara o cartão
    df = df.drop(columns=["Cartão"])
    
    print("Transformação concluída")
    
    return df
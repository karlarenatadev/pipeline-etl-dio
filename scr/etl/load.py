import sqlite3

def load_data(df):
    print("Carregando dados no banco...")

    conn = sqlite3.connect("bank.db")

    df.to_sql(
        "clientes",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
    print("Dados carregados com sucesso")
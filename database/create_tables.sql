CREATE TABLE IF NOT EXISTS transacoes (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data_transacao DATE NOT NULL,
    tipo_transacao VARCHAR(20) NOT NULL, -- Ex: 'PIX', 'TED', 'BOLETO'
    valor DECIMAL(12, 2) NOT NULL,      -- Formato monetário
    status VARCHAR(15) DEFAULT 'ATIVO'
);

-- Dica bônus: Criar um índice para buscas mais rápidas (recrutadores adoram ver isso)
CREATE INDEX IF NOT EXISTS idx_cliente ON transacoes(id_cliente);
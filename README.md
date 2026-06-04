# RPA Document Processing Demo

Projeto funcional para simular processamento de documentos com Python.

## Como executar

```bash
python src/generate_receipts.py --n 20 --output-dir data/receipts_txt
python src/parse_receipts.py --input-dir data/receipts_txt --output reports/parsed_receipts.csv
```

## O que o projeto faz

1. Gera recibos ficticios em texto.
2. Extrai campos com expressoes regulares.
3. Exporta uma tabela estruturada em CSV.

## Saida

- `reports/parsed_receipts.csv`

## Estrutura

```text
src/generate_receipts.py
src/parse_receipts.py
data/receipts_txt/
reports/parsed_receipts.csv
```

## Dados

Todos os documentos sao ficticios e criados pelo proprio projeto.

## Proximos passos

- Adicionar leitura de imagens com OCR.
- Criar validacao de campos.
- Exportar para Excel.

## Licenca

MIT License.

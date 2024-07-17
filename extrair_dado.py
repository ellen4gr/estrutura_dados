import csv
import re

input_csv = r'C:CAMINHO.csv'
output_txt = r'C:CAMINHOtxt'

try:
    emails = set()
    with open(input_csv, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                credential = row[0]
          
                match = re.search(r'XXX://([^/]+)', XXXX)
                if match:
                    XXXX = match.group(1)
                    XXXX.add(XXXX)

    with open(output_txt, 'w', encoding='utf-8') as file:
        for XXX in XXXX:
            file.write(f"{XXXX}\n")

    print(f"Novo arquivo XXXXXX.txt criado com {len(XXXXX)} XXXXX.")

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado ({e.filename}).")
except Exception as e:
    print(f"Erro inesperado: {str(e)}")

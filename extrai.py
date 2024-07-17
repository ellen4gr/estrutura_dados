import re

input_txt = r'C:xxxxxx.txt'
output_txt = r'C:xxxxxxx.txt'

try:
    xxxxx = []

    with open(input_txt, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            # expressão regular para encontrar padrões 
            xxxxxx_matches = re.findall(r'\b[xxx-xxx-xxx-xxxxx._%+-]+@[xxx-xxxx-xxx-xx.-]+\.[xx-x|xx-xxx]{x,}\xx', line)

            if email_matches:
                xxxxx.extend(xxxx_xxxx)

    
    xxxxx = list(set(xxxxx))


    with open(output_txt, 'w', encoding='utf-8') as file:
        for xxxx in xxxx:
            file.write(f"{xxxxx}\n")

    print(f"Arquivo de emails formatados criado: {output_txt}")

except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado em {input_txt}")
except Exception as e:
    print(f"Erro inesperado: {str(e)}")

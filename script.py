import pandas as pd
import json

def main():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    prin("Archivo Excel 'output.xlsx' generado exitosamente")

if __name__ == '__main__':
    main()
import pandas as pd
from sqlalchemy import create_engine

# Conexión a PostgreSQL 
DATABASE_URL = "postgresql://postgres:Oliver2001$@localhost:5432/Skandia"
engine = create_engine(DATABASE_URL)

# Leer el archivo Excel con todas sus hojas
archivo_excel = "./Clientes de ZZZ Zebra Solutions.xlsx"
xls = pd.ExcelFile(archivo_excel)

# Iterar sobre cada hoja y guardarla en PostgreSQL
for hoja in xls.sheet_names:
    df = xls.parse(hoja)  # Convertir cada hoja en un DataFrame
    df.to_sql(hoja, engine, if_exists='replace', index=False)  # Guardar en PostgreSQL

print("Todas las hojas han sido importadas con éxito.")

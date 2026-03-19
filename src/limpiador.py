import pandas as pd

import pandas as pd

def limpiar_planilla(df):
    # 1. Limpiar nombres de columnas
    df.columns = df.columns.str.strip().str.replace('_$$', '', regex=False).str.lower()
    
    # 2. Eliminar filas vacías y duplicados
    df = df.dropna(how='all').drop_duplicates()
    
    # 3. Limpiar nombres de clientes
    if 'nombre cliente' in df.columns:
        df['nombre cliente'] = df['nombre cliente'].astype(str).str.strip().str.title()
        df = df.dropna(subset=['nombre cliente'])
    
    # 4. Estandarizar sucursales
    if 'sucursal' in df.columns:
        df['sucursal'] = df['sucursal'].astype(str).str.strip().str.title().replace('Sp', 'San Pedro')
    
    # 5. Corregir montos y fechas
    if 'monto' in df.columns:
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce').fillna(0)
    
    if 'fecha_venta' in df.columns:
        df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], errors='coerce')

    # 6. Limpieza general de espacios en todo el dataframe
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    return df
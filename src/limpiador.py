import pandas as pd

def limpiar_planilla(df):
    # 1. Normalizar nombres de columnas (todo a minúscula para que el código no falle)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # 2. Limpieza de filas vacías
    df = df.dropna(how='all').drop_duplicates()
    
    # 3. Limpia Nombres (Formato Título)
    if 'nombre' in df.columns:
        # .astype(str) evita errores si hay números mezclados
        # .str.strip() quita espacios al inicio/final
        # .str.title() pone la primera en Mayúscula y el resto en minúscula
        df['nombre'] = df['nombre'].astype(str).str.strip().str.title()
        
        # Eliminar registros donde el nombre quedó como "Nan" o vacío
        df = df[~df['nombre'].isin(['Nan', 'None', ''])]

    # 4. Limpia Sucursales
    if 'sucursal' in df.columns:
        df['sucursal'] = df['sucursal'].astype(str).str.strip().str.title()
        # Corrección específica después de aplicar el título
        df['sucursal'] = df['sucursal'].replace({'Sp': 'San Pedro', 'S.P.': 'San Pedro'})
    
    # 5. Formateo de Montos y Fechas
    if 'monto' in df.columns:
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce').fillna(0)
    
    if 'fecha_venta' in df.columns:
        df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], errors='coerce')
        
    # 6. Género en minusculas
    if 'genero' in df.columns:
        df['genero'] = df['genero'].astype(str).str.strip().str.title()


    # 7. Limpieza final de celdas de texto restantes
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    return df
 

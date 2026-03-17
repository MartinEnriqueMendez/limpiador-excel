import pandas as pd

def limpiador_datos(archivo_entrada):
    #1.cargar datos
    df = pd.read_excel(archivo_entrada)
    
    #2. Limpiar nombres de columnas (quitar espacios)
    df.columns = df.columns.str.strip().str.replace('_$$', '', regex=False).str.lower()
    
    #3. Eliminar duplicados
    df = df.drop_duplicates()
    
    #4. Limpiar nombres de clientes (formato titulo)
    df['nombre cliente'] = df['nombre cliente'].str.strip().str.title()
    
    #5. Estandar sucursales
    df['sucursal'] = df['sucursal'].str.strip().str.title().replace('Sp', 'San Pedro')
    
    #6. Corregir montos (convertir a número, errores a 0)
    df['monto'] = pd.to_numeric(df['monto'], errors = 'coerce').fillna(0)
    
    #7. Estandarizar fechas
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], errors = 'coerce')
    
    #8. Eliminar filas donde el cliente sea nulo
    df = df.dropna(subset=['nombre cliente'])
    
    return df

if __name__ == "__main__":
    df_limpio = limpiador_datos('datos_sucios.xlsx')
    df_limpio.to_excel('datos_limpios.xlsx', index=False)
    print("¡Datos pulidos y guardados en 'datos_limpios.xlsx'!")
    print(df_limpio)
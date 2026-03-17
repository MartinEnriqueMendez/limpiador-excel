import pandas as pd

def limpiar_planilla(ruta_archivo):
    try:
        #cargar los datos
        df = pd.read_excel(ruta_archivo)
        print("Archivo cargado con éxito")
        
        #limpieza básica: eliminar filas vacias
        df_limpio = df.dropna(how = 'all')
        
        #guardar resultado
        df_limpio.to_excel('data/output/planilla_limpia.xlsx', index=False)
        print("Limpieza básica completada.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Iniciando limpiador...")
    
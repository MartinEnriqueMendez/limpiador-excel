import os
import glob
import pandas as pd
# Importamos tu función desde el archivo limpiador.py
from limpiador import limpiar_planilla 


def ejecutar_procesamiento():
    input_folder = 'data/input/'
    output_folder = 'data/output/'
    os.makedirs(output_folder, exist_ok=True)

    archivos = glob.glob(os.path.join(input_folder, "*.xlsx"))

    if not archivos:
        print("No se encontraron archivos en data/input/")
        return

    for ruta in archivos:
        nombre = os.path.basename(ruta)
        print(f"Procesando: {nombre}...")
        
        try:
            df_sucio = pd.read_excel(ruta)
            
            # INVOCACIÓN AL LIMPIADOR
            df_pulido = limpiar_planilla(df_sucio)
            
            df_pulido.to_excel(os.path.join(output_folder, f"PULIDO_{nombre}"), index=False)
            print(f"--- {nombre} finalizado con éxito ---")
            
            df_pulido = limpiar_planilla(df_sucio)
            #Después de guardar el excel, se genera el reporte
            generar_pdf(df_pulido, nombre_archivo)
            
        except Exception as e:
            print(f"Error en {nombre}: {e}")


if __name__ == "__main__":
    ejecutar_procesamiento()


"""

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
    
"""


import os
import glob
import pandas as pd
# Importamos tu función desde el archivo limpiador.py
from limpiador import limpiar_planilla
from reporte import generar_reporte


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
            generar_reporte(df_pulido)
            
        except Exception as e:
            print(f"Error en {nombre}: {e}")


if __name__ == "__main__":
    ejecutar_procesamiento()

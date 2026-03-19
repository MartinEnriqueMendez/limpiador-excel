import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def generar_reporte(df, nombre_original):
    #1. cargar los datos ya pulidos
    df = pd.read_excel('datos_limpios.xlsx')
    
    #2. crear gráfico de ventas por sucursal
    # Agrupar los datos para el gráfico
    resumen = df.groupby('sucursal')['monto'].sum()
    
    plt.figure(figsize=(6, 4))
    resumen.plot(kind = 'bar', color = ['#007bff', '#28a745'])
    plt.title('ventas totales por sucursal ($)', fontsize = 14, fontweight = 'bold')
    plt.xlabel('Sucursal')
    plt.ylabel('Monto acumulado')
    plt.xticks(rotation = 0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    #guardar el gráfico como imágen temporal
    plt.savefig('grafico_temp.png')
    plt.close()
    
    #3. configurar el pdf
    class PDF(FPDF):
        def header(self):
            #titulo del reporte
            self.set_font('Arial', 'B', 16)
            self.set_text_color(33, 37, 41)
            self.cell(0, 10, 'INFORME EJECUTIVO DE VENTAS', 0, 1, 'C')
            self.set_font('Arial', '', 10)
            self.cell(0, 5, 'Análisis de operaciones por sucursal', 0, 1, 'C')
            self.ln(10)
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')
    
    pdf = PDF()
    pdf.add_page()
    
    #--sección 1: Gráfico --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, '1. Resumen Estadístico', 0, 1)
    pdf.ln(5)
    #se inserta la imágen del gráfico
    pdf.image('grafico_temp.png', x=30, w=150)
    pdf.ln(10)
    
    #--sección 2: tabla de datos --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, '2. Detalle de operaciones procesadas', 0, 1)
    pdf.ln(5)
    
    #Encabezados de tabla
    pdf.set_fill_color(0, 123, 255) #Azul
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Arial', 'B', 10)
    
    pdf.cell(55, 10, 'Cliente', 1, 0, 'C', True)
    pdf.cell(35, 10, 'Fecha', 1, 0, 'C', True)
    pdf.cell(30, 10, 'Monto ($)', 1, 0, 'C', True)
    pdf.cell(50, 10, 'Sucursal', 1, 1, 'C', True)
    
    #filas en la tabla
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', '', 9)
    
    for _, fila in df.iterrows():
        #se formatea la fecga a solo día/mes/año
        fecha_str = str(fila['fecha_venta'].date())
        
        pdf.cell(55, 8, str(fila['nombre cliente']), 1)
        pdf.cell(35, 8, fecha_str, 1, 0, 'C')
        pdf.cell(30, 8, f"{fila['monto']:,.2f}", 1, 0, 'R')
        pdf.cell(50, 8, str(fila['sucursal']), 1)
        pdf.ln()
        
    #4. Guardar archivo final y limpiar
    nombre_salida = f"data/output/REPORTE_{nombre_original.replace('.xlsx', '.pdf')}"
    pdf.output(nombre_salida)
    os.remove('grafico_temp.png') #se borra la imágen temporal
    print(f">>> ¡Éxito! El archivo {nombre_original} ha sido generado.")
    
if __name__ == "__main__":
    generar_reporte()

import pandas as pd
import numpy as np

data = {
    ' Nombre Cliente ': [' Juan Perez', 'Ana Gomez ', 'JUAN Perez', 'Luis Lopez', None, ' Marta Diaz'],
    'Fecha_Venta': ['2024-01-10', '11/01/2024', '02-10-2025','2024-05-15', '2024-05-16','17-01-2024'],
    'Monto_$$': ['1500.50', '2300', '1500.50', 'not_a_number', None, None],
    'sucursal': ['San Pedro', 'SP', 'san pedro', 'Capital', 'Capital', 'San Pedro']
}
"""
data = {
    ' Nombre Cliente ': ['Juan Perez', 'Ana Gomez', 'JUAN Perez', 'Luis Lopez', None, 'Marta Diaz'],
    'Fecha_Venta': ['2024-01-10', '11/01/2024', '2024-01-10','2024-05-15', '2024-05-16','17-01-2024'],
    'Monto_$$': ['1500.50', '2300', '1500.50', 'not_a_number', '4500.75','1200'],
    'sucursal': ['San Pedro', 'SP', 'san pedro', 'Capital', 'Capital', 'San Pedro']
}
"""

df = pd.DataFrame(data)
df.to_excel('sucios.xlsx', index=False)
print("¡Archivo 'sucios.xlsx' creado!")
#df.to_excel('datos_sucios.xlsx', index=False)
#print("¡Archivo 'datos_sucios.xlsx' creado!")
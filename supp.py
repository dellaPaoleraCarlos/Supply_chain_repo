import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("global_supply_chain_risk_2026.csv")
print(df.head(5))
#print(df.info())
print(df.describe())

# Lo unico que nos llama la atencion es que la columna "Date" esta como objeto
# La voy a cambiar a formato datetime para poder analizarla mejor
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print(df.info())  

'''plt.figure(figsize=(10, 6))
plt.hist(df['Weather_Condition'], bins=30, color='salmon', edgecolor='black')
plt.xlabel('Weather_Condition')
plt.ylabel('Frequency') 
plt.title('Distribution of Weather Conditions')  
plt.show()'''

#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#

# Limpia los nombres: cambia espacios por "_" y pasa todo a minúscula
df.columns = [c.replace(' ', '_').lower() for c in df.columns]

# 'if_exists="replace"' borra la tabla si ya existe y la crea de nuevo
# 'index=False' evita que el índice de Pandas se cree como una columna extra
df.to_csv('envios_stats.csv', index=False)

print("¡Éxito! El DataFrame ya es una tabla SQL en supply_chain_data.csv")
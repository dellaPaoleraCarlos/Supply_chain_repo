📊 Dashboard de Análisis de Puertos y Logística
Este proyecto consiste en un tablero interactivo desarrollado en Power BI que visualiza métricas clave de operaciones portuarias. El objetivo principal es identificar la relevancia de los puertos de origen y analizar la distribución de carga mediante indicadores de frecuencia y volumen.


🛠️ Proceso de Datos (Pipeline)
El proyecto siguió un flujo de trabajo de tres etapas para asegurar la integridad y calidad de la información:

Extracción (Sourcing): Se utilizó un dataset crudo proveniente de Kaggle con registros globales de logística y transporte.

Limpieza y Transformación (Wrangling): * Se realizó una limpieza profunda utilizando Python.

Exportación del set de datos optimizado a un archivo CSV para garantizar una carga ligera en el modelo.

Modelado y Visualización: * Importación del CSV a Power BI Desktop.

Creación de una Tabla de Calendario personalizada para análisis cronológico.

Desarrollo de medidas en DAX para métricas de conteo y participación.


📈 Características del Tablero
El dashboard incluye las siguientes secciones y visualizaciones:

Mapa de Relevancia Geográfica: Un mapa de burbujas donde el tamaño indica la frecuencia de menciones de cada puerto de origen, permitiendo identificar rápidamente los nodos logísticos principales.

Análisis Temporal: Gráficos de líneas/columnas con etiquetas rotadas a 45° para una lectura clara de la evolución mensual.

KPIs Principales: Tarjetas con formato personalizado (ej. 1.000 km) para métricas de distancia y volumen total.

Filtros Interactivos: Segmentadores por fecha, región y tipo de carga.


🚀 Tecnologías Utilizadas
Power BI: Visualización y modelado de datos.

DAX: Cálculos de inteligencia de tiempo y métricas personalizadas.

Kaggle Dataset: Fuente de datos original.

CSV: Formato de almacenamiento intermedio.

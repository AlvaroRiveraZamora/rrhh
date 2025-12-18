Panel de Analítica RRHH – Diversidad y Modalidad Laboral
1. Pregunta que busca responder el panel

El objetivo de este panel es responder una pregunta simple pero relevante para gestión de personas:

¿Cómo se distribuyen los colaboradores de la organización según género, modalidad de trabajo, tipo de jornada y región, y cómo se relaciona esto con su estatus laboral?

La idea es entregar una visión general y clara de la composición de la dotación, permitiendo identificar patrones de distribución y posibles focos de análisis para gestión de personas, diversidad y planificación.

2. Fuentes de datos utilizadas

Para este ejercicio se utilizaron datos públicos y/o simulados de RRHH, estructurados en distintas tablas lógicas:

Información base de empleados

Catálogos de funciones, departamentos y regiones

Tablas de referencia para modalidad de trabajo, jornada, educación y estatus

El resultado final se consolidó en un único archivo:

dataset_RRHH.xlsx

Este archivo es el dataset que consume directamente el dashboard en Power BI.

3. Proceso de limpieza y transformación de los datos

El proceso se pensó de forma simple y ordenada, separando responsabilidades:

SQL

Consolidación de la información desde una tabla central de empleados.

Uso de join con tablas maestras para normalizar atributos como función, departamento, región y modalidad.

Estandarización de nombres de columnas para facilitar el análisis.

Python

Conversión y validación de campos de fecha (contratación y baja).

Normalización del estatus del empleado (por ejemplo, empleados sin fecha de baja se consideran activos).

Validaciones básicas de calidad (eliminación de registros incompletos).

Exportación del dataset final en formato Excel.

El objetivo fue dejar un dataset claro, consistente y fácil de consumir desde Power BI.

4. Decisiones de diseño del panel

El diseño del dashboard se enfocó en claridad y lectura rápida, evitando sobrecargar con información innecesaria.

Principales decisiones:

Uso de gráficos simples (barras y distribuciones) para facilitar la comparación.

Filtros por región, modalidad y estatus para permitir exploración sin complejidad.

Títulos claros que expliquen qué responde cada visual.

Flujo de lectura de arriba hacia abajo, partiendo por una visión general y luego el detalle.

El panel busca responder la pregunta planteada de forma directa, priorizando la comprensión del usuario por sobre la sofisticación técnica.

5. Publicación y acceso

El dashboard fue desarrollado en Power BI Desktop utilizando modo Import, por lo que los datos se encuentran embebidos dentro del archivo pbix.

Esto permite:

Visualizar el panel sin necesidad de conexiones externas.

Revisar el modelo y las visualizaciones de forma local.

Compartir el archivo de manera simple.

6. Alcance del ejercicio

Este desarrollo no busca ser un producto final ni exhaustivo. El foco está en:

Definir una pregunta clara.

Construir un dataset coherente.

Comunicar información de forma efectiva a través de visualizaciones.

import pandas as pd

# 1. Cargar el resultado del query SQL
# Este archivo representa la salida del SQL con JOINs
df = pd.read_csv("rrhh_sql.csv")

# 2. Conversión de columnas de fecha
df["Fecha Contratación"] = pd.to_datetime(df["Fecha Contratación"], errors="coerce")
df["Fecha Baja"] = pd.to_datetime(df["Fecha Baja"], errors="coerce")

# 3. Normalización del estatus del empleado
# Si no existe fecha de baja, se considera Activo
df["Estatus"] = df["Estatus"].fillna("Activo")

# 4. Validaciones básicas de calidad de datos
# Eliminamos registros sin ID de empleado
df = df.dropna(subset=["ID Empleado"])

# 5. Reordenar columnas
df = df[
    [
        "ID Empleado",
        "Función",
        "Departamento",
        "Región",
        "Educación",
        "Género",
        "Jornada",
        "Modalidad",
        "Fecha Contratación",
        "Estatus",
        "Fecha Baja"
    ]
]

# 6. Exportar dataset final utilizado por el dashboard
df.to_excel("dataset_RRHH.xlsx", index=False)

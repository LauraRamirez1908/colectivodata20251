import pandas as pd

usuariosDataFrame=pd.read_excel("./data/usuarios_sistema_completo-xlxs")

# Asegurar formato de fecha
usuariosDataFrame['fecha_nacimiento'] = pd.to_datetime(usuariosDataFrame['fecha_nacimiento'], errors='coerce')

# Crear columnas auxiliares
usuariosDataFrame['anio_nacimiento'] = usuariosDataFrame['fecha_nacimiento'].dt.year
usuariosDataFrame['edad'] = datetime.now().year - usuariosDataFrame['anio_nacimiento']

print(usuariosDataFrame.isnull().sum())



# Listado de aprendices/estudiantes
estudiantes = usuariosDataFrame.query('tipo_usuario == "estudiante"')
print(estudiantes)

# listado solo instructores/profesores
docentes = usuariosDataFrame.query('tipo_usuario == "docente"')
print(docentes)

# listado de procesores especialistas en desarrollo web/sistemas

docentesWebSistemas = usuariosDataFrame[
    (usuariosDataFrame['tipo_usuario'] == 'docente') &
    (usuariosDataFrame['especialidad'].str.contains('Ingenieria de Sistemas', case=False, na=False))
]
print("Docentes en desarrollo web o sistemas:\n", docentesWebSistemas)

# listado de usuarios con direcciones en medellin

usuariosMedellin = usuariosDataFrame[
    usuariosDataFrame['direccion'].str.contains('medellin', case=False, na=False)
]
print(usuariosMedellin)


# listado de usuarios cuyas direcciones terminen en sur

usuariosDireccionSur = usuariosDataFrame[
    usuariosDataFrame['direccion'].str.lower().str.strip().str.endswith("sur", na=False)
]
print(usuariosDireccionSur)

# listado de profesores que en su especialidad contega la palabra "datos"

docentesDatos = usuariosDataFrame[
    (usuariosDataFrame['tipo_usuario'] == 'docente') &
    (usuariosDataFrame['especialidad'].str.contains('datos', case=False, na=False))
]
print(docentesDatos)

# listado de docentes de itagui

docentesItagui = usuariosDataFrame[
    (usuariosDataFrame['tipo_usuario'] == 'docente') &
    (usuariosDataFrame['direccion'].str.contains('itagüí|itagui', case=False, na=False))
]
print(docentesItagui)

# listado de nacidos en los 90 o antes
nacidosAntes2000 = usuariosDataFrame[usuariosDataFrame['anio_nacimiento'] <= 1999]
print(nacidosAntes2000)



# listado de instructores mayores de 60 años
docentesMayores60 = usuariosDataFrame[
    (usuariosDataFrame['tipo_usuario'] == 'docente') &
    (usuariosDataFrame['edad'] > 60)
]
print(docentesMayores60)

# listado deprofesores y estudiantes nacidos > 2.000    
usuariosPost2000 = usuariosDataFrame[
    (usuariosDataFrame['tipo_usuario'].isin(['docente', 'estudiante'])) &
    (usuariosDataFrame['anio_nacimiento'] > 2000)
]
print("Docentes y estudiantes nacidos después del 2000:\n", usuariosPost2000)
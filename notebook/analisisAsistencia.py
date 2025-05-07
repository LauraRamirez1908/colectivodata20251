import pandas as pd

asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

print(asistenciaDataFrame)


#FILTROS o consultas detalladas

#Enontrar Los estudiantes que si asistieron 
estudiantesQueAsistieron=asistenciaDataFrame.query('estado=="asistio"')
print(estudiantesQueAsistieron)


#Necesito encontrar los estudiantes que faltaron

estudiantesQueNoAsistieron=asistenciaDataFrame.query('estado=="inasistencia"')
print(estudiantesQueNoAsistieron)

# necesito encontrar los estudiantes que llegaron tarde


#estudiantes de estrato 1

estudiantesEstratoUno=asistenciaDataFrame.query('estrato==1')
print(estudiantesEstratoUno)

#Estudiantes de estractos altos
estudiantesEstratoAlto = asistenciaDataFrame.query('estrato >= 4')
print(estudiantesEstratoAlto)

#Estudiantes que llegan en metro

estudiantesQueAndanEnMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
print(estudiantesQueAndanEnMetro)

#Estudiantes que llegan en bici 

estudiantesTransporteBici = asistenciaDataFrame.query('medio_transporte=="bicicleta"')
print(estudiantesTransporteBici)

# todos los estudiantes menos los que llegaron a pie
estudiantesQueNoCaminan=asistenciaDataFrame.query('medio_transporte!="a pie"')
print(asistenciaDataFrame["medio_transporte"].unique())

#todos los registros de asistencia de junio 

asistenciaJunio = asistenciaDataFrame[asistenciaDataFrame['fecha'].dt.month == 6]
print(asistenciaJunio)

#todos los estudiantes que utiliza transporte ecologicos
estudiantesTransporteEcologico = asistenciaDataFrame.query('medio_transporte in ["bicicleta", "a pie"]')
print(estudiantesTransporteEcologico)

# los que utilizan bus y son de estracto alto
busEstratoAlto = asistenciaDataFrame.query('medio_transporte == "bus" and estrato >= 4')
print(busEstratoAlto)


#los que usan bus y son de eztracto bajo
busEstratoBajo = asistenciaDataFrame.query('medio_transporte == "bus" and estrato <= 2')
print(busEstratoBajo)

#necesito estudiantes  que caminan para llegar a clases
estudiantesCaminan = asistenciaDataFrame.query('medio_transporte == "a pie"')
print(estudiantesCaminan)

#CONTEOS CON AGRUPACIONES

#conteo de registros por estados de asistencia 

conteoAsistencias=asistenciaDataFrame.groupby('estado').size()
print(conteoAsistencias)

#obtener el numero de registros por estrato

conteoPorEstrato = asistenciaDataFrame.groupby('estrato').size()
print(conteoPorEstrato)

#cantidad de estudiantes por medio de transporte 
conteoMedioTransporte=asistenciaDataFrame.groupby('medio_transporte').size()
print(conteoMedioTransporte)

#promedio de estrato por estado de asistencia
promedioAsistenciaPorEstracto=asistenciaDataFrame.groupby('estado')['estrato'].mean() 
print(promedioAsistenciaPorEstracto)

#maximo estrato pot estado
maxEstratoPorEstado = asistenciaDataFrame.groupby('estado')['estrato'].max()
print(maxEstratoPorEstado)

#minimo extracto por estado
minEstratoPorEstado = asistenciaDataFrame.groupby('estado')['estrato'].min()
print(minEstratoPorEstado)

#conteo de asistencia por grupo y estado 

conteoPorGrupoEstado = asistenciaDataFrame.groupby(['grupo', 'estado']).size()
print(conteoPorGrupoEstado)

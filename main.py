#importacion de la libreria para utilizar expresiones
import re

#importamos el metodo reduce
from functools import reduce

#inicialización del estacionamiento (hay 10 plazas)
plazas = [None] * 10  #matriz para 10 plazas (None significa que estan vacias inicialmente)
tarifa_hora = 1000  #costo por hora (se puede actualizar o cambiar en cualquier momento)
vehiculos = {} #diccionario para alamacenar informacion de los vehiculos ingresados
dinero = [] #montos que se van a almacenar por cada vehiculo ingresado.
total_dinero = [] #Declaramos la variable para calcular el monto total

#funcion para registrar entradas de vehiculos en un archivo
def registrar_entradas(mensaje):
    """ 
    Propósito: Guarda un mensaje en un archivo llamado registro_entradas.txt.
    Uso típico: Registrar las acciones de entrada de vehículos para mantener un historial.
    """
    try:
        archivo = open("registro_entradas.txt","a", encoding="UTF-8")  #modo "a" para escribir el archivo sin pisar el contenido anterior
        #UTF-8 para mantener los caracteres especiales y acentuaciones
        archivo.write(mensaje + "\n")
    except IOError:    #maneja errores relacionados con el acceso o la escritura en el archivo
        print("Error al acceder/escribir en el archivo de registro.")
        registrar_error("Error en el acceso/escritura del archivo de registro")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error(f"Error general: {e}")

def registrar_dinero(valor):
    """ 
    Propósito: Guarda un mensaje en un archivo llamado registro_entradas.txt.
    Uso típico: Registrar las acciones de entrada de vehículos para mantener un historial.
    """
    try:
        archivo = open("registro_monto.txt","a", encoding="UTF-8")  #modo "a" para escribir el archivo sin pisar el contenido anterior
        #UTF-8 para mantener los caracteres especiales y acentuaciones
        archivo.write(valor + "\n")
    except IOError:    #maneja errores relacionados con el acceso o la escritura en el archivo
        print("Error al acceder/escribir en el archivo de registro.")
        registrar_error("Error en el acceso/escritura del archivo de registro")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error(f"Error general: {e}")

#funcion buscar patentes
def autos_por_dia():
    """ 
    Propósito: Extrae todas las patentes de vehículos registradas en el archivo registro_entradas.txt.
    Resultado: Devuelve una lista de patentes registradas.
    """
    try:
        archivo = open("registro_entradas.txt", "r") #abrimos el archivo para leer
        caracteres = archivo.read() #leemos el archivo
        if not caracteres: #hacemos una validacion para que en caso de que este vacio devuelva una lista vacia
            return []
        patron = '[A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2}' #definimos el patron de las patentes para encontrarlas
        buscar = re.findall(patron, caracteres, re.IGNORECASE) # busca cuales coinciden
        return buscar
    except IOError:    #maneja errores relacionados con el acceso o la escritura en el archivo
        print("Error al acceder/escribir en el archivo de registro.")
        registrar_error("Error en el acceso/escritura del archivo de registro")
    except FileNotFoundError:
        print("Error, no se encontró ningun archivo")
        registrar_error("Error, no se encontró ningun archivo")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error(f"Error general: {e}")

#funcion para contar cantidad de patentes
def cantidad_autos():
    """ 
    Propósito: Calcula la cantidad de vehículos únicos ingresados en un día y muestra las patentes duplicadas junto con el número de veces que ingresaron.
    Uso típico: Obtener estadísticas de ingreso de vehículos.
    Resultado: Devuelve el número de vehículos únicos.
    """    
    patentes_dia = autos_por_dia() 
    patentes_sin_duplicar = [] 
    patentes_duplicadas = []
    for patente in patentes_dia:
        if patente not in patentes_sin_duplicar:
            patentes_sin_duplicar.append(patente)
        else:
            patentes_duplicadas.append(patente)
    cantidad_por_dia = len(patentes_sin_duplicar) 
    print(f"EL DIA DE LA FECHA INGRESARON {cantidad_por_dia} AUTOS")
    return cantidad_por_dia

#funcion contar dinero por dia
def contar_dinero(dinero): 
   """
    Propósito: Suma los valores almacenados en la lista dinero.
    Resultado: Devuelve la suma total de los montos. 
   """
   suma = reduce(lambda a, b: a + b, dinero)

   return suma

def registrar_error(error):
    try:
        archivo = open("registro_errores.txt","a", encoding="UTF-8") #modo "a" para escribir el archivo ain pisar el contenido anterior
        #UTF-8 para mantener los caracteres especiales y acentuaciones
        archivo.write(error + "\n")
    except IOError:    #maneja errores relacionados con el acceso o la escritura en el archivo
        print("Error al acceder/escribir en el archivo de registro.")
        registrar_error("Error en el acceso/escritura del archivo de registro")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error(f"Error general: {e}")

#funcion para registrar actividades en un archivo
def registrar_en_archivo(mensaje):
    """ 
    Propósito: Guarda un mensaje en un archivo llamado registro_estacionamiento.txt.
    Uso típico: Mantener un registro de las operaciones realizadas en el estacionamiento.
    """
    try:
        archivo = open("registro_estacionamiento.txt","a", encoding="UTF-8") #modo "a" para escribir el archivo ain pisar el contenido anterior
        #UTF-8 para mantener los caracteres especiales y acentuaciones
        archivo.write(mensaje + "\n")
    except IOError:    #maneja errores relacionados con el acceso o la escritura en el archivo
        print("Error al acceder/escribir en el archivo de registro.")
        registrar_error("Error en la escritura del archivo de registro")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error(f"Error general: {e}")

#funcion para mostrar el estado del estacionamiento (plazas disponibles/ocupadas)
def mostrar_plazas():
    """ 
    Propósito: Muestra el estado actual de las plazas del estacionamiento, indicando cuáles están ocupadas o disponibles.
    Resultado: Imprime el estado de cada plaza en la consola.
    """
    print("\nEstado del Estacionamiento:")
    for i in range (len(plazas)): #recorro plazas
        estado = [f"Ocupada por {plazas[i][0]}" if plazas[i]!=None else "Disponible"]  #comprension de listas para ver si el estado es ocupada/disponible
        print(f"Plaza {i + 1}: {estado[0]}")   # estado[0] es para que imprima solo lo que dice dentro de la lista
    registrar_en_archivo("Estado del estacionamiento mostrado al usuario.")
    print()

#funcion para el ingreso de vehiculo y para reservar plaza            
def reservar_plaza(patente, horas_reserva):
    """ 
    Propósito: Reserva una plaza para un vehículo, registrando la patente y las horas de reserva.
    """
    try:
        if patente not in [plaza[0] for plaza in plazas if plaza is not None]: #verificar si esta repetida la patente
            indice = plazas.index(None) #buscar el indice de la primera plaza disponible
            plazas[indice] = (patente, horas_reserva, 0) #tupla para registrar (patente, horas reservadas, horas permanencia)
            vehiculos[patente] = {'plaza': indice, 'horas_reservadas': horas_reserva, 'horas_permanencia': 0} #diccionario
            mensaje = (f"Vehículo {patente} reservó la plaza {indice + 1} por {horas_reserva} horas.")
            print(mensaje)
            registrar_en_archivo(mensaje)
            registrar_entradas(mensaje)
        else:
            print("La patente ya fue ingresada, intentelo de nuevo.")
            registrar_error("Intento de reserva fallido: la patente ya fue ingresada.")
    except Exception as e:
        print(f"Error al reservar plaza: {e}")
        registrar_error(f"Error al reservar plaza: {e}")

#funcion para salida de vehiculo y calculo de costos
def salida_vehiculo(patente, horas_permanencia):
    """ 
    Propósito: Libera una plaza ocupada por un vehículo, calcula el costo de permanencia y elimina la información del vehículo.
    Resultado: Devuelve la lista actualizada de montos recaudados (dinero).
    """
    global total_dinero #Declaramos global la variable para poder utilizarla durante todo el programa 
    try: 
        if plazas != ([None] * 10):  #verificar si hay alguna plaza ocupada. Si todas estan en none no podes eliminar ningun vehiculo
            for i in range(len(plazas)): #recorro plazas
                if plazas[i]!=None and (plazas[i][0] == patente):   #verificar si coincide con una patente
                    plazas[i] = None    #liberar plaza y ponerla disponible
                    costo_total = horas_permanencia * tarifa_hora
                    del vehiculos[patente]   #eliminar la entrada del diccionario
                    mensaje = f"Vehículo {patente} salió de la plaza {i + 1}. Costo total: ${costo_total}"
                    print(mensaje)
                    registrar_en_archivo(mensaje)
                    dinero.append(costo_total)
            registrar_dinero(dinero)
            return dinero
        print("Vehículo no encontrado. La patente no coincide con ningún vehículo ingresado.")   #en caso de no encontrar el vehiculo despues de iterar por todas las plazas
        registrar_error("Intento de salida fallido: vehículo no encontrado.")
    except Exception as e:
        print(f"Error al procesar salida de vehículo: {e}")
        registrar_error(f"Error al procesar salida de vehículo: {e}")

#funcion principal para el menu del sistema
def main():
    """ 
    Propósito: Proporciona una interfaz interactiva para el sistema del estacionamiento.
    Funcionamiento: Muestra un menú con opciones para ver el estado del estacionamiento, registrar ingresos y salidas de vehículos, y salir del programa.
    """
    global total_dinero #Declaramos global la variable para poder utilizarla durante todo el programa 
    try:
        while True:    #ciclo infinito. Muestra las opciones para elegir
            print("\n1. Mostrar plazas")
            print("2. Ingreso de vehículo")
            print("3. Salida de vehículo")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                mostrar_plazas() 
        
            elif opcion == "2":
                if None in plazas: #verificar si hay una plaza disponible
                    patente = input("Ingrese la patente del vehículo: ").upper()
                    while len(patente)!=6 and len(patente)!=7:   #valida que las patentes tengan un largo de 6 o 7 caracteres. Ejemplo: LMZ392 / AA398CC
                        print("Patente inválida.")
                        patente = input("Ingrese la patente del vehículo: ").upper()
                    horas_reserva = int(input("Ingrese las horas a reservar (máximo 24): "))    
                    while horas_reserva > 24:                    #valida que las horas ingresadas sean menor a 24
                        print("No se puede reservar más de 24 horas.")
                        horas_reserva = int(input("Ingrese las horas a reservar (máximo 24): "))
                    reservar_plaza(patente, horas_reserva)
                else:
                    print("Estan todas las plazas ocupadas")
                    registrar_error("Intento de reserva fallido: no hay plazas disponibles.")
            
            elif opcion == "3":
                if plazas == [None] * 10:
                    print("No hay ningun vehiculo ingresado. Ingrese un vehiculo")
                else:
                
                    patente = input("Ingrese la patente del vehículo: ").upper()
                    while len(patente)!=6 and len(patente)!=7: #valida que las patentes tengan un largo de 6 o 7 caracteres. Ejemplo: LMZ392 / AA398CC
                        print("Patente inválida.")
                        patente = input("Ingrese la patente del vehículo: ").upper()
                
                    horas_permanencia = int(input("Ingrese las horas de permanencia: ")) #son las horas que finalmente se quedó el vehiculo. Pueden ser más o menos de las que reservó anteriormente
                    total_dinero = salida_vehiculo(patente, horas_permanencia)
                
            elif opcion == "4":
                patentes = autos_por_dia()
                if not patentes:
                    print("No se registraron ingresos en el día")
                else:
                    cantidad_autos()
                print("-------------------------------------")
                if not total_dinero:
                    print("No hay dinero recaudado")
                else:
                    print(f"EL TOTAL DE DINERO EN EL DIA ES DE: {contar_dinero(total_dinero)}")
                print("-------------------------------------")
                print("Saliendo del sistema...")
                break  #finaliza completamente el ciclo while
            
            else:
                print("Opción no válida.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_error(f"Error general: {e}")

main() #llama a la funcion principal para comenzar el programa

"""
Sistema de Gestión para estacionamientos. Debe incluir:
-Gestión de entradas y salidas: Control preciso del ingreso y egreso de vehículos en el estacionamiento.
-Reservas de Espacios: Permite realizar reservas de plazas por horas (máximo 24 horas).El vehículo llega al
estacionamiento y reserva las horas que se quedará durante el día. 
-Control de Permanencia: Monitoreo detallado del tiempo que cada vehículo permanece en el estacionamiento
para luego calcular el costo.
-Cálculo de Costos: Determinación automática y precisa del costo de estadía, basado en el tiempo de permanencia
y las tarifas establecidas. El costo de la hora es de $1000, pero puede ser modificado cuando se requiera.

Matrices: se utiliza la matriz plazas.

Tuplas: cuando se registra un vehiculo en una plaza, se utiliza una tupla para almacenar tres valores:
la patente, las horas reservadas y las horas de permanencia (en entrada_vehiculo(patente) como plazas[indice])

Comprensión de listas: se utiliza en mostrar_plazas para el valor de la variable estado.

Diccionarios: se utiliza el diccionario vehiculos para almacenar informacion sobre cada vehiculo.
Cuando ingresa un vehiculo se registra en el diccionario. Cuando el vehiculo sale se elimina la entrada del diccionario.

Archivos: utilizamos 2 archivos.
Un archivo llamado registro_entradas.txt para registrar las acciones de entrada de vehículos para mantener un historial.
De ese archivo usamos la información para obtener todas las patentes que ingresaron en el día.
Otro archivo llamado registro_estacionamiento.txt para mantener un registro de todas las operaciones realizadas en el estacionamiento.
Permite un seguimiento detallado de las operaciones realizadas y problemas ocurridos.

Lambda y reduce: lo utilizamos en la funcion contar dinero para realizar la suma total del dinero por dia.

Expresiones regulares: lo utilizamos para buscar las patentes dentro de un archivo. Definimos un patron con lo cual se realiza la busqueda.

"""
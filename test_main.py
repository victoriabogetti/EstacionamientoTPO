from main import contar_dinero, autos_por_dia, cantidad_autos, salida_vehiculo
import random

def test_contar_dinero():
    sumas = [2000, 5000]
    assert contar_dinero(sumas) == 7000

def test_autos_por_dia():
    archivo = open("test_registro_entradas.txt", "r") 
    caracteres = archivo.read()
    assert autos_por_dia() == ['HOL123','TOM123']

def test_cantidad_autos():
    patentes_dia = ['HOL123','TOM123']
    assert cantidad_autos() == 2

def test_salida_vehiculo():
    patente = "HOL123"
    horas_permanencia = 4
    salida_vehiculo(patente, horas_permanencia) == [4]

    
    
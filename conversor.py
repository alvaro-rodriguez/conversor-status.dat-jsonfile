# -*- encoding: utf-8 -*-
#####Launcher.py ~~> Comienza la ejecución
import os
import sys
import datetime
import time
import pprint
import json
#vars

file = sys.argv[1]
log_nagios_bruto = []
pp = pprint.PrettyPrinter(indent=4)

#_vars del log
"""
old_stdout = sys.stdout
archivo_log = 'log-.txt'
print('LOG EN : '+ archivo_log)
log_file = open(archivo_log,"w")
sys.stdout = log_file
"""
#_vars para el diccionario
log_nagios_pulido = {}
log_nagios_refinado= {}
#funciones

#Abre el archivo como un objeto
def abrir_fichero(file):
    leer_fichero(open(file,'r'))

#Trasforma el objeto en una lista en la que cada elemento es una linea
def leer_fichero(fichero):
    jsonificador(fichero.readlines())
    
#Parsea las líneas y genera un diccionario con el contenido del fichero
def jsonificador(lineas):
    elemento=False
    #contador_elemento=0
    for linea in lineas:
        #print(linea)
        if '{' in linea:
            print('Abre elemento')
            indice=(linea.split('{')[0].replace(' ',''))
            print(indice)
            contador_elemento = 0
            salida = False
            while salida == False:
                if indice+'-'+str(contador_elemento) not in log_nagios_pulido.keys():
                        print('--Es un elemento nuevo')
                        log_nagios_pulido[indice+'-'+str(contador_elemento)]={}
                        salida = True
                else:
                    #print('nonuevo')
                    contador_elemento +=1
                
                
            elemento =True
        elif '}' in linea:
            print('Cierra el elemento')
            elemento=False
        elif elemento == True:
            print('Nuevo subelemento')
            print(linea.split('=')[0].replace('\t',''),':',linea.split('=')[1])
            log_nagios_pulido[indice+'-'+str(contador_elemento)][linea.split('=')[0].replace('\t','')]=linea.split('=')[1].replace('\n','')
    pp.pprint(log_nagios_pulido)
    guardar_json(log_nagios_pulido)

#Ahora modificamos los nombres de los elementos
#def modificar_nombres(log_nagios_pulido):
    #for elemento in log_nagios_pulido:
        #if elemento =='host_name':
            
#Guardamos el archivo json
def guardar_json(log_nagios_pulido):
    with open('dict.json', 'w') as outfile:
        json.dump(log_nagios_pulido, outfile)
#main(?)
print(sys.argv[1])

abrir_fichero(file)

"""
sys.stdout = old_stdout

log_file.close()
"""
#exceptions

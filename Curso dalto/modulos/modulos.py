#importando un modulo y asignandole el nombre "saludar"
import modulo_saludar as m_saludar

#Se puede importar todo con * pero esto es mala práctica así que no se utiliza
#from modulo_saludar import *

#desde ese módulo, se importó la función y se cambió el nombre
from modulo_saludar import saludar as salude

#se crea la variable
saludo = salude("Luis")

#mostramos el resultado
print(saludo)

#para ver las propiedades y metodos del namespace
#print(dir(m_saludar))

#para acceder al nombre del módulo
#print(m_saludar,__name__)
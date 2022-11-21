# Joel
Solo faltaria calcular el promedio, maxima y minima de todos los alumnos y mostrarlo en el archivo.txt con un mensaje.

import csv
from random import randint

alumnos = [
["44696178","Joel Caliba", "Urquiza1898", "3875458198", "joel@gmail.com", randint(0,10)],
["32456486","Maria Lopez","Tucuman 1176","3875234212","marialopez@gmail.com",randint(0,10)],
["35382123","Pablo Torres","Caseros 1896","3874676421","pablotorres@gmail.com",randint(0,10)],
["40754345","Carlos Gomez","Junin 1073","3874076245","carlosgomez@gmail.com",randint(0,10)],
["27534746","Cristian Fernandez","San Luis 135","3874347686","cristianfernandez@gmail.com",randint(0,10)],
["459711748","Facundo Torres","Ayacucho 429","387574938","facundo@gmail.com",randint(0,10)],
["354712721","Nahuel Tolaba","San Luis 52","3875128527","nahuel@gmail.com",randint(0,10)],
["29325693","Martina Palma","España 308","3876248628","martina@gmail.com",randint(0,10)],
["31534631","Matias Cruz","Av. Belgrano 2152","3876688241","matias@gmail.com",randint(0,10)],
["44212745","Francisco Gutierrez","12 de Octubre 1257","3875981283","francisco@gmail.com",randint(0,10)]
]

with open ("calificacionesV2.csv","w",newline="", encoding="utf-8") as file:                    # CREAR UN ARCHIVO CSV, y lo nombro como file
    titulo = "DNI,Nombre y Apellido,Direccion,Telefono,Correo electronico,Nota_parcial\n"       # DEFINO EL TITULO 
    file.write(titulo)                                                                          # ESCRIBO EL TITULO EN calificacionesV2.csv
    writer = csv.writer(file, delimiter = ",")                                                  # LE INDICO EL DELIMITADOR O SEPARADOR, QUE SERIA ","
    writer.writerows(alumnos)                                                                   # ESCRIBO TODA LA LISTA DE ALUMNOS EN calificacionesV2.csv, writerows = Nos coloca una lista abajo de la otra, writerow = nos coloca una lista al lado del otro




with open ("resumen.txt","w") as filee:
        with open ("calificacionesV2.csv","r") as file:
            resumen = "Resumen de notas primer parcial programacion II\n" 
            filee.write(resumen)


            

file.close()
filee.close()
print ("Escritura completa")

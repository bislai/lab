#!/usr/local/bin/bash

: '
Dependencias: jq - csvkit - sed(linux)
Script para consumir los datos de la API de Poletika.
La idea es generar un JSON de cada partido y tematica.
'



# Otro array con los nombres de partidos y tematicas normalizados sin acentos, espacios ni mayúsuculas
partidosre=('unidas-podemos' 'partido-socialista' 'ciudadanos' 'partido-popular')

# La ruta donde tenemos los archivos
pathPartidos="$(pwd)/partidos/"

# La urta donde los vamos a mover
github="$HOME/github/pqnvl/csv/"

for ((i = 0; i < ${#partidosre[@]}; i++)); do

    mv "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}"-total-propuestas.csv "$github""${partidosre[$i]}"/"${partidosre[$i]}"-total-propuestas.csv

done

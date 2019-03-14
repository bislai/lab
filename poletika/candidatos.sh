#!/usr/local/bin/bash

: '
Dependencias: jq
Para consumir los datos de la API de Poletika.
La idea es generar un JSON de cada partido y tematica.
'
# Array con la lista de partidos y tematicas
partidos=('Unidas Podemos' 'Partido Socialista' 'Ciudadanos' 'Partido Popular' 'Vox')
tematicas=('Empleo' 'Educación' 'Fiscalidad' 'Género' 'Protección social' 'Cambio climático' 'Calidad democrática' 'Desarrollo')

# Otro array con los nombres de partidos y tematicas normalizados sin acentos, espacios ni mayúsuculas
partidosre=('unidas-podemos' 'partido-socialista' 'ciudadanos' 'partido-popular')
tematicasre=('empleo' 'educacion' 'fiscalidad' 'enero' 'proteccion-social' 'cambio-climatico' 'calidad-democratica' 'desarrollo')

# Creamos un directorio donde almacenar los JSON de cada partido
mkdir partidos tematicas

# La ruta donde se alojarán todos los archivos
pathPartidos="$(pwd)/partidos/"
pathTematicas="$(pwd)/tematicas/"

for ((i = 0; i < ${#partidos[@]}; i++)); do

    curl -s https://data.what-politicians-say.poletika.org/json/ | jq -r "map(select(.party==\"${partidos[$i]}\"))" > "$pathPartidos""${partidosre[$i]}".json

done

for ((i = 0; i < ${#tematicas[@]}; i++)); do

    curl -s https://data.what-politicians-say.poletika.org/json/ | jq -r "map(select(.topic==\"${tematicas[$i]}\"))" > "$pathTematicas""${tematicasre[$i]}".json

done

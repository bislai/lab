#!/usr/local/bin/bash

: '
Dependencias: jq - csvkit - sed(linux)
Script para consumir los datos de la API de Poletika.
La idea es generar un JSON de cada partido y tematica.
'

# Array con la lista de partidos y tematicas
partidos=('Unidas Podemos' 'Partido Socialista' 'Ciudadanos' 'Partido Popular' 'Vox')
tematicas=('Calidad democrática' 'Cambio climático' 'Conflictos y migración' 'Desarrollo' 'Educación' 'Empleo' 'Fiscalidad' 'Género' 'Infancia' 'Protección social' 'Sanidad')

# Otro array con los nombres de partidos y tematicas normalizados sin acentos, espacios ni mayúsuculas
partidosre=('unidas-podemos' 'partido-socialista' 'ciudadanos' 'partido-popular')
tematicasre=('calidad-democratica' 'cambio-climatico' 'conflictos-y-migracion' 'desarrollo' 'educacion' 'empleo' 'fiscalidad' 'genero' 'infancia' 'proteccion-social' 'sanidad')

# Creamos un directorio donde almacenar los JSON de cada partido
mkdir partidos tematicas

# La ruta donde se alojarán todos los archivos
pathPartidos="$(pwd)/partidos/"
pathTematicas="$(pwd)/tematicas/"

for ((i = 0; i < ${#partidos[@]}; i++)); do

    # Si no existe la carpeta de cada partido la creamos
    if [[ ! -d "$pathPartidos""${partidosre[$i]}" ]] ; then
        mkdir "$pathPartidos""${partidosre[$i]}"
    fi

    # Nos descargamos el JSON y lo filtramos por partido
    # Esto nos genera un JSON para cada partido
    curl -s https://data.what-politicians-say.poletika.org/json/ | jq -r "map(select(.party==\"${partidos[$i]}\"))" > "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}".json

    # Generamos una variable por partido para usarla con JQ [movida disponible a partir de JQ 1.4]
    export party="${partidos[$i]}"

    # Ahora creamos un CSV solo con partido, tema y la fecha
    jq -r '["partido", "tema", "fecha"], (.[] | select(.party==env.party) | [.party, .topic, .date]) | @csv' "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}".json > "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}".csv

    # Eliminamos las comillas dobles, cortesía de mi TOC
    sed -i 's/\"//g' "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}".csv

    # Ahora vamos a contar el número de propuestas por tema
    for ((x = 0; x < ${#tematicas[@]}; x++)); do
        # Buscamos por propuesta y contamos el número de veces que han presentado una propuesta de ese tema
        # Lo guardamos en un temporal
        csvgrep -c tema -r "${tematicas[$x]}" "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}".csv | csvstat -c tema --count > "$pathPartidos""${partidosre[$i]}"/temp.csv

        # Ahora eliminamos el Row count que genera CSVKIT y los sustituimos por el título de la propuesta
        # Esto lo guardamos en el CSV que almacenara el total de todas las propuestas
        sed -e "s/Row count: /${tematicas[x]},/g" "$pathPartidos""${partidosre[$i]}"/temp.csv >> "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}"-total-propuestas.csv

        # Eliminamos el temporal
        rm "$pathPartidos""${partidosre[$i]}"/temp.csv
    done

    # Añadimos el header del CSV para identificar cada columna
    sed -i '1s/^/nombre,total\n/' "$pathPartidos""${partidosre[$i]}"/"${partidosre[$i]}"-total-propuestas.csv

done

for ((j = 0; j < ${#tematicas[@]}; j++)); do

    curl -s https://data.what-politicians-say.poletika.org/json/ | jq -r "map(select(.topic==\"${tematicas[$j]}\"))" > "$pathTematicas""${tematicasre[$j]}".json

done

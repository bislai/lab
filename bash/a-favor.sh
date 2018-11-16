#!/bin/bash

# Ciudadanos no esta en el script ya que al usar comilla simple para abreviar su nombre C'S esto solo da putos problemas

partidos=("PP" "ZEC" "PSOE" "CHA")

# Recorremos el array de numeros
for (( i=0; i<${#partidos[@]}; ++i )); do

        # Lo primero que hacemos es crear un JSON con los campos afavor, presentada y fecha.
        jq --raw-output ['.[] | {"afavor": .a_favor, "presentada": .presentada, "fecha": .fecha}'] mociones.json > a-favor-"${partidos[$i]}".json &&

        # Esto nos devuelve algunos resultados con null, estos resultados son aquellos de las mociones que se han votado por unanimidad. Así que ahora vamos a limpiarlos
        jq --raw-output ['.[] | select(.afavor!=null) | select(.afavor | contains("${partidos[$i]}"))'] a-favor-"${partidos[$i]}".json > limpiando-"${partidos[$i]}".json &&

        # Ahora vamos a eliminar las mociones que ha presentado CHA y obviamente se ha votado a sí misma.
        jq --raw-output ['.[]  | select(.presentada | contains("${partidos[$i]}") | not) '] limpiando-"${partidos[$i]}".json >> sin-"${partidos[$i]}".json &&

        # Y ahora que ya tenemos todo limpio no nos hace falta el campo de afavor, así que lo eliminamos
        jq --raw-output ['.[] | {"presentada": .presentada, "fecha": .fecha}'] sin-"${partidos[$i]}".json > legislatura-"${partidos[$i]}"-votos-a-favor.json &&

        # Por último transformamos el JSON a CSV
        json2csv -i legislatura-"${partidos[$i]}"-votos-a-favor.json -o legislatura-"${partidos[$i]}"-votos-a-favor.csv &&

        # Eliminamos las comillas de todo el CSV
        sed 's/\"//g' legislatura-"${partidos[$i]}"-votos-a-favor.csv &&

        # Eliminamos todos los archivos que hemos generado a excepción de los CSV y mociones.json
        find . -type f -not -name 'mociones.json' -not -name '*.csv' -delete

done

#!/bin/bash

# Ciudadanos no esta en el script ya que he usado la abreviación C'S que da problemas

partidos=("PP" "ZEC" "PSOE" "CHA")

# Recorremos el array de numeros
for (( i=0; i<${#partidos[@]}; ++i ));
        do

        # Lo primero que hacemos es crear un JSON con los campos afavor, presentada y fecha.
        jq --raw-output ['.[] | {"afavor": .a_favor, "presentada": .presentada, "fecha": .fecha}'] mociones.json > a-favor-"${partidos[$i]}".json &&

        # Esto nos devuelve algunos resultados con null, estos resultados son aquellos de las mociones que se han votado por unanimidad. Así que ahora vamos a limpiarlos
        jq --raw-output ['.[] | select(.afavor!=null) | select(.afavor | contains("'${partidos[$i]}'"))'] a-favor-"${partidos[$i]}".json > limpiando-"${partidos[$i]}".json &&

        # Ahora vamos a eliminar las mociones que ha presentado CHA y obviamente se ha votado a sí misma.
        jq --raw-output ['.[]  | select(.presentada | contains("'${partidos[$i]}'") | not) '] limpiando-"${partidos[$i]}".json >> sin-"${partidos[$i]}".json &&

        # Y ahora que ya tenemos todo limpio no nos hace falta el campo de afavor, así que lo eliminamos
        jq --raw-output ['.[] | {"presentada": .presentada, "fecha": .fecha}'] sin-"${partidos[$i]}".json > legislatura-"${partidos[$i]}"-votos-a-favor.json &&

        # Por último transformamos el JSON a CSV
        json2csv -i legislatura-"${partidos[$i]}"-votos-a-favor.json -o legislatura-"${partidos[$i]}"-votos-a-favor.csv &&

        # Eliminamos las comillas de todo el CSV
        sed -i 's/"//g' *.csv

        done &&

# Ahora vamos con ciudadanos
jq --raw-output ['.[] | {"afavor": .a_favor, "presentada": .presentada, "fecha": .fecha}'] mociones.json > a-favor-ciudadanos.json &&

# Eliminamos la molesta comilla p or nada
sed -i "s/'/ /g" a-favor-ciudadanos.json &&
# Ahora sustituimos la abreviatura por el nombre completo y el resto es igual
sed -i 's/C S/CIUDADANOS/g' a-favor-ciudadanos.json &&

# Esto nos devuelve algunos resultados con null, estos resultados son aquellos de las mociones que se han votado por unanimidad. Así que ahora vamos a limpiarlos
jq --raw-output ['.[] | select(.afavor!=null) | select(.afavor | contains("CIUDADANOS"))'] a-favor-ciudadanos.json > limpiando-ciudadanos.json &&

# Ahora vamos a eliminar las mociones que ha presentado CHA y obviamente se ha votado a sí misma.
jq --raw-output ['.[]  | select(.presentada | contains("CIUDADANOS") | not) '] limpiando-ciudadanos.json >> sin-ciudadanos.json &&

# Y ahora que ya tenemos todo limpio no nos hace falta el campo de afavor, así que lo eliminamos
jq --raw-output ['.[] | {"presentada": .presentada, "fecha": .fecha}'] sin-ciudadanos.json > legislatura-ciudadanos-votos-a-favor.json &&

# Por último transformamos el JSON a CSV
json2csv -i legislatura-ciudadanos-votos-a-favor.json -o legislatura-ciudadanos-votos-a-favor.csv &&

# Eliminamos las comillas de todo el CSV
sed -i 's/"//g' *.csv &&

# Eliminamos todos los archivos que hemos generado a excepción de los CSV y mociones.json
find . -type f -not -name 'mociones.json' -not -name '*.csv' -not -name '*.sh' -delete

#!/usr/local/bin/bash

: '
Dependencias: jq
Script para saber si Poletika ha actualizado su JSON
Vamos a comprobar la longitud de elementos de nuestro JSON contra el suyo
Si el suyo es mayor, obviamente es que han actualizado. Así que vamos a
ejecutar candidatos.sh para traernos todos los cambios. También vamos
a descargar la versión más actualizada y sustituirla por la que tenemos.
'

# Nuestro JSON
our=$(curl -s 'https://raw.githubusercontent.com/bislai/lab/0cfd954718069d80b1d5f836be1a61d25f4b4a00/poletika/poletika.json' | jq '. | length')

# Su JSON
your=$(curl -s 'https://data.what-politicians-say.poletika.org/json/' | jq '. | length')

if [ "$your" -gt "$our" ] ; then
    echo "Poletika ha actualizado candi-DATOS. Vamos a traernos los cambios."
    rm partidos tematicas
    bash candidatos.sh
    curl https://data.what-politicians-say.poletika.org/json/ --output temp.json &&
    rm poletika.json && mv temp.json poletika.json
else
    echo "No hay ninguna actualización disponible."
fi

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
our=$(curl -s 'https://raw.githubusercontent.com/bislai/lab/master/poletika/poletika.json' | jq '. | length')

# Su JSON
your=$(curl -s 'https://data.what-politicians-say.poletika.org/json/' | jq '. | length')

# Nos traemos la fecha para así actualizar el repositorio con la fecha del día de la actualización
fecha=$(date '+%Y-%m-%d')


if [ "$your" -gt "$our" ] ; then
    echo "Poletika ha actualizado candi-DATOS. Vamos a traernos los cambios."
    # Eliminamos los antiguos datasets
    rm -rf partidos tematicas

    # Lanzamos el script para generar los datasets
    bash candidatos.sh

    rm poletika.json
    # Actualizamos nuestro JSON para comparar en la siguiente actualización
    curl https://data.what-politicians-say.poletika.org/json/ --output poletika.json | jq '.'
    git add poletika.json
    git commit -m "update poletika API | date: '$fecha'"
    git push origin master
    echo "Actualizados los datos de Poletika. Vamos a mover los datasets a su ubicación."
    bash mv-datasets.sh

else
    echo "No hay ninguna actualización disponible."
fi

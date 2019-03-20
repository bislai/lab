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
    printf "🎉 \e[1m\e[32mPoletika ha actualizado candi-DATOS.\n\n\e[0m\e[92mVamos a traernos los cambios.\n"
    # Eliminamos los antiguos datasets
    rm -rf partidos tematicas &&

    # Lanzamos el script para generar los datasets
    bash candidatos.sh &&

    rm poletika.json &&
    # Actualizamos nuestro JSON para comparar en la siguiente actualización
    curl https://data.what-politicians-say.poletika.org/json/ --output poletika.json | jq '.' &&
    git add poletika.json partidos tematicas &&
    git commit -m "update poletika API and datasets | date: '$fecha'" &&
    git push origin master &&
    printf "✅ \e[1m\e[32mActualizados los datos de Poletika.\n\n🚀 \e[0mVamos a mover los datasets a su ubicación." &&
    bash mv-datasets.sh
else
    echo "No hay ninguna actualización disponible."
fi

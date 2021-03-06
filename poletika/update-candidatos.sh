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
fecha=$(date '+%d-%m-%Y')


if [ "$your" -gt "$our" ] ; then
    printf "🎉 \e[1m\e[32mPoletika ha actualizado candi-DATOS.\n\n\e[0m\e[92mVamos a traernos los cambios.\n"
    # Eliminamos los antiguos datasets
    rm -rf partidos tematicas &&

    # Lanzamos el script para generar los datasets
    bash candidatos.sh &&

    rm poletika.json &&
    # Actualizamos nuestro JSON para comparar en la siguiente actualización
    curl https://data.what-politicians-say.poletika.org/json/ --output poletika.json | jq '.' &&

    # Vamos a dejar todo subido a git para la próxima actualización
    git add poletika.json partidos tematicas &&
    git commit -m "update poletika API and datasets | date: '$fecha'" &&
    git push origin master &&
    printf "✅ \e[1m\e[32mActualizados los datos de Poletika.\n\n🚀 \e[0mVamos a mover los datasets a su ubicación." &&

    # Ejecutamos otro script para mover los nuevos datasets al repositorio que hace las gráficas
    bash mv-datasets.sh &&
    cd ~/github/pqnvl/ &&
    git add csv &&
    git commit -m "update datasets | date: '$fecha'" &&
    git push origin master &&
    now || exit &&
    t update "🎉 Visualización actualizada('$fecha') con la información de candi-DATOS. #PoletikaVigila ha recogido un total de $your compromisos  https://pqnvl.jorgeatgu.now.sh  (tweet automático)"
else
    echo "No hay ninguna actualización disponible."
fi

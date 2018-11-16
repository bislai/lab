#!/bin/bash

# Por desgracia la nomenclatura de las paginas de acuerdos y orden del día siguen una numeración que ellos entenderán.

# Friendly Reminder: los días posteriores a una moción la web no suele ir, el despliegue o lo que hagan la deja frita. Así que comprobamos que esta operativa

if curl -s --head  --request GET https://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias.htm | grep "200 OK" > /dev/null; then
    echo "
    \033[00;32mIt's a miracle! La web esta levantada vamos a scrapear\033[0m 🤓🤓
    "
    fecha=$1
    # Obtenemos la URL de las mociones y votaciones seleccionado como buenamente se puede
    votaciones=$(curl -s https://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias.htm | pup 'td[headers="fecha"]:contains("'${fecha}'") + td + td + td + td > a:first-child attr{href}')
    # Obtenemos la URL con los enlaces de todas las mociones seleccionado como buenamente se puede
    mociones=$(curl -s https://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias.htm | pup 'td[headers="fecha"]:contains("'${fecha}'") + td + td > a:first-child attr{href}')

    # El mes de la votación, esto simplemente es para añadir un nombre diferenciador y tener todo ordenado
    nombreMociones="${fecha}-lista-de-votaciones"
    nombreLinks="${fecha}-lista-de-enlaces"

    # Extrayendo el contenido y votaciones de las mociones. Lo guardamos en JSON
    curl -s  $votaciones | pup 'div#rscont > ul li json{}' > $nombreMociones.json &&

    # Extrayendo los links de las mociones. Lo guardamos en JSON.
    curl -s $mociones | pup 'div#rscont > ul li json{}' > $nombreLinks.json

else
   echo "\033[1;31mLa han vuelto a romper, si te corre prisa avisa a @zaragoza_es \033[0m"
fi

# Scraping

Scrapeando el HTML que contiene las mociones y los links de las mociones con PUP

La estructura HTML deja mucho que desear. No contiene clases ni identificadores lo cual genera un trabajo extra para scrapear, y un resultado pésimo a nivel visual para el usuario.

Lo primero es extraer las votaciones que están en acuerdos, y lo segundo es extraer los enlaces de las mociones completas que están en el orden del día.

Extrayendo el contenido y votaciones de las mociones.
```
curl -s https://www.zaragoza.es/sede/portal/organizacion/plenos/servicio/fehaciente/68342 | pup 'div#rscont > ul li' > $nombre.html
```

Extrayendo el contenido en formato JSON

```
cat $nombre.html | pup 'li json{}'
```

Extrayendo los enlaces que contienen las mociones completas. 

```
curl -s https://www.zaragoza.es/sede/portal/organizacion/plenos/servicio/fehaciente/68085 | pup 'div#rscont > ul li' > prueba.html
```


## Filtrando con jq

Queremos sacar por fecha los votos a favor(también en contra y abstención) que ha ido haciendo CHA(y el resto de partidos) a lo largo de la legislatura.

Todo lo que está a continuación se lanza con el script ```a-favor.sh```

Lo primero que hacemos es crear un JSON con los campos afavor, presentada y fecha.

```
jq --raw-output ['.[] | {"afavor": .a_favor, "presentada": .presentada, "fecha": .fecha}'] mociones.json > a-favor-chunta.json
```

Esto nos devuelve algunos resultados con null, estos resultados son aquellos de las mociones que se han votado por unanimidad. Así que ahora vamos a limpiarlos

```
jq --raw-output ['.[] | select(.afavor!=null) | select(.afavor | contains("CHA"))'] a-favor-chunta.json > limpiando-chunta.json
```

Ahora vamos a eliminar las mociones que ha presentado CHA y obviamente se ha votado a sí misma.

```
jq --raw-output ['.[]  | select(.presentada | contains("CHA") | not) '] limpiando-chunta.json >> sin-chunta.json
```

Y ahora que ya tenemos todo limpio no nos hace falta el campo de afavor, así que lo eliminamos

```
jq --raw-output ['.[] | {"presentada": .presentada, "fecha": .fecha}'] sin-chunta.json > legislatura-chunta-votos-a-favor.json
```

Por último transformamos el JSON a CSV

```
json2csv -i legislatura-chunta-votos-a-favor.json -o legislatura-chunta-votos-a-favor.csv
```

# Bislai scraping

Aquí todas las movidas para obtener los datos del Ayuntamiento de Zaragoza, y a partir de ellos generar múltiples estadísticas para las gráficas de [Bislai](https://bislai.co).

## Python

### Plenos

Si quieres tocar algo del scraper las dependecias se gestionan con pipenv. Lo primero hacemos un ```pipenv install``` para que funcione todo correctamente. 

Lanzamos el script con ```python mociones.py``` en mi caso lo lanzo con pipenv ```pipenv run python mociones.py``` 

<blockquote>
Como el comando es muy largo y no estamos para perder tiempo es recomendable hacerse un alias prp=pipenv run python
</blockquote>

El scraper espera tres parametros
- El primero la url de la moción que queremos obtener.
- El segundo el día que se celebro.
- El tercero el mes que se celebro.

Estos dos últimos parametros son para generar un nombre legible para el CSV.

Una vez lanzado obtenemos en un CSV:
 - El número de la moción
 - El partido que lo ha presentado
 - La url con la moción completa
 - El texto de cada moción

### Actas

Si quieres tocar algo del scraper las dependecias se gestionan con pipenv. Lo primero hacemos un ```pipenv install``` para que funcione todo correctamente. 

Lanzamos el script con ```python actas.py``` en mi caso lo lanzo con pipenv ```pipenv run python actas.py``` 

Con el script obtenemos todos los PDF de las actas de la última legislatura 2015-2018. Se puede modificar para obtener los de todos los años, hay que tener en cuenta que las actas solo están disponibles desde 2012.

Para modificar los años hay que añadir los diferentes años a la lista de URL:

```
list_url = [
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_17.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_16.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_15.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_14.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_13.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_12.htm']
```


Lanzando el script ```merge-actas.py``` generamos un único PDF de 11467 🤯 páginas con el nombre ```todas-las-actas-desde-2015-2019.pdf``` 

### Votaciones

En proceso...

Por ahora lo que hay no es suficiente ya que para las votaciones cada día emplean un termino diferente.

## Bash

El scraping con bash ya ha pasado a la historia. Aún así esta documentado todo el proceso en bash/commands.md


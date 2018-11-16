# scraping

Aquí todas las movidas para obtener los datos del Ayuntamiento de Zaragoza, y a partir de ellos generar múltiples estadísticas para las gráficas de @Bislai.


## Node + Lodash

Comprobar que la matriz que contiene todas las mociones esta actualizada en ```mociones/mociones.json``` Lanzamos lodash contra la matriz. Para ello hay un script de NPM que primero actualiza los objetos de los partidos y una vez actualizado contabiliza los diferentes archivos correspondientes a cada partido.

```
npm run data:bislai
```

Después de lanzar el script obtenemos para cada partido:

- Votos a favor del resto de partidos
- Votos en contra del resto de partidos
- Abstenciones
- Votos en su contra del resto de partidos
- Votos a favor del resto de partidos

Para las estadísticas generales obtenemos:

- ¿Quién vota a favor?
- ¿Quién vota en contra?
- ¿Quién se abstiene?
- Cuantás mociones se han presentado
- Resultado de las **votaciones**, no son mociones.
- Votaciones por unanimidad
- La soledad del pleno, aquellos partidos que votan solos ya se a favor, en contra o abstención.

## Bash

Documentado todo el proceso en bash/commands.md

## Python

**WIP**

Necesitamos pipenv para gestionar las dependencias de Python, por ahora solo request. Lanzamos el scraper con ```pipenv run python lurte.py```



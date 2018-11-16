var fs = require("fs");
var _ = require("lodash");

//Cargamos el total de todas las votaciones
data = JSON.parse(fs.readFileSync('pp/pp-total.json','utf8'));

//Obtenemos las votaciones donde el PP ha votado a favor y luego las filtramos por que partido la ha presentado
ppFavor = _.filter(data, function(res) { if (/PP/.test(res.a_favor)) return res.fecha });
ppFavor = _.countBy(ppFavor, function(res) { return (res.presentada) })

fs.writeFile('pp/pp-favor.json', JSON.stringify(ppFavor, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde el PP ha votado en contra y luego las filtramos por que partido la ha presentado
ppContra = _.filter(data, function(res) { if (/PP/.test(res.en_contra)) return res.fecha });
ppContra = _.countBy(ppContra, function(res) { return (res.presentada) })

fs.writeFile('pp/pp-contra.json', JSON.stringify(ppContra, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde el PP se ha abstenido y luego las filtramos por que partido la ha presentado
ppAbstencion = _.filter(data, function(res) { if (/PP/.test(res.abstencion)) return res.fecha });
ppAbstencion = _.countBy(ppAbstencion, function(res) { return (res.presentada) })

fs.writeFile('pp/pp-abstencion.json', JSON.stringify(ppAbstencion, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

// Sumando el total de los votos en contra de Chunta
function sum(obj) {
  var sum = 0;
  for( var el in obj ) {
    if( obj.hasOwnProperty( el ) ) {
      sum += parseFloat( obj[el] );
    }
  }
  return sum;
}

var ppContraTotal = "Las votaciones en contra suman: " + sum(ppContra);
var ppFavorTotal = 'Las votaciones a favor suman: ' + sum(ppFavor);
var ppAbstencionTotal = "Las abstenciones suman: " + sum(ppAbstencion);

//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('pp/pp-contra-total.json', JSON.stringify(ppContraTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('pp/pp-contra-total.json', JSON.stringify(ppFavorTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('pp/pp-contra-total.json', JSON.stringify(ppAbstencionTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

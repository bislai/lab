var fs = require("fs");
var _ = require("lodash");

//Cargamos el total de todas las votaciones
data = JSON.parse(fs.readFileSync('psoe/psoe-total.json','utf8'));

//Obtenemos las votaciones donde el PP ha votado a favor y luego las filtramos por que partido la ha presentado
psoeFavor = _.filter(data, function(res) { if (/PSOE/.test(res.a_favor)) return res.fecha });
psoeFavor = _.countBy(psoeFavor, function(res) { return (res.presentada) })

fs.writeFile('psoe/psoe-favor.json', JSON.stringify(psoeFavor, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde el psoe ha votado en contra y luego las filtramos por que partido la ha presentado
psoeContra = _.filter(data, function(res) { if (/PSOE/.test(res.en_contra)) return res.fecha });
console.log(psoeContra)
psoeContra = _.countBy(psoeContra, function(res) { return (res.presentada) })

fs.writeFile('psoe/psoe-contra.json', JSON.stringify(psoeContra, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde el psoe se ha abstenido y luego las filtramos por que partido la ha presentado
psoeAbstencion = _.filter(data, function(res) { if (/PSOE/.test(res.abstencion)) return res.fecha });
psoeAbstencion = _.countBy(psoeAbstencion, function(res) { return (res.presentada) })

fs.writeFile('psoe/psoe-abstencion.json', JSON.stringify(psoeAbstencion, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

// sumando el total de los votos en contra de Chunta
function sum(obj) {
  var sum = 0;
  for( var el in obj ) {
    if( obj.hasOwnProperty( el ) ) {
      sum += parseFloat( obj[el] );
    }
  }
  return sum;
}

var psoeContraTotal = "Las votaciones en contra suman: " + sum(psoeContra);
var psoeFavorTotal = 'Las votaciones a favor suman: ' + sum(psoeFavor);
var psoeAbstencionTotal = "Las abstenciones suman: " + sum(psoeAbstencion);

//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('psoe/psoe-contra-total.json', JSON.stringify(psoeContraTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('psoe/psoe-contra-total.json', JSON.stringify(psoeFavorTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('psoe/psoe-contra-total.json', JSON.stringify(psoeAbstencionTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

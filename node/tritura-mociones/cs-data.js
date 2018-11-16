var fs = require("fs");
var _ = require("lodash");

data = JSON.parse(fs.readFileSync('cs/cs-total.json','utf8'));

//Obtenemos las votaciones donde el PP ha votado a favor y luego las filtramos por que partido la ha presentado
csFavor = _.filter(data, function(res) { if (/C'S/.test(res.a_favor)) return res.fecha });
csFavor = _.countBy(csFavor, function(res) { return (res.presentada) })

fs.writeFile('cs/cs-favor.json', JSON.stringify(csFavor, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde el cs ha votado en contra y luego las filtramos por que partido la ha presentado
csContra = _.filter(data, function(res) { if (/C'S/.test(res.en_contra)) return res.fecha });
csContra = _.countBy(csContra, function(res) { return (res.presentada) })

fs.writeFile('cs/cs-contra.json', JSON.stringify(csContra, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde el cs se ha abstenido y luego las filtramos por que partido la ha presentado
csAbstencion = _.filter(data, function(res) { if (/C'S/.test(res.abstencion)) return res.fecha });
csAbstencion = _.countBy(csAbstencion, function(res) { return (res.presentada) })

fs.writeFile('cs/cs-abstencion.json', JSON.stringify(csAbstencion, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

//Sumando el total de los votos en contra de Chunta
function sum(obj) {
  var sum = 0;
  for( var el in obj ) {
    if( obj.hasOwnProperty( el ) ) {
      sum += parseFloat( obj[el] );
    }
  }
  return sum;
}

var csContraTotal = "Las votaciones en contra suman: " + sum(csContra);
var csFavorTotal = 'Las votaciones a favor suman: ' + sum(csFavor);
var csAbstencionTotal = "Las abstenciones suman: " + sum(csAbstencion);

//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('cs/cs-contra-total.json', JSON.stringify(csContraTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('cs/cs-contra-total.json', JSON.stringify(csFavorTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('cs/cs-contra-total.json', JSON.stringify(csAbstencionTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

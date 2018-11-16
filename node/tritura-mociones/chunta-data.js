var fs = require("fs");
var _ = require("lodash");

//Cargamos el total de todas las votaciones
data = JSON.parse(fs.readFileSync('cha/cha-total.json','utf8'));

//Obtenemos las votaciones donde Chunta ha votado a favor y luego las filtramos por que partido la ha presentado
chaFavor = _.filter(data, function(res) { if (/CHA/.test(res.a_favor)) return res.fecha });
chaFavor = _.countBy(chaFavor, function(res) { return (res.presentada) })

//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('cha/cha-favor.json', JSON.stringify(chaFavor, null, 2), 'utf8', function(err) {
    if (err) {
        throw err;
    }
});


//Obtenemos las votaciones donde Chunta ha votado en contra y luego las filtramos por que partido la ha presentado
chaContra = _.filter(data, function(res) { if (/CHA/.test(res.en_contra)) return res.fecha });
chaContra = _.countBy(chaContra, function(res) { return (res.presentada) })

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

//Obtenemos las votaciones donde Chunta se ha abstenido y luego las filtramos por que partido la ha presentado
chaAbstencion = _.filter(data, function(res) { if (/CHA/.test(res.abstencion)) return res.fecha });
chaAbstencion = _.countBy(chaAbstencion, function(res) { return (res.presentada) })

//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('cha/cha-abstencion.json', JSON.stringify(chaAbstencion, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

var chaContraTotal = "Las votaciones en contra suman: " + sum(chaContra);
var chaFavorTotal = 'Las votaciones a favor suman: ' + sum(chaFavor);
var chaAbstencionTotal = "Las abstenciones suman: " + sum(chaAbstencion);


//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('cha/cha-contra.json', JSON.stringify(chaContra, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

//Creamos un nuevo JSON con todos los datos filtrados
fs.writeFile('cha/cha-contra-total.json', JSON.stringify(chaContraTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('cha/cha-contra-total.json', JSON.stringify(chaFavorTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.appendFile('cha/cha-contra-total.json', JSON.stringify(chaAbstencionTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

var fs = require("fs");
var _ = require("lodash");

var mociones = require('./mociones/mociones.json');

var pp = "PP";
var zec = "ZEC";
var psoe = "PSOE";
var cs = "C'S'";
var cha = "CHA";


//Obtenemos las mociones y votaciones que ha presentado cada partido
ppMociones = _.filter(mociones, function(res) { if (res.presentada == pp) return res.fecha });
zecMociones = _.filter(mociones, function(res) { if (res.presentada == zec) return res.fecha });
psoeMociones = _.filter(mociones, function(res) { if (res.presentada == psoe) return res.fecha });
csMociones = _.filter(mociones, function(res) { if (res.presentada == cs) return res.fecha });
chaMociones = _.filter(mociones, function(res) { if (res.presentada == cha) return res.fecha });

//Obtenemos los votos que ha emitido cada partido: a favor, en contra y abstención
ppTotal = _.filter(mociones, function(res) { if (/PP/.test(res.a_favor) || /PP/.test(res.en_contra) || /PP/.test(res.abstencion)) return res.fecha });
zecTotal = _.filter(mociones, function(res) { if (/ZEC/.test(res.a_favor) || /ZEC/.test(res.en_contra) || /ZEC/.test(res.abstencion)) return res.fecha });
psoeTotal = _.filter(mociones, function(res) { if (/PSOE/.test(res.a_favor) || /PSOE/.test(res.en_contra) || /PSOE/.test(res.abstencion)) return res.fecha });
csTotal = _.filter(mociones, function(res) { if (/C'S/.test(res.a_favor) || /C'S/.test(res.en_contra) || /C'S/.test(res.abstencion)) return res.fecha });
chaTotal = _.filter(mociones, function(res) { if (/CHA/.test(res.a_favor) || /CHA/.test(res.en_contra) || /CHA/.test(res.abstencion)) return res.fecha });

//Obtenemos cuantas votaciones se han votado por unanimidad
//Obtenemos cuantas votaciones se han presentado
//Obtenemos quien ha emitido votos a favor, en contra o se ha abstenido
$afavor = _.countBy(mociones, function(res) { return (res.a_favor) })
$encontra = _.countBy(mociones, function(res) { return (res.en_contra) })
$unanimidad = _.countBy(mociones, function(res) { return (res.unanimidad) })
$presentada = _.countBy(mociones, function(res) { return (res.presentada) })
$abstencion = _.countBy(mociones, function(res) { return (res.abstencion) })
$resultado = _.countBy(mociones, function(res) { return (res.resultado) })

fs.writeFile('pp/pp-mociones.json', JSON.stringify(ppMociones, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('pp/pp-total.json', JSON.stringify(ppTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});


fs.writeFile('zec/zec-mociones.json', JSON.stringify(zecMociones, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('zec/zec-total.json', JSON.stringify(zecTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('psoe/psoe-mociones.json', JSON.stringify(psoeMociones, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('psoe/psoe-total.json', JSON.stringify(psoeTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('cs/cs-mociones.json', JSON.stringify(csMociones, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('cs/cs-total.json', JSON.stringify(csTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('cha/cha-mociones.json', JSON.stringify(chaMociones, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('cha/cha-total.json', JSON.stringify(chaTotal, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('estadisticas/a-favor.json', JSON.stringify($afavor, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('estadisticas/en-contra.json', JSON.stringify($encontra, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('estadisticas/unanimidad.json', JSON.stringify($unanimidad, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('estadisticas/presentada.json', JSON.stringify($presentada, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('estadisticas/resultado.json', JSON.stringify($resultado, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

fs.writeFile('estadisticas/abstencion.json', JSON.stringify($abstencion, null, 2), function(err) {
    if (err) {
        throw err;
    }
});

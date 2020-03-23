//executar no terminal  node convertJsontoCSV.js > empresas
/* 
    quando executar vai sobre escrever o arquivo esmpresas com os novos codigos
*/

'use strict';

const fs = require('fs');

let rawdata = fs.readFileSync('Jsons/TodasEmpresasTech.json');
let dados = JSON.parse(rawdata);
dados.finance.result[0].quotes.map(empresa => {
    console.log(empresa.shortName.replace(/,/g , '')+ "," + empresa.symbol);
})
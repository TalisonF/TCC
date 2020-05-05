//executar no terminal  node convertJsontoCSV.js > empresas
/* 
    quando executar vai sobre escrever o arquivo esmpresas com os novos codigos
*/

'use strict';
let all = [];
const fs = require('fs');
//Vai para 46 pq foi a quantidade de JSONS PEGADOS DA API DO YAHOO
for (let i = 1; i <= 46; i++) {
    let rawdata = fs.readFileSync(`downloads/${i}.json`);
    let dados = JSON.parse(rawdata);
    dados.finance.result[0].quotes.map(empresa => {
        //Tem alguns codigos errados por iss o try.
        try {
            console.log(empresa.shortName.replace(/[,.]/g, '') + "," + empresa.symbol);
            all.push({
                cod: empresa.symbol,
                nome: empresa.shortName,
            });
        } catch (e) {

        }
    })
}

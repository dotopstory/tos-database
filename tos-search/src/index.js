const fs = require('fs'),
      lunr = require('lunr'),
      openKoreanText = require('open-korean-text-node').default,
      papa = require('papaparse'),
      path = require('path')
;

// Add timestamp to logs
require('console-stamp')(console, 'yyyy-mm-dd HH:MM:ss');

require('../node_modules/lunr-languages/lunr.multi.js')(lunr);
require('../node_modules/lunr-languages/lunr.stemmer.support.js')(lunr);
require('../node_modules/lunr-languages/tinyseg.js')(lunr);
require('../node_modules/lunr-languages/lunr.jp.js')(lunr);
require('./lunr.kr.js')(lunr, openKoreanText);

function log(...msg) {
    console.log('[' + REGION + ']', '[tos-search]', ...msg);
}

const REGION_iTOS = 'iTOS';
const REGION_jTOS = 'jTOS';
const REGION_kTEST = 'kTEST';
const REGION_kTOS = 'kTOS';
const REGION_twTOS = 'twTOS';
const REGION = process.argv[2] || REGION_iTOS;

if ([REGION_iTOS, REGION_jTOS, REGION_kTOS, REGION_kTEST, REGION_twTOS].indexOf(REGION) === -1)
    throw Error('Invalid region: ' + REGION);

let documents = {};
let folder = path.join(__dirname, '..', '..', 'web', 'src', 'assets', 'data', REGION.toLowerCase());

// Load Documents
log('Loading documents...');
let files = fs.readdirSync(folder);
    files.forEach((fileName) => {
        if (fileName.indexOf('.csv') === -1)
            return;

        log('Papa parsing ' + fileName + '...');
        let dataset = fileName.slice(0, fileName.indexOf('.'));
        let file = fs.readFileSync(path.join(folder, fileName), 'utf8');

        documents[dataset] = [];

        papa.parse(file, { dynamicTyping: true, header: true, skipEmptyLines: true })
            .data
            .forEach((row) => documents[dataset].push(row));
    });

// Build index
log('Building index...');
var idx = lunr(function () {
    if (REGION === REGION_jTOS)
        this.use(lunr.multiLanguage('en', 'jp'));
    if (REGION === REGION_kTOS || REGION === REGION_kTEST)
        this.use(lunr.multiLanguage('en', 'kr'));

    // Disable stemmer
    this.pipeline.remove(lunr.stemmer);

    this.ref('$ID_lunr');
    this.field('$ID');
    this.field('$ID_NAME');
    this.field('Name');
    //this.field('Description');

    Object.entries(documents)
        .forEach(value => {
            let documents = value[1];
            let dataset = value[0];

            documents.forEach((doc) => {
                doc['$ID_lunr'] = dataset + '#' + doc['$ID'];
                this.add(doc)
            });
        })
});

// Save index
log('Saving Index...');
fs.writeFileSync(path.join(folder, 'index.json'), JSON.stringify(idx));

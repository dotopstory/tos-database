const childProcess = require('child_process');
const fs = require('fs');
const path = require('path');
const shared = require("./shared");

// Add timestamp to logs
require('console-stamp')(console, 'yyyy-mm-dd HH:MM:ss');

shared.singletonLock();

if (shared.IS_PROD) {
    // Update git repository
    shared.log('Updating git repository...');
    childProcess.execSync('git reset --hard HEAD');
    childProcess.execSync('git pull');

    // Update node projects
    shared.log('Updating node projects...');
    childProcess.execSync('npm install', { cwd: path.join('..', 'tos-html')});
    childProcess.execSync('npm install', { cwd: path.join('..', 'tos-ngsw')});
    childProcess.execSync('npm install', { cwd: path.join('..', 'tos-patreon')});
    childProcess.execSync('npm install', { cwd: path.join('..', 'tos-search')});
    childProcess.execSync('npm install', { cwd: path.join('..', 'tos-sitemap')});
    childProcess.execSync('npm install', { cwd: path.join('..', 'web')});
}

// Get current revision
shared.log('Loading current revision...');
let revision_path = path.join('revision.txt');
let revision = fs.existsSync(revision_path) ? fs.readFileSync('revision.txt', { encoding: 'utf8' }) : null;
let revision_new = childProcess.execSync('git rev-parse HEAD').toString();

console.log('+========================================================================+');
console.log('| Patching...                                                            |');
console.log('+========================================================================+');

let is_new_patch = false, is_new_revision = revision !== revision_new;
let argv, cwd, js, py, result;

for (let region of shared.REGIONS) {

    // 1. Patcher & parser
    shared.log(`[${ region }] 1. Patcher & parser`);
    cwd = path.join('..', 'tos-parser');
    py = path.join(cwd, 'src', 'main.py');

    result = childProcess.spawnSync(`python ${ py } ${ region } ${ is_new_revision }`, { cwd, shell: true, stdio: 'inherit' });
    result.status !== 0 && shared.logError('Failed to patch', result);

    // 2. Search index
    shared.log(`[${ region }] 2. Search index`);
    cwd = path.join('..', 'tos-search');
    js = path.join(cwd, 'src', 'index.js');

    result = childProcess.spawnSync(`node ${ js } ${ region }`, { cwd, shell: true, stdio: 'inherit' });
    result.status !== 0 && shared.logError('Failed to search', result);

    // 3. Sitemap
    shared.log(`[${ region }] 3. Sitemap`);
    cwd = path.join('..', 'tos-sitemap');
    js = path.join(cwd, 'src', 'index.js');

    result = childProcess.spawnSync(`node ${ js } ${ region }`, { cwd, shell: true, stdio: 'inherit' });
    result.status !== 0 && shared.logError('Failed to sitemap', result);

    // 4. Patreon
    shared.log(`[${ region }] 4. Patreon`);
    cwd = path.join('..', 'tos-patreon');
    js = path.join(cwd, 'src', 'index.js');

    result = childProcess.spawnSync(`node ${ js } ${ region }`, { cwd, shell: true, stdio: 'inherit' });
    result.status !== 0 && shared.logError('Failed to patreon', result);

    // 5. Commit changes
    let changes = childProcess.execSync('git status --porcelain', { encoding: 'utf8', shell: true }).toString();
    if (changes.split('\n').length > 1 && shared.IS_PROD) {
        shared.log(`[${ region }] 5. Commit changes`);
        cwd = path.join('..');

        result = childProcess.spawnSync(`git add .`, { cwd, shell: true, stdio: 'inherit' });
        result.status !== 0 && shared.logError('Failed to add', result);

        result = childProcess.spawnSync(`git commit -m "Updated ${ region } as of ${ new Date().toISOString().slice(0, 10) }"`, { cwd, shell: true, stdio: 'inherit' });
        result.status !== 0 && shared.logError('Failed to commit', result);

        result = childProcess.spawnSync(`git push`, { cwd, shell: true, stdio: 'inherit' });
        result.status !== 0 && shared.logError('Failed to push', result);

        is_new_patch = true;
    }

}

if (is_new_patch || is_new_revision || shared.IS_FORCE_DEPLOY) {
    console.log('+========================================================================+');
    console.log('| Deploying...                                                           |');
    console.log('+========================================================================+');

    // 6. Build & Deploy
    shared.log('6. Build & Deploy');
    argv = process.argv.slice(2).join(' ');
    cwd = path.join('.');
    js = path.join(cwd, 'src', 'deploy-web.js');

    result = childProcess.spawnSync(`node ${ js } ${ argv }`, { cwd, shell: true, stdio: 'inherit' });
    result.status !== 0 && shared.logError('Failed to build & deploy', result);

    // Update revision
    fs.writeFileSync(revision_path, childProcess.execSync('git rev-parse HEAD').toString());
} else {
    shared.log('No new patch nor revision available. No deployment is needed.');
}


shared.singletonUnlock();

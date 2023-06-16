import os
import shutil
import subprocess

os.environ['NODE_ENV'] = 'production'

os.chdir('./app')

subprocess.run(['npx', 'parcel', 'build', 'src/index.html', '--no-cache', '--no-source-maps'])

os.chdir('..')

if os.path.exists('./server/static'):
    shutil.rmtree('./server/static')

shutil.copytree('./app/dist', './server/static')
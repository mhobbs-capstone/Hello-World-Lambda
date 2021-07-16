import subprocess

install = 'python3 -m pip install virtualenv'
venv = 'python3 -m venv .venv'
source = 'bash --rcfile ".venv/bin/activate"'

subprocess.run(install,shell=True)
subprocess.run(venv,shell=True)
subprocess.run(source,shell=True)
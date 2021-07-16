import subprocess

update = 'sudo apt-get update'
upgrade = 'sudo apt-get upgrade -y'
serverlessinstall = 'npm install --user serverless'
serverless = 'cd .. && serverless'

subprocess.run(update,shell=True)
subprocess.run(upgrade,shell=True)
subprocess.run(serverlessinstall,shell=True)
subprocess.run(serverless,shell=True)
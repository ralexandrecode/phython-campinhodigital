import os
os.system("ls")

"""A lista completa de argumentos de subprocess.run() é semelhante a esta:

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)"""

import subprocess
subprocess.run(["ls","-l","README.md"])
print()
subprocess.run(["ls"])
print()
subprocess.run(["ls","-l"])

#INFORMAÇÕES SOBRE O SISTEMA:

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#ESPAÇO EM DISCO:

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


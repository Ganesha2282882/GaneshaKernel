from time import sleep
from os import listdir

errors = 0
print('Ganesha Kernel, A competitor to Linux Kernel.')

sleep(3)
print('\n' * 1000)
print('Starting up . . .')
if 'main.py' in listdir():
    print('It works!')

else:
    print('Kernel Panic: main.py not found')
    errors += 1

while True:
    print('Apps:\n{W}eb')
    app = input()
    if app == "W":
        import requests as req
        print(req.get(input("URL: ")).content)

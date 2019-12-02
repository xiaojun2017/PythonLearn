import sys
import os
import HelloWorld

print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe python path is: ', sys.path, '\n')

print(os.getcwd())

print("call hello world")
HelloWorld.HelloWorld()
print('hello world version:',HelloWorld.__version__)

print("_________dir_________")
dir(sys)

dir()
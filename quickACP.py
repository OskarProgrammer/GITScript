
from os import system,chdir,getcwd
import argparse
import sys
from colorama import Fore

"""
To use the full potential of the script, put the path to this .py file in your environment PATH.

Using the script:
if you have added python to PATH--> quickACP.py (ARGUMENTS)
if not --> python/python3 quickACP.py (ARGUMENTS)

Arguments:
-m --message Message to commit

-f --file Files to be committed

-c --check Check if the message and file arguments have been passed correctly (after the script exits)

-s --status Show the stages of the script in the console (start of specific commands/end of execution)

"""

parser = argparse.ArgumentParser(description="Quick pushing changes to GIT repo")

parser.add_argument("-m","--message",help="Message to commit",required=False,type=str,default="Default message")
parser.add_argument("-f","--file",help="Files to add to stage",required=False,type=str,default="*")
parser.add_argument("-c","--check",help="Check if arguments are passing correctly",required=False,type=str,default="False")
parser.add_argument("-s","--status",help="Check status of command in real time",required=False,type=str,default="False")

args = parser.parse_args()

class Pushing(object):
    def __init__(self, message, files):
        self._message = message
        self._files = files

        try:
            if args.status != "False":
                print(Fore.GREEN+f"Adding files {self._files}..."+Fore.RED)
                system(f"git add {self._files}")
                print(Fore.GREEN+f"Added files {self._files} successfully")
                
                print(Fore.GREEN+f"Committing with message {self._message}"+Fore.RED)
                system(f"git commit -m \"{self._message}\"")
                print(Fore.GREEN+f"Commited with message {self._message} succesfully")
                
                print(Fore.GREEN+f"Pushing changes to repo"+Fore.RED)
                system(f"git push origin")
                print(Fore.GREEN+f"Pushed changes to repo succesfully")

                print(Fore.WHITE+"Some information: ")
            else:
                system(f"git add {self._files}|git commit -m \"{self._message}\" | git push origin")
        except:
            print("No git repo/ No file .git/ Error during executing the script")

    def __str__(self):
        return f"Your message: {self._message}\nFiles: {self._files}"
        
obj = Pushing(args.message,args.file)
if args.check != "False":
    print(obj)
#!/bin/python
#"subprocess" is used for running shell commands.
#"os" provides a way of interacting with the operating system.
#"sys" is used for interacting with the Python interpreter.
import subprocess, os, sys

#Defining a list of strings that, if found in the command output, indicate an error.
#If you want to add more string at the end indent with ,
string = ["vol offline: entry doesn't exist", "There are no entries matching your query", "Error"]

#Opening the file named 'test.txt' in read mode, Please look at test.txt file for the formate.
#!!!If you already have ssh public key setup then just use "ssh" else have to pass "sshpass"
with open('test.txt') as f:
    for line in f:
        # Use shlex.split to safely split the command
        command = line.strip()
		#Using subprocess.Popen to execute the command in a new process.
		#Capturing both standard output (out) and standard error (err) streams.
        try:
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
        except Exception as e:
            print(f"Error executing command: {command}")
            print(f"Exception: {e}")
            sys.exit(1)
		
		#Checking if any of the error strings are present in the decoded standard output or standard error.
        if any(s in out.decode() for s in string) or any(s in err.decode() for s in string):
			#If an error is detected, printing the command, standard output, and standard error. Then, exiting the script with a status code of 1.
            print('xxxxxxxxxxxxxx- Something went wrong, check below command -xxxxxxxxxxxx')
            print(f"Command: {command}")
            print(f"STDOUT: {out.decode()}")
            print(f"STDERR: {err.decode()}")
            sys.exit(1)
		#If no errors are found, printing the command, standard output, and standard error.
        else:
            print(f"Command: {command}")
            print(f"STDOUT: {out.decode()}")
            print(f"STDERR: {err.decode()}")

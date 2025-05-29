import streamlit as st
import subprocess
import os

server_process = None
output_lines = []

def capture_server_output():
    global output_lines
    while True:
        line = server_process.stdout.readline().strip()
        if line == '[SUMMARY]':
            output_lines.append(line)
            break
        output_lines.append(line)

    while True:
        line = server_process.stdout.readline().strip()
        output_lines.append(line)
        if not line:
            break

    with open('output.txt', 'w') as f:
        f.write('\n'.join(output_lines))

    if server_process.returncode != 0:
        print("Error occurred:", server_process.stderr)
    else:
        print("Output saved to output.txt")

server_command = ['python', 'server.py']
server_process = subprocess.Popen(server_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

server_process.wait()

if server_process.poll() is None:
    capture_server_output()
else:
    print("Server process has terminated before capturing output.")

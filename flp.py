import subprocess
import os
import time

server_script_path = r"    " #path to save the output of server_script
client_script_path = r"    " #path to save the output of client_script
output_file_path = r"      "  # Full path to save the output of server.py

def run_script_in_terminal(script_path, output_file=None):
    if output_file:
        with open(output_file, "w") as f:
            subprocess.Popen(["start", "cmd", "/k", "python", script_path], stdout=f, stderr=f, shell=True)
    else:
        subprocess.Popen(["start", "cmd", "/k", "python", script_path], shell=True)

print("Starting server...")
run_script_in_terminal(server_script_path, output_file=output_file_path)
time.sleep(2)  

num_clients = 3  
print("Starting clients...")
for i in range(num_clients):
    print(f"Starting client {i+1}...")
    run_script_in_terminal(client_script_path)

print("All scripts started.")

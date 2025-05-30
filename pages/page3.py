from navigation import make_sidebar
import streamlit as st
from time import sleep
import subprocess

def slow_text(text, delay=1):
    st.text(text)
    sleep(delay)

make_sidebar()

st.markdown("# Model Training Control")

slow_text(" ")
slow_text("Setting up federated learning server...")
slow_text("Initializing clients...")
slow_text("Client 1 setup")
slow_text("Client 2 setup")
slow_text("Client 3 setup")

def run_flp_script():
    subprocess.Popen(["start", "cmd", "/k", "python", r"D:\Users\HP\Downloads\Test1\fl-ids-main (1)\fl-ids-main\flp.py"], shell=True)

if st.button("Start the Federated learning process"):
    run_flp_script()

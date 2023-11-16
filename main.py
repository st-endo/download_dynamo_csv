import time
import subprocess

while True:
    subprocess.run(["python", "download_csv.py"])
    time.sleep(60)

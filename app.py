from flask import Flask
import getpass
import subprocess
import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Baikunth Sharma"  
    username = getpass.getuser()
    
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # top output (only first few lines for brevity)
    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    return f"""
    <h1>System Monitor</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

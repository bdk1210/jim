from flask import Flask
from threading import Thread
import datetime

app = Flask('')

# Track last ping and bot start time
last_ping_time = None
start_time = datetime.datetime.now()

@app.route('/')
def home():
    global last_ping_time
    last_ping_time = datetime.datetime.now()
    return "jim: yo what's up gng"

@app.route('/status')
def status():
    now = datetime.datetime.now()
    uptime = now - start_time
    ping_info = f"Last UptimeRobot ping: {last_ping_time}" if last_ping_time else "No pings yet"
    return f"""
    <html>
    <head><title>Jim Status</title></head>
    <body>
        <h1>Status: Jim</h1>
        <p><strong>Started:</strong> {start_time}</p>
        <p><strong>Uptime:</strong> {uptime}</p>
        <p><strong>{ping_info}</strong></p>
    </body>
    </html>
    """

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

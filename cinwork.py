from flask import Flask, render_template
from flask_socketio import SocketIO
import psutil
import time
from scapy.all import sniff
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")



def owl_bandwidth():
    old_stats = psutil.net_io_counters()

    while True:
        time.sleep(1)
        new_stats = psutil.net_io_counters()

        upload_speed = (new_stats.bytes_sent - old_stats.bytes_sent) / 1024  # KB/s
        download_speed = (new_stats.bytes_recv - old_stats.bytes_recv) / 1024  # KB/s

        socketio.emit("bandwidth_update", {"upload": upload_speed, "download": download_speed})

        old_stats = new_stats

def packet_handler(packet):
    packet_info = packet.summary()
    socketio.emit("packet_update", {"packet": packet_info})

def start_sniffing():
    sniff(prn=packet_handler, store=False)

if __name__ == "__main__":
    threading.Thread(target=owl_bandwidth, daemon=True).start()
    threading.Thread(target=start_sniffing, daemon=True).start()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

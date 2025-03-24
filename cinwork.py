import eventlet
eventlet.monkey_patch()

import psutil
import time
from collections import Counter
from flask import Flask, render_template
from flask_socketio import SocketIO
from scapy.all import sniff, IP

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode="eventlet")

top_talkers = Counter()

@app.route("/")
def index():
    return render_template("index.html")

def owl_bandwidth():
    old_stats = psutil.net_io_counters()
    while True:
        socketio.sleep(1)
        new_stats = psutil.net_io_counters()
        upload_speed = (new_stats.bytes_sent - old_stats.bytes_sent) / 1024  # KB/s
        download_speed = (new_stats.bytes_recv - old_stats.bytes_recv) / 1024  # KB/s
        socketio.emit("bandwidth_update", {"upload": upload_speed, "download": download_speed})
        old_stats = new_stats

def packet_handler(packet):
    global top_talkers
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        top_talkers.update([src_ip, dst_ip])
        
        top_5_talkers = top_talkers.most_common(5)
        socketio.emit("top_talkers_update", {"top_talkers": top_5_talkers})
    
    packet_info = packet.summary()
    socketio.emit("packet_update", {"packet": packet_info})

def start_sniffing():
    sniff(prn=packet_handler, store=False)

if __name__ == "__main__":
    socketio.start_background_task(owl_bandwidth)
    socketio.start_background_task(start_sniffing)
    socketio.run(app, host="0.0.0.0", port=5000)
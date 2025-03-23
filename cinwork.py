import psutil
import time
from scapy.all import sniff
import threading

LOG_FILE = "network_log.txt"

def log_data(data):
    with open(LOG_FILE, "a") as f:
        f.write(data + "\n")

def owl_bandwidth(interval=1):
    print("Monitoring bandwidth usage...")
    old_stats = psutil.net_io_counters()

    while True:
        time.sleep(interval)
        new_stats = psutil.net_io_counters()

        bytes_sent = new_stats.bytes_sent - old_stats.bytes_sent
        bytes_recv = new_stats.bytes_recv - old_stats.bytes_recv

        log_entry = f"[Bandwidth] Upload: {bytes_sent / 1024:.2f} KB/s | Download: {bytes_recv / 1024:.2f} KB/s"
        print(log_entry)
        log_data(log_entry)

        old_stats = new_stats

def packet_handler(packet):
    log_entry = f"[Packet] {packet.summary()}"
    print(log_entry)
    log_data(log_entry)

def start_sniffing():
    print("Sniffing packets...")
    sniff(prn=packet_handler, store=False) 


threading.Thread(target=owl_bandwidth, daemon=True).start()

start_sniffing()

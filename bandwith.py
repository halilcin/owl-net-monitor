import psutil
import time

def owl_bandwith(interval=1):
    print("Monitoring bandwith usage... Use CTRL+C to stop")
    old_stats = psutil.net_io_counters()

    while True:
        time.sleep(interval)
        new_stats = psutil.net_io_counters()

        bytes_sent = new_stats.bytes_sent - old_stats.bytes_sent
        bytes_recv = new_stats.bytes_recv - old_stats.bytes_recv

        print(f"Upload: {bytes_sent / 1024:.2f} KB/s | Download: {bytes_recv / 1024:.2f} KB/s")

        old_stats = new_stats 

owl_bandwith()
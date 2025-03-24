# Owl-Net-Monitor

Owl-Net-Monitor is a simple network observation tool that provides real-time bandwidth monitoring and packet sniffing using Flask, Flask-SocketIO, and Scapy.

## Features
- **Real-time Bandwidth Monitoring**: Tracks upload and download speeds.
- **Packet Sniffing**: Captures and displays network packets.
- **Web Dashboard**: Displays network activity using Flask and SocketIO.
- **Docker Support**: Coming in next versions.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/halilcin/owl-net-monitor.git
cd owl-net-monitor
```

### 2. Install Dependencies
Ensure you have Python 3 installed, then run:
```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install eventlet flask flask-socketio psutil scapy
```

### 3. Running the Application
To start the app locally, run:
```bash
python3 cinwork.py
```
Access the web dashboard at [http://localhost:5000](http://localhost:5000).


## Notes
- **Run with root privileges** if using Scapy for packet sniffing.
- Flask-SocketIO uses **eventlet** for async background tasks.
- (For Future Versions)--Docker container needs **`NET_ADMIN`** capability for packet sniffing.

## License
MIT License. Feel free to modify and contribute!


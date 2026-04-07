import subprocess
import datetime
import requests
import os

# ---------------- Configuration ----------------
DEVICES = {
    "iPhone X": "10.0.3.90",
    "iPhone 14 Pro": "10.0.0.183",
    "Laptop": "10.0.0.12"
}

# New Log Path
LOG_DIR = r"C:\Users\Mojalefa\Downloads\hub\Log"
LOG_FILE = os.path.join(LOG_DIR, "network_monitor_log.txt")

# Telegram
BOT_TOKEN = "Place Your Bot Token Here"
CHAT_ID = "Place Your Chat_ID here"

# ---------------- Functions ----------------

def ensure_log_directory():
    """Creates the log directory if it doesn't exist."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log(message):
    """Writes to file and prints to console."""
    ensure_log_directory()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{log_entry}\n")
    print(log_entry)

def ping_device(ip):
    """Pings a device and returns True if reachable."""
    try:
        # -n 1: one packet, -w 1000: 1 second timeout
        output = subprocess.run(["ping", "-n", "1", "-w", "1000", ip], capture_output=True)
        return output.returncode == 0
    except Exception as e:
        log(f"Ping Error for {ip}: {e}")
        return False

def send_telegram(message):
    """Sends notification to Telegram and logs the result."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        response = requests.get(url, params={"chat_id": CHAT_ID, "text": message}, timeout=10)
        if response.status_code == 200:
            log(f"Telegram notification sent successfully.")
        else:
            log(f"Telegram failed with status code: {response.status_code}")
    except Exception as e:
        log(f"Telegram Error: {e}")

# ---------------- Main Script ----------------

def main():
    log("--- Starting Scheduled Network Scan ---")
    
    for name, ip in DEVICES.items():
        is_online = ping_device(ip)
        status = "ONLINE" if is_online else "OFFLINE"
        emoji = "✅" if is_online else "⚠️"
        
        # Log the local result
        log(f"Device Check: {name} ({ip}) is {status}")

        # Send the Telegram alert
        telegram_msg = f"{emoji} MONITOR: {name} ({ip}) is {status}"
        send_telegram(telegram_msg)
    
    log("--- Scan Complete ---")

if __name__ == "__main__":
    main()
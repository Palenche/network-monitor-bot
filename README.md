A Python-based network monitoring system that tracks device availability on a local network and sends real-time alerts via Telegram.

🚀 Features:
- Monitors multiple devices via IP (Ping-based)
- Logs device status (ONLINE / OFFLINE)
- Sends real-time Telegram alerts when devices go offline
- Runs automatically using Windows Task Scheduler
- Designed for home lab / small network environments

📡 Devices Monitored:
- iPhone X
- iPhone 14 Pro
- Laptop

🛠️ Technologies Used:
- Python
- Requests (Telegram API)
- Windows Task Scheduler

⚙️ How It Works:
1. The script pings each device using its IP address
2. Logs results with timestamps
3. Sends Telegram alerts if a device is offline

📦 Setup:
1. Install Python
2. Install dependencies:
   pip install requests
3. Add your Telegram Bot Token and Chat ID in the script
4. Run:
   python centralHub.py

📌 Notes:
- Logs are stored locally and excluded from GitHub using .gitignore
- Ensure devices have static IPs for accurate monitoring

💡 Future Improvements:
- Smart alerting (avoid duplicate alerts)
- Detect full network outages
- Cloud logging (AWS S3 / CloudWatch)
- Bandwidth monitoring per device

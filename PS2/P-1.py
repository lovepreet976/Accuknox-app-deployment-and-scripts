import psutil
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

def system_health_monitor():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"[{timestamp}] ALERT: High CPU usage: {cpu_usage}%")

    # Memory Usage
    mem = psutil.virtual_memory()
    if mem.percent > MEM_THRESHOLD:
        print(f"[{timestamp}] ALERT: High Memory usage: {mem.percent}%")

    # Disk Usage (C: drive)
    disk = psutil.disk_usage('C:\\')
    if disk.percent > DISK_THRESHOLD:
        print(f"[{timestamp}] ALERT: High Disk usage: {disk.percent}%")

    # Running Processes
    processes = len(psutil.pids())
    print(f"[{timestamp}] Total running processes: {processes}")

if __name__ == "__main__":
    system_health_monitor()

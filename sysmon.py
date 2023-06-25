import psutil

#CPU Usage 

cpu_percent = psutil.cpu_percent(interval=1) #CPU Usage in Percentage
print(f"CPU Usage: {cpu_percent}%")

#Memory Usage 

mem = psutil.virtual_memory()
total_memory = mem.total / 1024 ** 3 
available_memory = mem.available / 1024 ** 3
used_memory = mem.used / 1024 ** 3 
memory_percent = mem.percent 
print(f"Total Memory: {total_memory}GB")
print(f"Available Memory: {available_memory}GB")
print(f"Used Memory: {used_memory}GB")
print(f"Memory Usage: {memory_percent}%")


#Disk Usage 

disk = psutil.disk_usage('/')
total_disk_space = disk.total / 1024 ** 3
used_disk_space = disk.used / 1024 ** 3 
free_disk_space = disk.free / 1024 ** 3
disk_percent = disk.percent / 1024 ** 3 
print(f"Total Disk Space: {total_disk_space}GB")
print(f"Used Disk Space: {used_disk_space}GB")
print(f"Free Disk Space: {free_disk_space}GB")
print(f"Disk Usage: {disk_percent}%")

#Network Usage 

net_io = psutil.net_io_counters()
bytes_sent = net_io.bytes_sent / (1024 ** 2)
bytes_received = net_io.bytes_recv / (1024 ** 2)
print(f"Bytes Sent: {bytes_sent}MB")
print(f"Bytes Received: {bytes_received}MB")

#Run this program in the terminal with the command "python sysmon.py" you will see the cpu usage and memory in the terminal  
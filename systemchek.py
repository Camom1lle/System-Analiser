import psutil
import platform
from datetime import datetime
from colorama import init, Fore
from rich.progress import track
from time import sleep
import time

# def process_data():
#     sleep(0.02)
start_time = time.time()

init(autoreset=False)
# for _ in track(range(100), description='[green]Processing data'):
#     process_data()


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print(Fore.BLUE + "="*40, Fore.CYAN + "System Information", Fore.BLUE + "="*40)



uname = platform.uname()

print( Fore.GREEN + '\n')
def process_data():
    sleep(0.00002)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

print( Fore.BLUE + '\n')

print("="*40, Fore.CYAN + "Boot Time", Fore.BLUE + "="*40)

def process_data():
    sleep(0.00002)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
print( Fore.BLUE + '\n')
print("="*40, Fore.CYAN +  "CPU Info",  Fore.BLUE + "="*40)
# number of cores
print( Fore.GREEN + '\n')

def process_data():
    sleep(0.00002)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
print( Fore.BLUE + '\n')
print("="*40, Fore.CYAN + "Memory Information", Fore.BLUE + "="*40)
print( Fore.GREEN + '\n')

def process_data():
    sleep(0.00002)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")
print( Fore.BLUE + '\n')
print("="*40, Fore.CYAN + "Disk Information", Fore.BLUE + "="*40)
print( Fore.GREEN + '\n')

def process_data():
    sleep(0.00002)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")
print( Fore.BLUE + '\n')
print("="*40, Fore.CYAN + "Network Information", Fore.BLUE + "="*40)
print( Fore.GREEN + '\n')

def process_data():
    sleep(0.00002)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

quitaccess=str(input())
if quitaccess=='q':
    print("--- %s seconds ---" % (time.time() - start_time))
    time.sleep(3)
else:
    quit
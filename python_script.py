import platform
import socket
import psutil
import os
import speedtest
import uuid

def get_installed_software():
    software_list = os.popen('wmic product get name').read()
    return software_list

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000  # in Mbps
    return download_speed, upload_speed

def get_system_resolution():
    try:
        from win32api import GetSystemMetrics
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        return f"{width}x{height}"
    except ImportError:
        return "Unable to fetch resolution on non-Windows systems"

def get_cpu_info():
    cpu_info = platform.processor()
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    return cpu_info, cores, threads

def get_gpu_info():
    try:
        import GPUtil
        gpu_info = GPUtil.getGPUs()[0].name
        return gpu_info
    except ImportError:
        return "GPUtil module not available"

def get_ram_size():
    ram_info = psutil.virtual_memory().total / (1024**3)  # in GB
    return ram_info

def get_screen_size():
    return "15 inch"  # You might need a platform-specific library for accurate screen size

def get_network_info():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2,7)][::-1])
    ip_address = socket.gethostbyname(socket.gethostname())
    return mac_address, ip_address

def get_windows_version():
    return platform.version()

if __name__ == "__main__":
    if platform.system().lower() == 'windows':
        installed_software = get_installed_software()
        print("Installed Software:\n", installed_software)

        download_speed, upload_speed = get_internet_speed()
        print(f"Internet Speed: Download - {download_speed:.2f} Mbps, Upload - {upload_speed:.2f} Mbps")

        resolution = get_system_resolution()
        print("Screen Resolution:", resolution)

        cpu_info, cores, threads = get_cpu_info()
        print("CPU Model:", cpu_info)
        print("Number of Cores:", cores)
        print("Number of Threads:", threads)

        gpu_info = get_gpu_info()
        print("GPU Model:", gpu_info)

        ram_size = get_ram_size()
        print(f"RAM Size: {ram_size:.2f} GB")

        screen_size = get_screen_size()
        print("Screen Size:", screen_size)

        mac_address, ip_address = get_network_info()
        print("Network MAC Address:", mac_address)
        print("Public IP Address:", ip_address)

        windows_version = get_windows_version()
        print("Windows Version:", windows_version)
    else:
        print("This script is intended to be run on Windows Command Prompt.")

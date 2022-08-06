import psutil
import platform
from datetime import datetime
import platform

from numpy.distutils.cpuinfo import cpuinfo


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


print("=" * 40, "System Information", "=" * 40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

for cpu in cpuinfo.Win32CPUInfo():
    print("您的CPU序列号为:" + cpu.ProcessorId.strip())

    print("您的CPU名称为:" + cpu.Name)

    print("您的CPU已使用:%d%%" % cpu.LoadPercentage)

    print("您的CPU核心数为:%d" % cpu.NumberOfCores)

    print("您的CPU时钟频率为:%d" % cpu.MaxClockSpeed)

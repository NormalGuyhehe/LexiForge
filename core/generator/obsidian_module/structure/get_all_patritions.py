import psutil
from functools import lru_cache

@lru_cache
def get_mount_points():
    return [p.mountpoint for p in psutil.disk_partitions() if 'rw' in p.opts]
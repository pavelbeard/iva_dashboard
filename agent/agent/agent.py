import asyncio
import json
import logging
import os
import shutil
import subprocess


def get_disk_usage():
    # disk usage
    total, used, free = shutil.disk_usage('/')

    # read/write
    read_write = [x.strip() for x in subprocess.run(
        'vmstat;-D'.split(';'), stdout=subprocess.PIPE
    ).stdout.decode('utf-8').split('\n') if x.__contains__('total reads') or x.__contains__('writes')][:-1]

    total_reads = read_write[0].split()[0]
    total_writes = read_write[1].split()[0]

    logging.info(f'{get_disk_usage.__name__} works normally')

    return json.dumps(
        {
            'total': round(total / 1024 ** 3, 1),
            'used': round(used / 1024 ** 3, 1),
            'free': round(free / 1024 ** 3, 1),
            'r/w': {
                'total_reads': total_reads,
                'total_writes': total_writes,
            },
        }
    )


def get_ram_usage(output_type: int = 1):
    # mem usage

    if output_type == 1:
        filters = 'total memory;used memory;active memory;inactive memory;free memory'.split(';')
        vmstat_s = [x.strip()
                    for x in subprocess.run('vmstat;-s'.split(';'),
                                            stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
                    if any(s in x for s in filters)
                    ]

        total, used, active, inactive, free = [x.split()[0] for x in vmstat_s]

        logging.info(f'{get_ram_usage.__name__} works normally')

        return json.dumps({
            'total memory': round(int(total) / (10**6), 1),
            'used memory': round(int(used) / (10**6), 1),
            'active memory': round(int(active) / (10**6), 1),
            'inactive memory': round(int(inactive) / (10**6), 1),
            'free memory': round(int(free) / (10**6), 1),
        })

    elif output_type == 2:
        free_h__giga = [x.split()
                        for x in subprocess.run('free;-h;--giga'.split(';'),
                                                stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')][1]

        total, used, free, *available = [x for x in free_h__giga[1:]]

        logging.info(f'{get_ram_usage.__name__} works normally')

        return json.dumps({
            'total': total,
            'used': used,
            'free': free,
            'available': available[-1],
        })


def get_cpu_usage():
    """
    Gathering info about logical and physical cores
    :return: str
    """
    cpu_count = os.cpu_count()
    cpu_load = [x / cpu_count * 100 for x in os.getloadavg()]

    logging.info(f'{get_cpu_usage.__name__} works normally')

    return json.dumps({
        'cpu_count': cpu_count,
        'cpu_load': cpu_load
    })



import asyncio
import logging
import os

from agent import get_disk_usage, get_ram_usage, get_cpu_usage
from agent import send_data


def setup_logger():
    log_dir = os.path.join(os.getcwd(), 'log')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    logging.basicConfig(
        filename=os.path.join(log_dir, 'agent.log'), level=logging.INFO, filemode='a',
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    logger = logging.getLogger(__name__)


if __name__ == '__main__':
    setup_logger()

    tasks = (
        (get_disk_usage, '/api/disk'),
        (get_ram_usage, '/api/ram', 1),
        (get_cpu_usage, '/api/cpu'),
        # network interfaces
    )

    asyncio.run(send_data(url='http://localhost:8000', data=tasks))

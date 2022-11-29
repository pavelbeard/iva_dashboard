import asyncio
import concurrent.futures
import json
import unittest
from typing import Coroutine, Any

from .agent import get_cpu_usage, get_ram_usage, get_disk_usage


def coro(name):
    return json.dumps({name: "test"})


class CoroTests(unittest.TestCase):
    def test_coroutines(self):
        result = get_ram_usage(1)
        self.assertEqual(type(result), type(Coroutine[Any, Any, str]))

    def test_coroutines_2(self):
        r = coro()
        self.assertEqual(r, type(Coroutine))

    def test_run_in_executor(self):
        async def run_in_exec():
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(executor, coro, "test")
            print(result)

        asyncio.run(run_in_exec())


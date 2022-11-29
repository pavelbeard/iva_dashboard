import ast
import asyncio
import concurrent.futures
import json
import logging
import time
import urllib.request
from typing import Any, Callable
from urllib.error import HTTPError, URLError


def request(url: str, method: str, data: bytes = None) -> str | None:
    rq = urllib.request.Request(
        url, data, method=method, headers={
            'Content-Type': 'application/json; charset=utf-8'
        }
    )

    response = None
    try:
        with urllib.request.urlopen(rq) as rs:
            response = bytes.decode(rs.read(), encoding='utf-8')
            
    except URLError as err:
        logging.error("URLError", exc_info=True)
        return None
    except HTTPError as err:
        logging.error("HTTPError", exc_info=True)
        return None
    except TimeoutError as err:
        logging.error("TimeoutError", exc_info=True)
        return None
    finally:
        logging.info(f'{request.__name__} works normally')
        return response


async def send_data(url: str, data: tuple, interval: int = 5):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    loop = asyncio.get_event_loop()

    while True:
        for func, api_route, *args in data:
            coro_result = await loop.run_in_executor(executor, func) if len(args) == 0 else await loop.run_in_executor(
                executor, func, *args
            )
            json_data = json.dumps(ast.literal_eval(coro_result)).encode('utf-8')
            response_api = await loop.run_in_executor(executor, request, url + api_route, 'POST', json_data)
            logging.info(response_api)

        response_interval = await loop.run_in_executor(executor, request, url + '/api/settings', 'GET')
        interval = ast.literal_eval(response_interval).get('interval')
        logging.info(response_interval)

        await asyncio.sleep(int(interval))

from concurrent.futures import ThreadPoolExecutor
import requests
import time

baseUrl = "http://127.0.0.1:8000"

def make_request(endpoint: str):
    return requests.post(f"{baseUrl}/{endpoint}", json={"question": "What is interface segregation?"})

start_time = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(make_request, "ask-async") for _ in range(5)]
    results = [f.result() for f in futures]
    end_time = time.time()

print(f"{end_time - start_time} seconds")
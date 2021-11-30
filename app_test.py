import pytest
import requests
from time import time


URL = 'http://localhost:5000'

def test_calc_route_success():
    req = requests.get(f'{URL}/?numbers=1,2,3')
    assert req.status_code == 200
    assert req.text == 'La moyenne de 1+2+3 est 2.0'

def test_calc_stress():
    exec_times = []
    for i in range(1000):
        start = time()
        requests.get(f'{URL}/?numbers=1,2,3')
        end = time()
        exec_times.append(((end - start)*1000))
    assert len(exec_times) == 1000
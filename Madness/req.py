#!/usr/bin/env python3

import requests

MAX = 99

IP = "10.10.254.50"

print("=====Find==The==Secret=====")
for p in range(1, MAX + 1) :
    url =f"http://{IP}/th1s_1s_h1dd3n/index.php?secret={p}"
    req = requests.get(url)
    if "That is wrong!" not in req.text :
        print(f"[+] found at : {url}")



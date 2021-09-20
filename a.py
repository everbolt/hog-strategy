import http.client
import json
PLAYER_NAME = "computer go brrrr"
m = None
def final_strategy(s, o):
    global m
    if not m:
        m = g()
    return m[min(s, 49)][min(o, 49)]
def g():
    c = http.client.HTTPSConnection("pastebin.com")
    c.request("GET", "/raw/NndHMn9W")
    r = c.getresponse()
    d = r.read().decode()
    return json.loads(d)["m"]
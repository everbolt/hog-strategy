import http.client
import json
PLAYER_NAME='computer go brrrr'
m=0
def final_strategy(s,o):
 global m
 if not m:
  c=http.client.HTTPSConnection("pastebin.com")
  c.request("GET","/raw/bdzRqwG1") #NndHMn9W is final #bdzRqwG1 is buffer
  m=json.loads(c.getresponse().read().decode())["m"]
 return m[min(s,49)][min(o,49)]
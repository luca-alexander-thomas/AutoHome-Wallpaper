import json
import os
import sys
import time

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) # {"name": "John", "age": 30, "city": "New York"}


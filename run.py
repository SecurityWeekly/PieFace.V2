#!venv/bin/python
from app import app
import platform

print("You are running " + platform.system())
if platform.system() == 'Linux':
    app.run('localhost', 5001, debug=True)
else:
    app.run('0.0.0.0', 5001, debug=True)

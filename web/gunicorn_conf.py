import multiprocessing

name = "flask_gunicorn"
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = "debug"
bind = f"0.0.0.0:18080"


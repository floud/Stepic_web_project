mport multiprocessing;

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
pythonpath = "/home/box/web/etc/"

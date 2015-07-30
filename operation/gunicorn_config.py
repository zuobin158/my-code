import multiprocessing
BASE_PATH = '/var/log/operation/'
bind = "0.0.0.0:7778"
pythonpath = "/edx/app/edxapp/cms"
workers = multiprocessing.cpu_count()

max_requests = 5

user = 'root'
group = 'root'

accesslog = BASE_PATH + 'gunicorn_access.log'
errorlog = BASE_PATH + 'gunicorn_error.log'
chdir = BASE_PATH

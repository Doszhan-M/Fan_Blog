command = 'gunicorn'
pythonpath = '/home/linux/github/Fan_Blog/ad_board'
bind = '127.0.0.1:8001'
workers = 3
user = 'linux'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=ad_board.settings'

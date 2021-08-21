# import os
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
#
# log_path = os.path.join(BASE_DIR, 'logs')
# log_file = os.path.join(log_path, 'app.log')
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     # 'formatters': {
#     #     'color': {
#     #         '()': 'colorlog.ColoredFormatter',
#     #         'format': '%(log_color)s%(levelname)-8s %(message)s',
#     #         'log_colors': {
#     #             'DEBUG':    'bold_black',
#     #             'INFO':     'white',
#     #             'WARNING':  'yellow',
#     #             'ERROR':    'red',
#     #             'CRITICAL': 'bold_red',
#     #         },
#     #     }
#     # },
#     'handlers': {
#         # Include the default Django email handler for errors
#         # This is what you'd get without configuring logging at all.
#         'mail_admins': {
#             'class': 'django.utils.log.AdminEmailHandler',
#             'level': 'ERROR',
#             # But the emails are plain text by default - HTML is nicer
#             'include_html': True,
#         },
#         # Log to a text file that can be rotated by logrotate
#         'logfile': {
#             'class': 'logging.handlers.WatchedFileHandler',
#             'filename': log_file,
#         },
#     },
#     'loggers': {
#         # Again, default Django configuration to email unhandled exceptions
#         'django.template': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         # Might as well log any errors anywhere else in Django
#         'django': {
#             'handlers': ['logfile'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         # Your own app - this assumes all your logger names start with "myapp."
#         'myapp': {
#             'handlers': ['logfile'],
#             'level': 'WARNING',  # Or maybe INFO or DEBUG
#             'propagate': False,
#         },
#         # 'django.db.backends': {
#         #     # django also has database level logging
#         #     'handlers': ['logfile'],
#         #     'level': 'DEBUG',
#         # },
#     },
# }

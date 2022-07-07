from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_delete, post_init, post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# ******Create a simple signal*******

# Connect signal with decorater easy way
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('------------------------')
    print('Logged-in Signal... run Intro...')
    print('Sender: ', sender)
    print('Request: ', request)
    print('User: ', user)
    print(f'Kwargs: {kwargs}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
# user_logged_in.connect(login_success, sender=User)

# -----------------------------------------------------------------------

# Connect signal with decorater easy way
@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print('------------------------')
    print('Logged-out Signal... run Outro...')
    print('Sender: ', sender)
    print('Request: ', request)
    print('User: ', user)
    print(f'Kwargs: {kwargs}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
# user_logged_out.connect(log_out, sender=User)


# -----------------------------------------------------------------------

# Connect signal with decorater easy way
@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print('------------------------')
    print('Login Failed Signal... run Outro...')
    print('Sender: ', sender)
    print('credentials: ', credentials)
    print('Request: ', request)
    print(f'Kwargs: {kwargs}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
# user_login_failed.connect(login_failed, sender=User)


# _____----__________----_______----_____----

"""
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, created, **kwargs):
    if created:
        print('------------------------')
        print('New Record...')
        print('Post Save Signal...')
        print('Sender: ', sender)
        print('Instance: ', instance)
        print('Createed: ', created)
        print(f'Kwargs: {kwargs}')
    else:
        print('------------------------')
        print('Update...')
        print('Post Save Signal...')
        print('Sender: ', sender)
        print('Instance: ', instance)
        print('Createed: ', created)
        print(f'Kwargs: {kwargs}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
# pre_save.connect(at_beginning_save, sender=User)
"""
# --------------------------

"""
# @receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print('Pre Delete Signal Delete...')
    print('Sender: ', sender)
    print('Instance: ', instance)
    print(f'Kwargs: {kwargs}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
pre_delete.connect(at_beginning_delete, sender=User)
"""

# --------------------------

"""
@receiver(pre_init, sender=User)
def at_beginning_pre_init(sender, *args, **kwargs):
    print('Pre Init Signal...')
    print('Sender: ', sender)
    print(f'Kwargs: {kwargs}')
    print(f'Kwargs: {args}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
# pre_init.connect(at_beginning_pre_init, sender=User)
"""
# --------------------------

"""
@receiver(post_init, sender=User)
def at_beginning_post_init(sender, *args, **kwargs):
    print('Post Init  Signal...')
    print('Sender: ', sender)
    print(f'Kwargs: {kwargs}')
    print(f'Kwargs: {args}')

    # ********Connect signel with recever********

# if connect signal with decorater dont use this code
# post_init.connect(at_beginning_post_init, sender=User)
"""

# -----------------Django Request - Built in signal----------------

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('At Beginning Request...')
    print('Sender: ', sender)
    print('Environ: ', environ)
    print(f'Kwargs: {kwargs}')
    # request_started.connect(at_beginning_request, sender=User)


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('At Ending Request...')
    print('Sender: ', sender)
    print(f'Kwargs: {kwargs}')
    # request_finished.connect(at_ending_request, sender=User)


# Use [ /home ] url in browser for test this exception signal code, wrote the code in views.py for exception
@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print('At Request Exception...')
    print('Sender: ', sender)
    print('Request: ', request)
    print(f'Kwargs: {kwargs}')
    # request_finished.connect(at_req_exception, sender=User)

# ______________________________________

@receiver(connection_created)
def connection_database(sender, connection, **kwargs):
    print('----------___--------____----------')
    print('Initial Connection to the Database...')
    print('Sender: ', sender)
    print('Connection: ', connection)
    print(f'Kwargs: {kwargs}')
    # connection_created.connect(connection_database, sender=User)
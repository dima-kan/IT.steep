import time
from settings import settings

while True:
    time.sleep(1)

    print(settings.app_name)
    print(settings.filename)
    print(settings.login)
    print(settings.password)
    print()

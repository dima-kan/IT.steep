import time
from settings import settings


while True:
    time.sleep(1)

    print(settings.password)
    print(settings.secret_text)
    print(settings.min_num)
    print(settings.max_num)

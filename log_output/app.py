import random
import string
import time
from datetime import datetime


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    random_str = generate_random_string(10)

    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
        print(f"{timestamp}: {random_str}", flush=True)
        time.sleep(5)

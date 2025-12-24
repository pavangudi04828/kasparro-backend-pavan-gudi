import time

def retry(func, retries=3):
    for _ in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(2)
    return None

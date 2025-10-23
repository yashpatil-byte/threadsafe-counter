import threading
import time

def worker():
    print("Thread starting")
    time.sleep(1)
    print("Thread done")

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads: t.start()
for t in threads: t.join()

print("All threads completed")

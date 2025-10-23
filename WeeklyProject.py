import threading, time

counter = 0
lock = threading.Lock()

def increment(thread_id):
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
    with open("log.txt", "a") as f:
        f.write(f"Thread {thread_id} finished\n")

threads = [threading.Thread(target=increment, args=(i,)) for i in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]

print("Final counter:", counter)
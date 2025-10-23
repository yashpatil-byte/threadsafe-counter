# 🧵 Thread-Safe Counter

A simple Python project demonstrating **multithreading**, **race conditions**, and how to fix them using `threading.Lock()`.

---

## 💡 Overview

When multiple threads modify the same variable simultaneously, **race conditions** can occur — leading to unpredictable results.  
This project shows how to safely update shared data using Python’s built-in locking mechanism.

---

## 🧠 What It Does

- Spawns multiple threads that increment a shared counter.  
- Demonstrates how **race conditions** cause incorrect results.  
- Fixes the issue using **locks** to ensure only one thread modifies the counter at a time.  
- Logs the completion of each thread to a file (`log.txt`).

---

## 🧩 Code Example

```python
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

⚙️ How to Run
Clone the repo
   git clone https://github.com/yashpatil-byte/threadsafe-counter.git
   cd threadsafe-counter
Run the Python script
   python3 WeeklyProject.py
Check the log file
   cat log.txt

🔒 Why Locks Are Important
Python threads share the same memory space.
Without synchronization, two threads may try to update the same variable at once.
Using a lock ensures that:
One thread acquires exclusive access before modifying shared data.
Others wait until the lock is released.
This prevents data corruption and ensures thread safety.

📚 What I Learned
Difference between multithreading and multiprocessing
What the GIL (Global Interpreter Lock) is and why it matters
How to use locks to prevent race conditions
How to use thread joins and logging to track execution

🚀 Future Improvements
Add a version using multiprocessing for performance comparison
Visualize thread execution time using timestamps
Add unit tests for verifying correctness

🧑‍💻 Author
Yash Patil
📍 Northeastern University, Boston
🔗 LinkedIn | GitHub (in my main yashpatil-byte)

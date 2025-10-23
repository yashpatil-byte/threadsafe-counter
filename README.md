# 🧮 Thread-Safe Counter

A simple Python project demonstrating **multithreading**, **race conditions**, and how to fix them using **threading.Lock()**.

---

## 🧠 What It Does
This program launches 5 threads that increment a shared counter variable 100,000 times each (total expected = 500,000).  
Without proper synchronization, threads overwrite each other's updates, leading to incorrect results.  
Using a `Lock` ensures that only one thread modifies the counter at a time.

---

## ⚙️ How It Works
- **Threading:** Creates multiple threads running the same `increment()` function.
- **Critical Section:** The `with lock:` block allows only one thread at a time to update `counter`.
- **Race Condition Prevention:** The lock enforces mutual exclusion.
- **Logging:** Each thread writes a message to `log.txt` when it finishes.

---

## 🧩 Run It

```bash
python3 counter.py

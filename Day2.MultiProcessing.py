import multiprocessing, time

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")

if __name__ == "__main__":
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)
    p1.start(); p2.start()
    p1.join(); p2.join()
    print(f"Finished in {round(time.perf_counter() - start, 2)} seconds")

# Objective: To copy a file's content to another, measure performance and understand buffering.
import time
start = time.perf_counter()
with open("input.txt", "rb") as src, open("output.txt", "wb") as dest:
    while chunk := src.read(1024*1024):
        dest.write(chunk) # read 1MB at a time

end = time.perf_counter()
print(f'Completed in {round(end - start)} seconds')
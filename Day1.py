import sys
import dis

def add(x, y):
    return x + y

print(dis.dis(add))
print(sys.getsizeof(1000000))

# output:
# yashpatil@YASHs-MacBook-Air SDE - 6mo % /opt/homebrew/bin/python3 "/Users/yashpatil/Desktop/SDE - 6mo/Day1.py"
 # 4           RESUME                   0

#. 5           LOAD_FAST_LOAD_FAST      1 (x, y)
#              BINARY_OP                0 (+)
#             RETURN_VALUE
# None
# 28
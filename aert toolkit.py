import sys

# --- PART A: Stack ADT Implementation ---
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x) [cite: 55]

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() [cite: 56]
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1] [cite: 57]
        return None

    def is_empty(self):
        return len(self.stack) == 0 [cite: 58]

    def size(self):
        return len(self.stack) [cite: 59]

# Global counters for Fibonacci analysis
naive_calls = 0
memo_calls = 0
memo = {}

# --- PART B: Factorial & Fibonacci ---
def factorial(n):
    if n < 0:
        return "Error: Negative input" [cite: 71, 151]
    if n == 0 or n == 1:
        return 1 [cite: 72]
    return n * factorial(n - 1) [cite: 69, 70]

def fib_naive(n):
    global naive_calls
    naive_calls += 1 [cite: 81, 82]
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2) [cite: 75]

def fib_memo(n):
    global memo_calls
    memo_calls += 1 [cite: 81, 83]
    if n in memo:
        return memo[n] [cite: 76]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2) [cite: 76]
    return memo[n]

# --- PART C: Tower of Hanoi ---
hanoi_stack = StackADT() # Using StackADT to store move descriptions [cite: 63, 65]

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move) [cite: 100]
        hanoi_stack.push(move)
        return
    hanoi(n - 1, source, destination, auxiliary) [cite: 93]
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    hanoi_stack.push(move)
    hanoi(n - 1, auxiliary, source, destination) [cite: 93]

# --- PART D: Recursive Binary Search ---
search_mids = StackADT() # Using StackADT to track visited midpoints [cite: 66]

def binary_search(arr, key, low, high):
    if low > high:
        return -1 [cite: 115]
    
    mid = (low + high) // 2
    search_mids.push(mid) [cite: 66]
    
    if arr[mid] == key:
        return mid [cite: 115]
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1) [cite: 113, 114]
    else:
        return binary_search(arr, key, mid + 1, high) [cite: 113, 114]

# --- Main Execution / Test Cases ---
def main():
    print("--- PART B: Factorial & Fibonacci ---")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}): {factorial(n)}") [cite: 89]
    
    print("\nFibonacci Comparison:")
    for n in [5, 10, 20, 30]: [cite: 90]
        global naive_calls, memo_calls, memo
        naive_calls = 0
        memo_calls = 0
        memo = {}
        res_n = fib_naive(n)
        res_m = fib_memo(n)
        print(f"n={n} | Result: {res_m} | Naive Calls: {naive_calls} | Memo Calls: {memo_calls}") [cite: 90]

    print("\n--- PART C: Tower of Hanoi (N=3) ---")
    hanoi(3, 'A', 'B', 'C') [cite: 94, 99]

    print("\n--- PART D: Binary Search ---")
    test_arr = [1, 3, 5, 7, 9, 11, 13]
    for k in [7, 1, 13, 2]: [cite: 123]
        idx = binary_search(test_arr, k, 0, len(test_arr)-1)
        print(f"Search {k} in {test_arr}: Index {idx}")
    
    print(f"Search in empty list []: {binary_search([], 5, 0, -1)}") [cite: 124]

if __name__ == "__main__":
    main()
# aert_toolkit.py

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Global counters and dictionary for Fibonacci
naive_calls = 0
memo_calls = 0
memo = {}

def factorial(n):
    if n < 0:
        return "Error: Negative input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

# Using Stack to store Hanoi moves
hanoi_moves = StackADT()

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        hanoi_moves.push(move)
        return
    hanoi(n - 1, source, destination, auxiliary)
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    hanoi_moves.push(move)
    hanoi(n - 1, auxiliary, source, destination)

def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

def main():
    print("--- PART B: Factorial & Fibonacci ---")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}): {factorial(n)}")
    
    print("\nFibonacci Comparison:")
    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls, memo
        naive_calls = 0
        memo_calls = 0
        memo = {}
        res_m = fib_memo(n)
        res_n = fib_naive(n)
        print(f"n={n} | Result: {res_m} | Naive Calls: {naive_calls} | Memo Calls: {memo_calls}")

    print("\n--- PART C: Tower of Hanoi (N=3) ---")
    hanoi(3, 'A', 'B', 'C')

    print("\n--- PART D: Binary Search ---")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for k in [7, 1, 13, 2]:
        idx = binary_search(arr, k, 0, len(arr) - 1)
        print(f"Search {k} in {arr}: Index {idx}")
    
    # Edge case: empty list
    empty_arr = []
    idx_empty = binary_search(empty_arr, 5, 0, -1)
    print(f"Search in empty list []: Index {idx_empty}")

if __name__ == "__main__":
    main()

import random
import string
import time
def simulate_stock_data(num_stocks=1000):
    stocks = []
    symbols = set()
    while len(stocks) < num_stocks:
        symbol = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 4)))
        if symbol in symbols:
            continue
        symbols.add(symbol)
        open_price = round(random.uniform(10, 1000), 2)
        change = random.uniform(-0.15, 0.15)  # -15% to +15%
        close_price = round(open_price * (1 + change), 2)
        stocks.append({
            'symbol': symbol,
            'open': open_price,
            'close': close_price
        })
    return stocks
def percentage_change(stock):
    return ((stock['close'] - stock['open']) / stock['open']) * 100
def heapify(arr, n, i, key_func):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and key_func(arr[l]) > key_func(arr[largest]):
        largest = l
    if r < n and key_func(arr[r]) > key_func(arr[largest]):
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key_func)
def heap_sort(arr, key_func):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key_func)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key_func)
    arr.reverse()
def build_stock_hashmap(stocks):
    return {stock['symbol']: stock for stock in stocks}
def search_stock(hashmap, symbol):
    return hashmap.get(symbol)
def print_stock(stock):
    if stock:
        print(f"Symbol: {stock['symbol']}, Open: {stock['open']:.2f}, Close: {stock['close']:.2f}, Change: {percentage_change(stock):.2f}%")
    else:
        print("Stock not found.")
def main():
    print("Welcome to the SRU FinTech Lab Stock Analyzer!")
    try:
        num_stocks = int(input("Enter number of stocks to simulate (e.g. 1000): "))
        if num_stocks < 1:
            print("Number of stocks must be at least 1. Using 1000 as default.")
            num_stocks = 1000
    except Exception:
        print("Invalid input. Using 1000 stocks as default.")
        num_stocks = 1000
    stocks = simulate_stock_data(num_stocks)
    print(f"Simulated {len(stocks)} stocks.")
    # Sorting with Heap Sort
    stocks_for_heap = stocks.copy()
    start = time.time()
    heap_sort(stocks_for_heap, key_func=percentage_change)
    heap_time = time.time() - start
    print(f"\nTop 5 gainers (Heap Sort):")
    for stock in stocks_for_heap[-5:][::-1]:
        print_stock(stock)
    print(f"Heap Sort Time: {heap_time:.6f} seconds")
    # Sorting with built-in sorted()
    start = time.time()
    stocks_sorted = sorted(stocks, key=percentage_change, reverse=True)
    sorted_time = time.time() - start
    print(f"\nTop 5 gainers (sorted()):")
    for stock in stocks_sorted[:5]:
        print_stock(stock)
    print(f"Built-in sorted() Time: {sorted_time:.6f} seconds")
    # Build hash map for searching
    start = time.time()
    stock_map = build_stock_hashmap(stocks)
    hash_build_time = time.time() - start
    print(f"\nHash map built in {hash_build_time:.6f} seconds.")
    # User-driven search loop (limit to 10 searches to prevent infinite loop)
    print("\nYou can now search for stock symbols. Type 'exit' to quit.")
    search_count = 0
    max_searches = 10
    while search_count < max_searches:
        symbol = input("Enter stock symbol to search: ").strip().upper()
        if symbol == 'EXIT':
            print("Exiting search.")
            break
        if not symbol:
            print("Please enter a stock symbol.")
            continue
        # Hash map search
        start = time.time()
        stock = search_stock(stock_map, symbol)
        hash_search_time = time.time() - start
        print_stock(stock)
        print(f"Hash map search time: {hash_search_time:.8f} seconds")
        # Linear search for comparison
        def linear_search(stocks, symbol):
            for stock in stocks:
                if stock['symbol'] == symbol:
                    return stock
            return None
        start = time.time()
        stock_linear = linear_search(stocks, symbol)
        linear_search_time = time.time() - start
        print(f"Linear search time: {linear_search_time:.8f} seconds")
        search_count += 1
    if search_count >= max_searches:
        print(f"\nMaximum number of searches ({max_searches}) reached. Exiting search.")
    print("\n--- Efficiency Analysis ---")
    print(f"Heap Sort is O(n log n), but slower than built-in sorted() (Timsort) for Python lists.")
    print(f"Hash map (dict) lookup is O(1) average, much faster than linear search (O(n)).")
    print(f"For large datasets, using built-in sorted() and dict is recommended for both speed and code simplicity.")
if __name__ == "__main__":
    main()



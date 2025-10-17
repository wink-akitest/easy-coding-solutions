# This function generates the Fibonacci sequence up to n terms.
# The sequence starts with 0 and 1, then each subsequent number
# is the sum of the previous two.

def fibonacci(n):
    # Generate Fibonacci sequence up to the nth term
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Example usage
if __name__ == "__main__":
    terms = 10
    print(f"Fibonacci sequence ({terms} terms):", fibonacci(terms))
  
git add python/beginner/fibonacci.py
git commit -m "Add beginner-level Fibonacci sequence solution"
git push origin main

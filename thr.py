import threading
import time

def greet(name):
    print(f"Started greeting {name}")
    time.sleep(2)  # Simulate some delay
    print(f"Hello, {name}!")

# Create threads
thread1 = threading.Thread(target=greet, args=("Alice",))
thread2 = threading.Thread(target=greet, args=("Bob",))

# Start threads
thread1.start()
thread2.start()

# Wait for both to complete
thread1.join()
thread2.join()

print("Finished all greetings.")

import queue
import threading
import time 

def main():
    filename = "message.txt"

    q = queue.Queue()

    producer_thread = threading.Thread(target=producer, args=(filename, q))
    producer_thread.start()

    consumer(q)

    producer_thread.join()


def producer(fileName, queue):
    with open(fileName, "r") as file:
        for line in file:
            queue.put(line.strip())
            time.sleep(0.1)
    queue.put(None)

def consumer(queue):
    while True:
        line = queue.get()
        if line is None:
            break
        print("Processed: ", line)

if __name__ == "__main__":
    main()

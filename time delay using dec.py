import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("time taken:{}".format(end - start))
        return result
    return wrapper
@timer
def slow():
    time.sleep(5)
    print("slow")
slow()

import time


def measure_time(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Computation took {end_time - start_time:.3f} seconds")
        return result

    return wrapper

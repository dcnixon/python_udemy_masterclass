import time

print(time.get_clock_info("monotonic"))
print(time.get_clock_info("perf_counter"))
print(time.get_clock_info("process_time"))
print(time.get_clock_info("thread_time"))
print(time.get_clock_info("time"))
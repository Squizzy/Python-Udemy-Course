import time
# from time import time as my_timer  # using time
# from time import perf_counter as my_timer  # using a counter, more precise and not subject to time changes
from time import monotonic as my_timer  # with this time cannot go backwards,
                                        # # wont be affected by time saving and computer clock adjustment
from time import process_time as my_timer  # uses the process / CPU used - useful for profiling code - also monotonic

import random

input("Press enter to start")

wait_time = random.randint(1, 6)

time.sleep(wait_time)
start_time = my_timer()

input("press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds!".format(end_time - start_time))

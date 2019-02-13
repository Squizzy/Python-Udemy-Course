# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

# a.append(time.get_clock_info('time'))
#
# a.append(time.get_clock_info('perf_counter'))
#
# a.append(time.get_clock_info('monotonic'))
#
# a.append(time.get_clock_info('process_time'))
#
# for i in range(0, 4):
#     adj, impl, mono, reso = a[i]
#     print("adjustable: {}\timplementation: {}\t monotonic: {}\t resolution: {}".format(adj, impl, mono, reso))

sClock = ['time', 'perf_counter', 'monotonic', 'process_time']

for i in range(4):
    a = time.get_clock_info(sClock[i])
#    print(a)
#    adj, impl, mono = time.get_clock_info('time')
    print("Name: {:10}\tadjustable: {}\timplementation: {:25}\t monotonic: {}\t resolution: {}".format(sClock[i], a.adjustable, a.implementation, a.monotonic, a.resolution))


import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
print(tz_to_display)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# Printing all the TZ available
for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])

for x in sorted(pytz.country_names):
    # fails as no TZ defined for BV
    # print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))

    # get will return non if non def
    # get returns non if no key defined in the dictionary
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
        print(pytz.country_timezones[x])
    else:
        print("\t\tNo timezone defined...")

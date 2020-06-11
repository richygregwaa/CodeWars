# My solution
def format_duration(seconds):
    intervals = (
        ('years', 31536000),  # 86400 * 365
        ('days', 86400),  # 60 * 60 * 24
        ('hours', 3600),  # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )

    result = []
    interval_type = 0

    for name, count in intervals:
        value = seconds // count
        if value:
            interval_type += 1
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))

    result = ', '.join(result)
    if interval_type > 1:
        last_char_index = result.rfind(",")
        result = result[:last_char_index] + " and" + result[last_char_index + 1:]
    return result or 'now'







# Alternative Solution 1
times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration1(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


# Alternative Solution 2
def format_duration2(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'



# Method I googled which has a really cool way of using granularity. I could use a lot!
def format_duration9(seconds, granularity=2):
    intervals = (
        ('years', 31536000),  # 86400 * 365
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),  # 60 * 60 * 24
        ('hours', 3600),  # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )

    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])


print(format_duration(3662))
print(format_duration2(3662))
print(format_duration(31536000+604800))
print(format_duration2(31536000+604800))
print(format_duration(31449601))
print(format_duration2(31449601))
print(format_duration(31449601+86399)) #3153600
print(format_duration2(31449601+86399)) #3153600
print(format_duration(31449601+86398))
print(format_duration2(31449601+86398))





# test.assert_equals(format_duration(120), "2 minutes")
# test.assert_equals(format_duration(3600), "1 hour")
# test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")



# test.assert_equals(format_duration(1), "1 second")
# test.assert_equals(format_duration(62), "1 minute and 2 seconds")
# test.assert_equals(format_duration(120), "2 minutes")
# test.assert_equals(format_duration(3600), "1 hour")
# test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
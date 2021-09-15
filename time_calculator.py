def add_time(start, duration, day_week=None):

    # timestamp start
    hour_start = int(start[ : start.find(':')])
    min_start = int(start[start.find(':') + 1 : start.find(':') + 3])
    meridiem = start[-2:]
    #print(hour_start, min_start, meridiem)
    hours_start = 0
    hours_start = 0 if meridiem == 'AM' and hour_start == 12 else hour_start if meridiem == 'AM' and hour_start != 12 else hour_start + 12
    timestamp_start = hours_start * 60 + min_start
    # timestamp end
    hours_duration = int(duration[ : duration.find(':')])
    min_duration = int(duration[duration.find(':') + 1 : duration.find(':') + 3])
    timestamp_end = timestamp_start + hours_duration * 60 + min_duration
    # new time
    new_time = ''
    new_hours = timestamp_end // 60
    new_min = timestamp_end - new_hours * 60
    days_later = timestamp_end // (60 * 24)
    new_hour24 = new_hours % 24
    new_hour12 = 12 if new_hour24 == 0 else new_hour24 if new_hour24 <= 12 else new_hour24 - 12
    new_meridiem = 'AM' if new_hour24 < 12 else 'PM'
    text_h = str(new_hour12)
    text_min = str(new_min) if new_min > 9 else '0' + str(new_min)
    text_days = ' (' + str(days_later) + ' days later)' if days_later != 1 else ' (next day)'
    if not day_week and not days_later:
        new_time = text_h + ':' + text_min + ' ' + new_meridiem
    elif not day_week:
        new_time = text_h + ':' + text_min + ' ' + new_meridiem + text_days
    else:
        text_week = ''
        week1 = {
            'sunday': 0,
            'monday': 1,
            'tuesday': 2,
            'wednesday': 3,
            'thursday': 4,
            'friday': 5,
            'saturday': 6,
            }
        week2 = {
            0: 'Sunday',
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            }
        new_num_day = (week1[day_week.lower()] + days_later) % 7
        new_day = week2[new_num_day]
        new_time = text_h + ':' + text_min + ' ' + new_meridiem + ', ' + new_day
        if days_later:
            new_time += text_days
            
    return new_time

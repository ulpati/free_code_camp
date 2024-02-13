def add_time(start, duration, start_day=None):
	# splitting the start time into its components
	start_time, period = start.split()
	start_hour, start_minute = map(int, start_time.split(':'))
	period = period.upper()

	# parsing the duration
	duration_hour, duration_minute = map(int, duration.split(":"))

	# converting start time to 24-hour format
	if period == 'PM':
		start_hour += 12

	# adding the duration
	new_hour = start_hour + duration_hour
	new_minute = start_minute + duration_minute

	# handling extra minutes
	new_hour += new_minute // 60
	new_minute %= 60

	# handling extra hours (convert to 12-hour clock)
	days_passed, new_hour = divmod(new_hour, 24)

	# converting back to 12-hour clock format
	new_period = 'AM' if new_hour < 12 else 'PM'
	new_hour = new_hour % 12 or 12

	# determine the day of the week
	days_of_week = [
		"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
		"Sunday"
	]
	if start_day:
		start_day = start_day.capitalize()
		day_index = days_of_week.index(start_day)
		new_day_index = (day_index + days_passed) % 7
		new_day = days_of_week[new_day_index]
		new_time = f"{new_hour}:{new_minute:02d} {new_period}, {new_day}"
	else:
		new_time = f"{new_hour}:{new_minute:02d} {new_period}"

	# handling days later
	if days_passed == 1:
		new_time += " (next day)"
	elif days_passed > 1:
		new_time += f" ({days_passed} days later)"

	return new_time
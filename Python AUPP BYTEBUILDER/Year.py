
# minutes=int(input("Enter the number of minutes:"))
# hours=minutes/60
# days=hours/24
# years=days/365
# print(f"{minutes} minutes is approxiamtely {round(years)} years and {round(days)} days")
minutes = int(input("Enter the number of minutes: "))

# Calculate total days from minutes
total_days = minutes / (60 * 24)

# Get years and remaining days
years = total_days /365
remaining_days = total_days % 365

# Output result
print(f"{minutes} minutes is approximately {years} years and {remaining_days} days")

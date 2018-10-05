import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'

# Get dates, high, and low temperatures from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows, avg = [], [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
            # avg.append(int(row[2]))
        except ValueError:
            print(current_date, "Missing Data")
        else:
            dates.append(current_date)
            highs.append(int(row[1]))
            lows.append(int(row[3]))


# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.4)
# plt.plot(dates, avg, c='green')

# Format plot
plt.title("Daily High Temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

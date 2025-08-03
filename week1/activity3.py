import numpy as np


def calcualte_rainfaill(input):
    weekDays = np.array(
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
    )
    total = sum(input)
    average = np.mean(input)
    zeroRain = np.array(np.where(input > 0)).size
    moreThan5 = np.array([weekDays[i] for i in np.where(input > 5)[0]])
    percentile = np.percentile(input, 75)

    return total, average, zeroRain, moreThan5, percentile


if __name__ == "__main__":
    rainfall = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    (
        total,
        average,
        zeroRain,
        moreThan5,
        percentile,
    ) = calcualte_rainfaill(rainfall)
    print("Numpy list:", rainfall)
    print("Total:", f"{total:.2f}")
    print("Average:", f"{average:.2f}")
    print("No rain:", zeroRain, "day(s)")
    print("More than 5mm:", moreThan5)
    print("75th percentile:", percentile)


# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Tasks:
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())
# Share your GitHub link on Teams when you have done.

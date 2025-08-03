import numpy as np


def calculate_temperature(input):
    max_temp = max(input)
    min_temp = min(input)
    fahrenheitValues = [f"{temp * 9/5 + 32}°F" for temp in input]
    weekDays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    exceed20Index = [i for i, temp in enumerate(input) if temp > 20]
    exceed20Days = [weekDays[i] for i in exceed20Index]
    avarageTemps = np.average(input)

    return max_temp, min_temp, fahrenheitValues, exceed20Days, avarageTemps


if __name__ == "__main__":
    temperatures = [18.5, 19, 20, 25.0, 2, 30, 13.9]
    (
        max,
        min,
        fahrenheit,
        exceed20Days,
        avarageTemps,
    ) = calculate_temperature(temperatures)
    print("Avarage temperature: ", f"{avarageTemps:.2f}°C")
    print("Max temperature: ", f"{max}°C")
    print("Min temperature: ", f"{min}°C")
    print(f"Fahrenheit values: ", fahrenheit)
    print(f"Days with temperature above 20°C: ", exceed20Days)

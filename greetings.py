import time

currentTimeHour = time.localtime().tm_hour
currentTimeMinute = time.localtime().tm_min
currentTime = f"{currentTimeHour} : {currentTimeMinute}"


def greet(name):
    if currentTimeHour <= 12:
        print(f"Hi {name}, Good Morning 🌅")
        print(f"It looks your local time is ⌚  {currentTime}")
    elif 16 >= currentTimeHour > 12:
        print(f"Hi {name}, Good Afternoon 🌞")
        print(f"It looks your local time is ⌚  {currentTime}")
    elif currentTimeHour > 16:
        print(f"Hi {name}, Good Evening 🌆")
        print(f"It looks your local time is ⌚  {currentTime}")


if __name__ == '__main__':
    print("Let's greet someone !")

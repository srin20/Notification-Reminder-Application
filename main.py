import pip
import time
import plyer
from plyer import notification


if __name__ == "_main_":
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="Let drink water remind you to drink water if you always forget it. "
                "Drinking water can prevent dehydration, a condition that can cause unclear thinking,"
                "result in mood change, cause your body to overheat, and lead to constipation and kidney stones."
                "The U.S. National Academies of Sciences, Engineering, and "
                "Medicine determined that an adequate daily fluid intake is:"
                "About 15.5 cups (3.7 liters) of fluids a day for men About 11.5 cups (2.7 liters) of fluids a day for women",
            app_icon="C:\\Users\\ranas\\PycharmProjects\\pythonProject2\\drink-water-2033667-1713173.ico",
            timeout=10
    )
    time.sleep(60*60)
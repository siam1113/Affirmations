import math, random

happiness = ["""
        "And [remember] when your Lord proclaimed, ‘If you are grateful, I will surely increase you [in favor]; but if 
        you deny, indeed, My punishment is severe.’  
        - Al-Quran (14:7)
        """, """
        “…If you are thankless—Allah is in no need of you—yet He is not pleased by ingratitude of His worshippers. And 
        if you are thankful He is pleased by it in you…” 
        - Al-Quran (39:7)
        """, """
        “…Anyone who desires the reward in this world shall be given it here, and anyone who desires the reward in the 
        hereafter shall be given it there. Soon We will reward the thankful.” 
        - Al-Quran (3:145)
        """]

sadness = [
    """
    “O you who have believed, seek help through patience and prayer.” 
    - Al-Quran [2:153]
    """,
    """
    “Indeed, Allah is with the patient.” 
    - Al-Quran [2:153]
    """,
    """
    “Whoever puts his trust in Allah; he will be enough for him.” 
    - Al-Quran [65:3]
    """,
]

random = math.floor(random.randint(0, 3))


def affirm(happy, sad):
    if happy == "Y":
        print(f"\033[32m{happiness[random]}\033[30m")
    elif sad == "Y":
        print(f"\033[32m{sadness[random]}\033[30m")


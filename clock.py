"""
The copy of the original iCoffee Clock
"""

import datetime
import time

def get_time_in_words(hours: int, minutes: int) -> str:
    """
    Returns the word based time

    :param hours: Hours part of time.
    :type hours: int
    :param minutes: Minutes part of time.
    :type minutes: int
    :return: Formatted time: e.g. 'Es ist Virtel vor Neun'
    :rtype: str
    """

    prefix = "Es ist "
    hours = hours % 12


    hour_dict = {0: "Zwölf",
                 1: "Eins",
                 2: "Zwei",
                 3: "Drei",
                 4: "Vier",
                 5: "Fünf",
                 6: "Sechs",
                 7: "Sieben",
                 8: "Acht",
                 9: "Neun",
                 10: "Zehn",
                 11: "Elf",
                 12: "Zwölf",
                 }

    min_dict = {0:f"{hour_dict[hours]} Uhr",
               5: "Fünf nach " + hour_dict[hours],
               10: "Zehn nach " + hour_dict[hours],
               15: "Viertel nach " + hour_dict[hours],
               20: "Zwanzig nach " + hour_dict[hours],
               25: "Fünf vor Halb " + hour_dict[hours+1],
               30: "Halb " + hour_dict[hours+1],
               35: "Fünf nach Halb " + hour_dict[hours+1],
               40: "Zwanzig vor " + hour_dict[hours+1],
               45: "Viertel vor " + hour_dict[hours+1],
               50: "Zehn vor " + hour_dict[hours+1],
               55: "Fünf vor " + hour_dict[hours+1],
               }

    return prefix + min_dict[minutes]


last = -1
while(True):
    temp = datetime.datetime.now()
    minutes = temp.minute
    minutes = minutes - minutes%5
    hour = temp.hour

    if minutes != last:
        last = minutes

        time_in_words = get_time_in_words(hour, minutes)
        print(time_in_words)

    time.sleep(1)

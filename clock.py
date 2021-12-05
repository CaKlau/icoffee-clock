"""
The copy of the original iCoffee Clock
"""

import datetime
import time

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

min_dict = {0:"-",
            5: "Fünf nach ",
            10: "Zehn nach ",
            15: "Viertel nach ",
            20: "Zwanzig nach ",
            25: "Fünf vor Halb ",
            30: "Halb ",
            35: "Fünf nach Halb ",
            40: "Zwanzig vor ",
            45: "Viertel vor ",
            50: "Zehn vor ",
            55: "Fünf vor ",
            }


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
    minutes = minutes - minutes%5
    if minutes == 0:
        return prefix + hour_dict[hours] + " Uhr"
    if minutes >= 25:
        return prefix + min_dict[minutes] + hour_dict[hours + 1]
    if minutes < 25:
        return prefix + min_dict[minutes] + hour_dict[hours]
    return prefix + "zu spät"


if __name__ == '__main__':
    last = -1
    while(True):
        temp = datetime.datetime.now()
        minutes = temp.minute
        hour = temp.hour

        if minutes != last:
            last = minutes

            time_in_words = get_time_in_words(hour, minutes)
            print(time_in_words)

        time.sleep(1)

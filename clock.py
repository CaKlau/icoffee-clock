import datetime
import sys
import os
import time

print("Hello World")

def get_time_in_words(hours: int, minutes: int) -> str:
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
    
    return min_dict[minutes]
    


i = 0
last = ""
while(True):
    temp = datetime.datetime.now()
    min = temp.minute
    min = min - min%5
    hour = temp.hour
    
    if min != last:
        last = min
    
        time_in_words = get_time_in_words(hour, min)
        print(time_in_words)
    
    time.sleep(1)


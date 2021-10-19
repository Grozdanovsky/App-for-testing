import json
import time
from difflib import get_close_matches

data = json.load(open('first project/data.json'))
loop = True
while loop:
    def explanation(key):

        key = key.lower()

        while True:

            if key in data:
                return data[key]

            elif len(get_close_matches(key, data.keys())) > 0:
                confirmation = input(f"Did you mean {get_close_matches(key, data.keys(), cutoff=0.8)[0]}? Enter Y for yes, or N for no:\n")

                if confirmation.lower() == "y":
                    return data[get_close_matches(key, data.keys(), cutoff=0.8)[0]]

                elif confirmation.lower() == "n":
                    print("The word doesn't exist. Please try again.")
                    break

                else:
                    return "We didn't understand your entry."

            else:
                print("The word doesn't exist. Please try again.")
                break

    word = input("Enter a word: ")

    output = (explanation(word))

    if type(output) == list:
        for item in output:
            print(item)

    again = input("Do you want another word? Enter Y for yes, or N for no:\n")
    if again.lower() == "y":
        continue
    elif again.lower() == "n":
        print("Have a nice day. BYE!")
        loop = False
        time.sleep(20)
    else:
        print("We didn't understand your entry.")
    time.sleep(20)
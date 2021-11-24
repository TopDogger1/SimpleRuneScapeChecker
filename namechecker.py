import threading
import requests, time

site = "https://apps.runescape.com/runemetrics/profile/profile?user="

x = 0
while x <3:
    unclaimed_file = open("unclaimed.txt", "a")
    word_file = open("user.txt", "r")
    word_array = word_file.readlines()

    print("{0} words were read from the provided file.".format(len(word_array)))
    print("Starting :)")

    for x in range(len(word_array)):

        word = word_array[x].strip()
        r = requests.get(site + word)
        data = r.json()
        try:
            response = data["error"]
        except:
            response = "ActiveAccount"

        if (response == "NO_PROFILE"):
            print(response+ ":" + word)
            unclaimed_file.write(word + ",")
        if(response == "NOT_A_MEMBER"):
            print(word + " is banned!" )
        if(response == "ActiveAccount"):
            print("Account " + word + " is taken by an Active Account!")
    print("All names are checked :)")
    unclaimed_file.close()

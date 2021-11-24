import requests
print("""\
 $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\        $$\   $$\                                          $$$$$$\  $$\                           $$\                           
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$$\  $$ |                                        $$  __$$\ $$ |                          $$ |                          
$$ /  $$ |$$ /  \__|$$ |  $$ |$$ /  \__|      $$$$\ $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ |  $$ |\$$$$$$\  $$$$$$$  |\$$$$$$\        $$ $$\$$ | \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$ |  $$ | \____$$\ $$  __$$<  \____$$\       $$ \$$$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$\   $$ |$$ |  $$ |$$\   $$ |      $$ |\$$$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
 $$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$  |      $$ | \$$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\       \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
 \______/  \______/ \__|  \__| \______/       \__|  \__| \_______|\__| \__| \__| \_______|       \______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|       
    """)
print("Made by TopDogger#8584")

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

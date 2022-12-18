# Names: Anthony Curcio-Petraccoro, Deming Tracy, William Sotiropoulos 
# Date: 11/17/2022 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# Week 12 Group Project 

import copy

musicrec1 = "musicrecplus.txt"

def loadUserToDictionary(fileName): # Anthony, Deming & William. 
    '''Takes in a text file and converts the user information into a dictionary.'''
    userDictionary = {}
    try:
        file = open(fileName, 'r+')
        for line in file:
            [userName, bands] = line.strip().split(":")
            bandList = bands.split(",")
            bandList.sort()
            titledL = []
            for bands in bandList:
                titledL.append(bands.title())
            userDictionary[userName.title()] = titledL
        file.close()
    except IOError:
        file = open(fileName, "w")
    return userDictionary

users = loadUserToDictionary(musicrec1)

def loadUsersToText(fileName): # Anthony, Deming & William. 
    '''Takes in a dictionary and converts the user information in a text file with the proper format.'''
    names = list(users.keys())
    people = copy.deepcopy(users)
    l = ""
    file = open(fileName, 'w')
    for line in range(len(names)):    
        l = names[line].strip() + ":" + ','.join(people[names[line]]) 
        l += "\n"
        file.write(l)
    file.close()

def greeting(): # Anthony, Deming & William. 
    '''This is the initial function a user sees when using the program. If they are a new user, they will be prompted to input preferences. If they are a returning user, they will be brought to the menu.'''
    username = input("Enter you name (put a $ symbol after your name if you wish your preferences to " + "\n" "remain private): " + "\n")
    if username.title() in users:
        menu(username.title())
    else:
        if username.title() != "":
            users[username.title()] = [] 
        enterPreference(username.title())

def menu(username): # Anthony, Deming & William. 
    '''This is the menu that redirects the user to the proper function based on their input.'''
    firstResponse = input("Enter a letter to choose an option: " + "\n" + "e - Enter preferences " + "\n" + "r - Get recommendations " + "\n" + "p - Show most popular artists " + "\n" + "h - How popular is the most popular " + "\n" + "m - Which user has the most the likes " + "\n" + "q - Save and quit " + "\n")
    if firstResponse.lower() == "e":
        enterPreference(username.title())
    if firstResponse.lower() == "r":
        print(getRecommendations(username.title()))
    if firstResponse.lower() == "p":
        print(showPopularArtist(username.title())[0])
        print(showPopularArtist(username.title())[1])
        print(showPopularArtist(username.title())[2])
    if firstResponse.lower() == "h":
        print(howPopularIsArtist(username.title()))
    if firstResponse.lower() == "m":
        print(mostLikes(username.title()))
    if firstResponse.lower() == "q":
        saveAndQuit()
    else:
        menu(username.title())

def enterPreference(username): # Anthony, Deming & William. 
    '''This function allows the user to add preferences, and properly stores them in the correct location in the dictionary based on the given username.'''
    L = users[username]
    likedArtist = input("Enter an artist that you like (Enter to finish): " + "\n")
    while likedArtist != "":
        if likedArtist.title() in users[username]:
            likedArtist = input("Enter an artist that you like (Enter to finish): " + "\n")
        else:
            L.append(likedArtist.title()) 
            likedArtist = input("Enter an artist that you like (Enter to finish): " + "\n")
    L.sort()
    users[username] = L
    menu(username)

def publicUsersOnly(): # Anthony, Deming & William. 
    '''This function returns a dictionary of the public users only. There username and preferences are stores in the dictionary.'''
    publicUsers = copy.deepcopy(users)
    currentUser = ""
    publicUsersNames = list(users.keys())
    for i in range(len(publicUsersNames)):
        lastLetter = len(publicUsersNames[i]) - 1
        currentUser = publicUsersNames[i]
        if currentUser[lastLetter] == "$":
            del publicUsers[publicUsersNames[i]]
    return publicUsers
 
def getRecommendations(username): # Anthony, Deming & William. 
    '''This function returns other user's preferences based on the amount of artists you have in common. Takes in the current user's username as an input to ensure the proper preferences are being added.'''
    def counterSimilarity(currentUserArtists, otherUserArtists):
        '''Takes the current user's preferences and the preferences of the other users and compares the similarities. The other user's preferences will be iterated through using a for loop in the getRecommendations() function.'''
        counter = 0
        for sim in range(len(otherUserArtists)):
            if otherUserArtists[sim] in currentUserArtists:
                counter += 1
        return counter       
    names = list(publicUsersOnly().keys())
    currentUserArtists = users[username]
    otherUserArtists = [] 
    mostSimilar = publicUsersOnly()[names[0]] 
    simCounter = 0
    for people in range(1, len(publicUsersOnly())): 
        otherUserArtists = publicUsersOnly()[names[people]] 
        if currentUserArtists != otherUserArtists:
            if counterSimilarity(currentUserArtists, mostSimilar) < counterSimilarity(currentUserArtists, otherUserArtists):
                mostSimilar = publicUsersOnly()[names[people]]
                simCounter += 1
            if counterSimilarity(currentUserArtists, mostSimilar) > counterSimilarity(currentUserArtists, otherUserArtists):
                simCounter += 1
    if simCounter == 0 or simCounter == len(currentUserArtists):
        str = "No recommendations available at this time." 
        return str
    if len(mostSimilar) < len(currentUserArtists): 
        for artists in range(len(mostSimilar)):
            if currentUserArtists[artists] in mostSimilar:
                mostSimilar.remove(currentUserArtists[artists])
    if len(mostSimilar) > len(currentUserArtists):
        for artists in range(len(currentUserArtists)):
            if currentUserArtists[artists] in mostSimilar:
                mostSimilar.remove(currentUserArtists[artists])
    for recs in range(len(mostSimilar)):
        if mostSimilar[recs] not in users[username]:
            print(mostSimilar[recs])
    menu(username)

def biglist(): # Anthony, Deming & William. 
    '''Returns the list of all artists in all public user's preferences. Artists can have duplicates, since multiple users can have the same artist in their preferences.''' 
    L = []
    for bands in publicUsersOnly():
        L.extend(publicUsersOnly()[bands])         
    return sorted(L)
    
def smalllist(): # Anthony, Deming & William. 
    '''Returns a list of each artist that appears in all the different user's preferences, but they only appear once.''' 
    L = []
    L2 = biglist()
    for i in range(len(L2)):
        if L2[i] not in L:
            L.append(L2[i])
    return L

def popular2(S, L): # Anthony, Deming & William. 
    '''This function compares two artists and returns the one that is more popular based on the amount of playlists they are in.'''
    counter = 0
    bigList = biglist()
    for i in range(len(biglist())):
        if bigList[i] == S:
            counter += 1
    return counter

def showPopularArtist(username): # Anthony, Deming & William. 
    '''This function utilizes the function above to obtain the most popular artist, but returns the top three artists and their names.''' 
    small = copy.deepcopy(smalllist())
    big = copy.deepcopy(biglist())
    S = small[0]
    names = []
    for j in range(3):
        for i in range(1, len(small)):
            t = popular2((small[i]), big)
            t2 = popular2((S), big)
            if t > t2:
                S = small[i]
        names.append(S)
        small.remove(S) 
        big.remove(S)
        S = small[0]
    if len(small) == 0:
        print("Scripts")
    return names
    menu(username)

def howPopularIsArtist(username): # Anthony, Deming & William. 
    '''Returns the amount of times the most popular artist appears in all the user's playlists.''' 
    name = str(showPopularArtist(username)[0])
    number = popular2(name, biglist())
    return number
    menu(username)
    
def mostLikes(username): # Anthony, Deming & William. 
    '''This returns the user with the largest preferences list.'''
    names = list(publicUsersOnly().keys())
    artists = list(publicUsersOnly().values())
    mostName = names[0]
    mostArtist = artists[0]
    likeCount = len(mostArtist)
    for people in range(1, len(publicUsersOnly())):
        second = artists[people]
        if len(second) > len(mostArtist):
            mostArtist = second
            likeCount = len(mostArtist)
            mostName = names[people]
    return mostName
    menu(username)

def saveAndQuit(): # Anthony, Deming & William. 
    '''Saves the dictionary to a text file utilizing the function at the top of the .py file.'''
    loadUsersToText(musicrec1)
    quit()  
    
greeting()

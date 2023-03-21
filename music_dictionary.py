#Kristof Rohaly-Medved
#CS21
#Program to access and present stored information on music artists, alubums, and songs

MIN_CHOICE = 1
MAX_CHOICE = 5

#Function that populates dictionary from input file and processes inputted choice
def main():
    #Open infile and prime loop that populates newly created dictionary
    try:
        print('Welcome to my music collection')
        infile = open('music_collection.txt', 'r')
    except ValueError:
        print('File not found. Program terminating ...')
    else:
        music_dictionary = {}
        music = infile.read().split('\n')
        for line in music:
            line = line.split(': ')
            if line[0] == 'Artist':
                artist = line[1]
                music_dictionary[artist] = {}
            if line[0] == 'Album':
                album = line[1]
                music_dictionary[artist][album] = []
            if line[0] == 'Song':
                music_dictionary[artist][album].append(line[1])
                
        #Get choice and execute appropriate function
        choice = get_menu_choice()
        #Print songs that start with character
        while choice != MAX_CHOICE:
            if choice == MIN_CHOICE:
                print('You have chosen to search for songs that begin with a specified character')
                character = input('What character do you choose? ')
                songs = songs_start_with(music_dictionary, character)
                if len(songs) > 0:
                    for song in songs:
                        print(song)
                else:
                    print(f'There are no songs that begin with {character}')
            #Print songs that contain word
            elif choice == MIN_CHOICE + 1:
                print('You have chosen to search for songs that contain a specified word')
                word = input('What word do you choose? ')
                songs = songs_containing_word(music_dictionary, word)
                if len(songs) > 0:
                    for song in songs:
                        print(song)
                else:
                    print(f'There are no songs that contain {word}')
            #Print artist for song
            elif choice == MIN_CHOICE + 2:
                print('You have chosen to find the artist for a specificed song')
                title = input('What song do you choose? ')
                artist = who_sang(music_dictionary, title)
                if len(artist) > 0:
                    print(f'{artist} performed {title}')
                else:
                    print(f'{title} is not in my collection')
            #Print all songs by artist
            elif choice == MIN_CHOICE + 3:
                print('You have chosen to list all songs by a specified artist')
                artist = input('Which artist? ')
                songs, proper_artist = song_by_artist(music_dictionary, artist)
                if len(songs) > 0:
                    print(f'Songs by {proper_artist}')
                    for song in songs:
                        print(song)
                else:
                    print(f'I have no songs by {artist}')
            print()
            choice = get_menu_choice()
            
#Function that validates and returns choice
def get_menu_choice():
    choice_list = ['1 - find all songs titles that begin with a specificed character','2 - find all song  titles that contain a specificed word','3 - find the artist for a given song title','4 - get a list of all songs by a specificed artist','5 - quit']
    print('Your choices are: ')
    for item in choice_list:
        print(item)
    go = False
    while go == False:
        try:
            choice = int(input('Your choice? '))
            while choice < MIN_CHOICE or choice > MAX_CHOICE:
                print('Your choices are: ')
                for item in choice_list:
                    print(item)
                choice = int(input('Your choice? '))
            return(choice)
        except ValueError:
            print('Only integer input accepted')
            print('Your choices are: ')
            for item in choice_list:
                    print(item)

#Function that returns all songs that start with inputted character
def songs_start_with(dictionary, char):
    char = char.lower()
    songs_list = []
    #Get all songs into one list
    for artist in dictionary:
        for album in dictionary[artist]:
            for index in range(len(dictionary[artist][album])):
                song = dictionary[artist][album][index]
                songs_list.append(song)
    #Check if song starts with character
    valid_songs = []
    for index in range(len(songs_list)):
        song = songs_list[index]
        song = song.lower()
        if song.startswith(char):
            valid_songs.append(songs_list[index])
    #Return list with all songs that start with specified character
    return valid_songs
    

#Function that returns all songs that contain an inputted word
def songs_containing_word(dictionary, word):
    word = word.lower()
    songs_list = []
    #Get all songs into one list
    for artist in dictionary:
        for album in dictionary[artist]:
            for index in range(len(dictionary[artist][album])):
                song = dictionary[artist][album][index]
                songs_list.append(song)
    #Check if song contains word
    valid_songs = []
    for index in range(len(songs_list)):
        song = songs_list[index]
        song = song.lower()
        song_split = song.split(' ')
        if word in song_split:
            valid_songs.append(songs_list[index])
    #Return list with all songs that contain an inputted word
    return valid_songs

#Function that returns artist that sang an inputted song title
def who_sang(dictionary, title):
    title = title.lower()
    #Compare stored songs to inputted title for each album for each artist
    for artist in dictionary:
        for album in dictionary[artist]:
            for index in range(len(dictionary[artist][album])):
                song = dictionary[artist][album][index]
                song = song.lower()
                #If inputted title is found, return artist of that title
                if song == title:
                    return artist
    #If no artist, return empty string
    return ''

#Function that returns all songs by an inputted artist               
def song_by_artist(dictionary, artist):
    artist = artist.lower()
    artist_songs = []
    for singer in dictionary:
        if artist == singer.lower():
            for album in dictionary[singer]:
                #Add each song from each album of inputted artist to a list
                for index in range(len(dictionary[singer][album])):
                    song = dictionary[singer][album]
                    artist_songs.append(song[index])
            artist = singer
    #Return list populated with songs by inputted artist
    return artist_songs, artist


main()

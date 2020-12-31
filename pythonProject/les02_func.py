# Defining a function

def Mysongs():
    first_fav=' "my heart will go on" '
    first_fav=first_fav.title().lstrip().rstrip()
    second_fav=" 'Dance monkey' "
    second_fav=second_fav.upper()
    third_fav=' "FADED" '
    third_fav=third_fav.lower()
    Fav_songs=first_fav + second_fav + third_fav
    return Fav_songs


def Artist(first_artist, second_artist, third_artist):
    artist1=first_artist
    artist2=second_artist
    artist3=third_artist
    print(Mysongs())
    print()
    return artist1 + artist2 + artist3
Artist=Artist("Dion "," Tones_and_I "," Alan_walker")
print(Artist)

def Ratings(firstsong_rating,secondsong_rating,thirdsong_rating):
    song1=str(firstsong_rating) + ' star'
    song2=str(secondsong_rating) + ' star'
    song3=str(thirdsong_rating) + ' star'
    print()
    print("my heart will go on=",song1)
    print("Dance monkey=",song2)
    print("faded=",song3)
    return True
Ratings(5,4.5,4)

def bool():
    val1=True
    val2=False
    print(val1+val2) # True+False=1
    return  Val1
print(bool())
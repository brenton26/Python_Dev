'''
This program takes in the lyrics of a song and returns a dictionary
object with the number of times each word in the song was used.
'''


lyrics='''
Oh baby, baby 
Oh baby, baby 
Oh baby, baby, how was I supposed to know 
That something wasn't right here? 
Oh baby, baby, I shouldn't have let you go 
And now you're out of sight, yeah 
Show me how want it to be 
Tell me, baby, 'cause I need to know now, oh because 
My loneliness is killing me (and I) 
I must confess I still believe (still believe) 
When I'm not with you I lose my mind 
Give me a sign 
Hit me, baby, one more time 
Oh baby, baby 
The reason I breathe is you 
Boy, you got me blinded 
Oh, pretty baby 
There's nothing that I wouldn't do 
It's not the way I planned it 
Show me how you want it to be 
Tell me, baby, 'cause I need to know now, oh because 
My loneliness is killing me (and I) 
I must confess I still believe (still believe) 
When I'm not with you I lose my mind 
Give me a sign 
Hit me, baby, one more time 
Oh baby, baby (oh oh) 
Oh baby, baby (yeah) 
Oh baby, baby, how was I supposed to know? 
Oh pretty baby, I shouldn't have let you go 
I must confess, that my loneliness is killing me now 
Don't you know I still believe 
That you will be here 
And give me a sign 
Hit me, baby, one more time 
My loneliness is killing me (and I) 
I must confess I still believe (still believe) 
When I'm not with you I lose my mind 
Give me a sign 
Hit me, baby, one more time 
I must confess, that my loneliness is killing me now 
Don't you know I still believe 
That you will be here 
And give me a sign 
Hit me, baby, one more time
'''
lyrics = lyrics.lower()
letters = ' abcdefghijklmnopqrstuvwxyz'
formated_lyrics = ''

for char in lyrics:
    if char in letters:
        formated_lyrics = formated_lyrics + char
#print (formated_lyrics)

lyrics_list = formated_lyrics.split(' ')
#print(lyrics_list)

lyrics_dictionary = {}

for word in lyrics_list:
    if word in lyrics_dictionary:
        lyrics_dictionary[word] += 1
    else:
        lyrics_dictionary[word] = 1
#print(lyrics_dictionary)
# print(sorted(lyrics_dictionary.()))


for i in lyrics_dictionary.items(): print(i)
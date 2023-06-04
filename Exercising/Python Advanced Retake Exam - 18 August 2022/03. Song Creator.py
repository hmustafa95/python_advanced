def add_songs(*args):
    my_dict = {}
    for song_all in args:
        name, lyrics = song_all
        if name not in my_dict:
            my_dict[name] = ''
        my_dict[name] += '\n'.join(lyrics)
    result = ''
    for k, v in my_dict.items():
        if len(v) == 0:
            result += f'- {k}' + '\n'
        else:
            result += f'- {k}\n{v}'
    return result

import os

def add_songs(*tuples_):
    songs = {}
    for t in tuples_:
        if t[0] not in songs:
            songs[t[0]] = []
        songs[t[0]].extend(t[1])
    result = []
    for song_title, song_lyrics in songs.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)
    return os.linesep.join(result)


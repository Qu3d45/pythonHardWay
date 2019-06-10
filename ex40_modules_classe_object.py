# Learn Pyhton The Hard Way ex40 - Modules, Classes, and Objects
# Manuel Lameira


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.varia = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def just_a_line(self):
        for line in self.varia:
            print(line * 2)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here"])

bulls_on_parade = Song(["\nThey rally around tha family",
                        "With pockets full of shells."])

cry_me_a_river = Song(["\nNow you say you're lonely",
                       "You cry the whole night through",
                       "Well you can cry me a river",
                       "Cry me a river, I cried a river over you"])

let_me_enter = Song(["\nHell is gone and heaven's here",
                     "There's nothing left for you to fear",
                     "Shake your arse come over here",
                     "Now scream",
                     "I'm a burning effigy",
                     "Of everything I used to be",
                     "You're my rock of empathy, my dear"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

cry_me_a_river.sing_me_a_song()

let_me_enter.sing_me_a_song()

let_me_enter.just_a_line()

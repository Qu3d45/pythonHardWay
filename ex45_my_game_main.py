# Learn Pyhton The Hard Way ex45 - My Final Super Game
# Manuel Lameira

# Here are your requirements:
# 1. Make a different game from the one I made. (I diden't ;) )
# 2. Use more than one file, and use import to use them. Make sure you know what that is. (check!)
# 3. Use one class per room and give the classes names that fit their purpose (like GoldRoom, KoiPon- dRoom ). (check!)
# 4. Your runner will need to know about these rooms, so make a class that runs them and knows
#    about them. There’s plenty of ways to do this, but consider having each room return what room
#    is next or setting a variable of what room is next. (check!)

# I cheated a bit (lack of time) and use the game from ex43: Gothons from Planet Percal #25

# ”Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so
# he can escape into an escape pod to the planet below. The game will be more like a Zork or Adventure
# type game with text outputs and funny ways to die. The game will involve an engine that runs a map
# full of rooms or scenes. Each room will print its own description when the player enters it and then tell
# the engine what room to run next out of the map.”


import ex45_my_game_rooms


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_secene('finished')

        while current_scene != last_scene:
            next_secene_name = current_scene.enter()
            current_scene = self.scene_map.next_secene(next_secene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Map(object):

    scenes = {
        'central_corridor': ex45_my_game_rooms.CentralCorridor(),
        'laser_weapon_armory': ex45_my_game_rooms.LaserWeaponArmory(),
        'the_bridge': ex45_my_game_rooms.TheBrige(),
        'escape_pod': ex45_my_game_rooms.TheEscapePod(),
        'death': ex45_my_game_rooms.Death(),
        'finished': ex45_my_game_rooms.Finished()
    }

    def __init__(self, start_scene):
        self.start_secene = start_scene

    def next_secene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_secene(self.start_secene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# Calling individual scene to test
# a_game = TheEscapePod()
# a_game.enter()

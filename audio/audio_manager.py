import pygame
from os import path
from .sound_enum import SoundType


class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self._background_music = None
        self._option_change_sound = None
        self._selected_sound = None
        self.character_sounds = {}
        self.volume = 0.6

    def load(self):
        try:
            self.load_sounds()
            self.load_music()
        except Exception as e:
            print(f"error to load assets: {e}")

    def load_music(self):
        music_path = path.join('assets', 'sounds', 'theme_background.mp3')
        if path.exists(music_path):
            self._background_music = music_path
        else:
            print("theme_background not found")

    def load_sounds(self):
        characters = ['ryu']
        sounds_type = [
            SoundType.WEAK_PUNCH,
            SoundType.MEDIUM_PUNCH,
            SoundType.HIGH_PUNCH,
            SoundType.WEAK_KICK,
            SoundType.MEDIUM_KICK,
            SoundType.HIGH_KICK,
        ]

        for character in characters:
            self.character_sounds[character] = []
            for sound_type in sounds_type:
                sound_path = path.join('assets', 'sounds', character, f"{sound_type.name.lower()}.mp3")
                if path.exists(sound_path):
                    sound = pygame.mixer.Sound(sound_path)
                    self.character_sounds[character].append(sound)

    def play_character_sound(self, character, sound_type: SoundType):
        if character in self.character_sounds and 0 <= sound_type.value < len(self.character_sounds[character]):
            sound = self.character_sounds[character][sound_type.value]
            sound.play()

    def play_background_music(self):
        if self._background_music:
            pygame.mixer.music.load(self._background_music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(self.volume)

    @staticmethod
    def play_sound_by_type(sound_type: SoundType):
        base_path: str = path.dirname(path.dirname(__file__))
        sound_path: str = f'assets/sounds/menu/{sound_type.value}.mp3'
        sound_path = path.join(base_path, sound_path)
        sound: pygame.mixer.Sound = pygame.mixer.Sound(sound_path)
        sound.play()

    @staticmethod
    def dispose():
        pygame.mixer.quit()

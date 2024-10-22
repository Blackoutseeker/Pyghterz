from utils import Character
from state import PlayerState
from pygame import Surface, Rect, draw
from .character_hitbox import CharacterHitbox


class Hitbox:
    def __init__(self, character: Character, player_state: PlayerState, scale: float, screen: Surface):
        self._character = character
        self._player_state = player_state
        self._scale: float = scale
        self._screen = screen
        self._body_rectangle: Rect = Rect(0, 0, 0, 0)
        self._attack_rectangle: Rect = Rect(0, 0, 0, 0)
        self._attack_hitboxes: dict = self._get_attack_hitboxes()
        self._counter: int = 0

    def render(self):
        self._render_body_hitbox()
        self._render_attack_hitbox()

    def _get_attack_hitboxes(self) -> dict:
        attack_hitboxes = CharacterHitbox.get_attack_hitboxes(self._character)
        return attack_hitboxes

    def _render_body_hitbox(self):
        player_position_x, player_position_y = self._player_state.get_player_position()
        width = self._get_scaled_size(46)
        height = self._get_scaled_size(102)
        base_x = self._get_scaled_size(60)
        base_y = self._get_scaled_size(22)
        self._body_rectangle.update(player_position_x + base_x, player_position_y + base_y, width, height)
        draw.rect(self._screen, (0, 255, 0), self._body_rectangle, 3)

    def _render_attack_hitbox(self):
        is_player_attacking = self._player_state.get_is_attacking()
        if is_player_attacking:
            sprite_index = self._player_state.get_sprite_index()
            player_action = self._player_state.get_player_action()
            attack_hitbox = self._attack_hitboxes[player_action.name]
            start_index: int = attack_hitbox['start_index']
            end_index: int = attack_hitbox['end_index']

            if start_index <= sprite_index <= end_index:
                player_position_x, player_position_y = self._player_state.get_player_position()
                hitbox_length = len(attack_hitbox['rectangles'])
                current_frame = sprite_index - start_index
                self._counter = min(current_frame, hitbox_length - 1)

                attack_rectangle: Rect = attack_hitbox['rectangles'][self._counter]
                is_facing_right = self._player_state.get_is_facing_right()
                if not is_facing_right:
                    attack_rectangle = attack_hitbox['mirror_rectangles'][self._counter]

                attack_rectangle_width = attack_rectangle.width
                attack_rectangle_height = attack_rectangle.height
                attack_rectangle_base_x = attack_rectangle.x
                attack_rectangle_base_y = attack_rectangle.y
                scaled_width = self._get_scaled_size(attack_rectangle_width)
                scaled_height = self._get_scaled_size(attack_rectangle_height)
                base_x = self._get_scaled_size(attack_rectangle_base_x)
                base_y = self._get_scaled_size(attack_rectangle_base_y)

                self._attack_rectangle.update(player_position_x + base_x, player_position_y + base_y,
                                              scaled_width, scaled_height)
                draw.rect(self._screen, (255, 0, 0), self._attack_rectangle, 3)
            else:
                self._counter = 0
                self._dismiss_attack_rectangle()

    def _dismiss_attack_rectangle(self):
        self._attack_rectangle.update(0, 0, 0, 0)

    def _get_scaled_size(self, size: float) -> float:
        return size * self._scale

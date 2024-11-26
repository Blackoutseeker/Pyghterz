from .screen import Screen, ScreenType
from pygame import Surface, QUIT, quit, KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_RETURN, Rect, draw, USEREVENT
from state import QuizState
from utils import Character, Dimensions, Quiz, QuizDifficulty
from font import CustomFont
from random import shuffle
from typing import List
from pygame.event import Event
from sys import exit
from pygame.time import get_ticks, set_timer


class QuizScreen(Screen):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self._custom_font: CustomFont = CustomFont()
        self._player1_quiz_state: QuizState = QuizState(Character.RYU)
        self._player2_quiz_state: QuizState = QuizState(Character.RYU, True)
        self._quiz: Quiz = Quiz()
        self._questions: List[dict] = []
        self._selected_option: int = 0
        self._correct_option: bool = False
        self._options: List[str] = []
        self._current_question: dict = {}
        self._current_question_index: int = 0
        self._is_answered: bool = False
        self._current_player: int = 1
        self._next_question_event: int = USEREVENT + 2
        self._feedback_duration: int = 5000
        self._feedback_time: int = 0
        self._is_selecting_difficulty: bool = True
        self._difficulty_options: List[QuizDifficulty] = list(QuizDifficulty)
        self._selected_difficulty_index: int = 0
        self._player_difficulties: dict = {1: QuizDifficulty.EASY,
                                           2: QuizDifficulty.EASY}
        self._quiz_ended: bool = False

    def _load_questions(self):
        difficulty = self._player_difficulties[self._current_player]
        self._questions = self._quiz.get_questions(difficulty)
        shuffle(self._questions)

    def handle_events(self, events: List[Event]):
        for event in events:
            if event.type == QUIT:
                quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return ScreenType.MAIN_MENU.name
                if self._is_selecting_difficulty:
                    self._handle_difficulty_selection(event)
                else:
                    self._handle_question_selection(event)

            elif event.type == self._next_question_event:
                set_timer(self._next_question_event, 0)
                if self._current_player == 2 and self._is_answered:
                    self._quiz_ended = True
                if not self._quiz_ended:
                    self._is_answered = False
                    self._next_question()

            if self._quiz_ended:
                return ScreenType.GAMEPLAY.name

    def _handle_difficulty_selection(self, event: Event):
        if event.key == K_UP:
            self._selected_difficulty_index = (self._selected_difficulty_index - 1) % len(self._difficulty_options)
        elif event.key == K_DOWN:
            self._selected_difficulty_index = (self._selected_difficulty_index + 1) % len(self._difficulty_options)
        elif event.key == K_RETURN:
            selected_difficulty = self._difficulty_options[self._selected_difficulty_index]
            self._player_difficulties[self._current_player] = selected_difficulty
            self._is_selecting_difficulty = False
            self._load_questions()
            self._load_current_question()

    def _load_current_question(self):
        if self._current_question_index >= len(self._questions):
            return
        self._current_question = self._questions[self._current_question_index]
        self._options = list(self._current_question['items'].keys())
        shuffle(self._options)
        self._correct_option = self._get_correct_option(self._current_question['items'], self._options)
        self._selected_option = 0
        self._is_answered = False

    def _next_question(self):
        self._current_player = 2 if self._current_player == 1 else 1
        self._current_question_index = 0
        self._selected_difficulty_index = 0
        self._is_selecting_difficulty = True
        self._player_difficulties = {1: QuizDifficulty.EASY,
                                     2: QuizDifficulty.EASY}

    def _handle_question_selection(self, event: Event):
        if event.key == K_UP and not self._is_answered:
            self._selected_option = (self._selected_option - 1) % len(self._options)
        elif event.key == K_DOWN and not self._is_answered:
            self._selected_option = (self._selected_option + 1) % len(self._options)
        elif event.key == K_RETURN and not self._is_answered:
            self._is_answered = True
            self._feedback_time = get_ticks()

            is_correct_option: bool = self._selected_option == self._correct_option
            is_second_player: bool = self._current_player == 2
            difficulty: QuizDifficulty = self._player_difficulties[self._current_player]
            quiz_player_state: QuizState = self._player1_quiz_state
            score: int = self._quiz.get_score(difficulty)
            percentage_balance: float = self._quiz.get_percentage_balance(difficulty)

            if is_second_player:
                quiz_player_state = self._player2_quiz_state
            if not is_correct_option:
                score = 0
                percentage_balance = -percentage_balance

            quiz_player_state.increase_score(score)
            quiz_player_state.set_percentage_balance(percentage_balance)
            print(quiz_player_state.get_score())
            print(quiz_player_state.get_percentage_balance())
            set_timer(self._next_question_event, self._feedback_duration)

    def render(self):
        screen_background_color: tuple[int, int, int] = (130, 31, 35)
        if self._current_player == 2:
            screen_background_color = (33, 91, 130)
        self.screen.fill(screen_background_color)
        if self._is_selecting_difficulty:
            self._render_difficulty_selection()
        else:
            self._render_question()

    def _render_difficulty_selection(self):
        font = self._custom_font
        screen_width = Dimensions.SCREEN_WIDTH.value
        screen_height = Dimensions.SCREEN_HEIGHT.value
        start_y = screen_height // 4
        option_height = 90
        line_height = 30

        title_text = f"Jogador {self._current_player}: Escolha a dificuldade!"
        title_lines = self._wrap_text(title_text, 16, screen_width - 100)
        y_offset = start_y

        question_rect = Rect(40, start_y, screen_width - 100, len(title_lines) * line_height + 10)
        question_rect.y -= 40
        draw.rect(self.screen, (0, 0, 0), question_rect.inflate(40, 40))

        for line in title_lines:
            title_line_text = font.render_font(
                text=line,
                size=16,
                color=(255, 255, 255),
                position=(0, 0)
            )
            self.screen.blit(title_line_text, (100, y_offset - 30))
            y_offset += line_height

        options_start_y = y_offset + 50

        for i, difficulty in enumerate(self._difficulty_options):
            difficulty_text = difficulty.value
            option_text = font.render_font(
                text=difficulty_text,
                size=14,
                color=(255, 255, 255),
                position=(0, 0)
            )
            option_rect = Rect(50, options_start_y + i * option_height, screen_width - 100, line_height)
            option_rect.x -= 10
            draw.rect(self.screen, (0, 0, 0), option_rect.inflate(40, 40))
            option_border_color: tuple[int, int, int] = (0, 0, 0)
            if i == self._selected_difficulty_index:
                option_border_color = (255, 255, 255)
            draw.rect(self.screen, option_border_color, option_rect.inflate(40, 40), width=5)
            self.screen.blit(option_text, (option_rect.width // 2, options_start_y + i * option_height + 8))

    def _wrap_text(self, text: str, size: int, max_width: int):
        words = text.split(' ')
        lines = []
        current_line = ''

        for word in words:
            test_line = current_line + (' ' if current_line else '') + word
            test_width, _ = (self._custom_font.render_font(test_line, size=size, color=(255, 255, 255), position=(0, 0))
                             .get_size())

            if test_width <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    @staticmethod
    def _get_correct_option(options: dict, shuffled_options: List[str]) -> int:
        correct_answer = next(key for key, value in options.items() if value)
        return shuffled_options.index(correct_answer)

    def _render_question(self):
        screen_background_color: tuple[int, int, int] = (130, 31, 35)
        if self._current_player == 2:
            screen_background_color = (33, 91, 130)
        self.screen.fill(screen_background_color)
        font = self._custom_font

        screen_width = Dimensions.SCREEN_WIDTH.value
        screen_height = Dimensions.SCREEN_HEIGHT.value

        question_height = 50
        option_height = 90
        spacing_between_question_and_options = 30
        line_height = 30

        total_height = (
                question_height
                + spacing_between_question_and_options
                + len(self._options) * option_height
        )

        start_y = (screen_height - total_height) // 2

        question_text = f'Jogador {self._current_player}: {self._current_question["question"]}'
        question_lines = self._wrap_text(question_text, 16, screen_width - 100)

        question_rect = Rect(40, start_y, screen_width - 100, len(question_lines) * line_height + 10)
        question_rect.y -= 40
        draw.rect(self.screen, (0, 0, 0), question_rect.inflate(40, 40))

        y_offset = start_y + 20
        for line in question_lines:
            question_line_text = font.render_font(
                text=line,
                size=14,
                color=(255, 255, 255),
                position=(0, 0)
            )
            self.screen.blit(question_line_text, (50, y_offset - 50))
            y_offset += line_height

        options_start_y = y_offset + spacing_between_question_and_options - 30

        for i, option in enumerate(self._options):
            letter = 'a)' if i == 0 else 'b)' if i == 1 else 'c)' if i == 2 else 'd)'
            option = f'{letter} {option}'
            is_correct_option: bool = self._selected_option == self._correct_option

            if self._is_answered:
                difficulty: QuizDifficulty = self._player_difficulties[self._current_player]
                percentage_balance: float = self._quiz.get_percentage_balance(difficulty)
                percentage: int = int(percentage_balance * 100)
                option = f'Errado! -{percentage}% de vida e -{percentage}% de dano causado!'
                if is_correct_option:
                    option = f'Correto! +{percentage}% de vida e +{percentage}% de dano causado!'

            option_lines = self._wrap_text(option, 12, screen_width - 100)
            option_rect = Rect(50, options_start_y + i * option_height, screen_width - 100,
                               len(option_lines) * line_height)
            option_rect.x -= 10
            show_rectangle: bool = not self._is_answered or (self._is_answered and self._selected_option == i)

            if show_rectangle:
                draw.rect(self.screen, (0, 0, 0), option_rect.inflate(40, 40))

            total_text_height = len(option_lines) * line_height
            y_offset = option_rect.top + (option_rect.height - total_text_height) // 2

            for line in option_lines:
                text_color = (255, 255, 255)
                if self._is_answered:
                    text_color = (255, 0, 0)
                    if is_correct_option:
                        text_color = (0, 255, 0)
                option_line_text = font.render_font(
                    text=line,
                    size=12,
                    color=text_color,
                    position=(0, 0)
                )
                if show_rectangle:
                    self.screen.blit(option_line_text, (50, y_offset + 10))
                y_offset += line_height

            selected_option_color: tuple[int, int, int] = (0, 0, 0)
            if i == self._selected_option:
                selected_option_color = (255, 255, 255)
                if self._is_answered:
                    selected_option_color = (255, 0, 0)
                    if is_correct_option:
                        selected_option_color = (0, 255, 0)
            if show_rectangle:
                draw.rect(self.screen, selected_option_color, option_rect.inflate(40, 40), 5)

            options_start_y += option_rect.height - 40

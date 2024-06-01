import time
import pygame
from pygame.font import Font
from pygame.color import Color
from pygame.event import Event
from pygame import Rect, Surface
from typing import List, Tuple, Callable

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400

# Fonts
NORMAL = Font("fonts/OpenSans-Regular.ttf", 28)
MEDIUM = Font("fonts/OpenSans-Regular.ttf", 40)
LARGE = Font("fonts/OpenSans-Regular.ttf", 60)

# Colors
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

# Alignment
VERTICAL = HEIGHT / 2
HORIZONTAL = WIDTH / 2


class GUI:
    def __init__(
        self,
        width: float = WIDTH,
        height: float = HEIGHT
    ) -> None:
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

    def show(self) -> None:
        pygame.display.flip()

    def background(self, color: Color) -> None:
        self.screen.fill(color)

    def events(self) -> List[Event]:
        return pygame.event.get()

    def mouse_pressed(self) -> bool:
        return pygame.mouse.get_pressed()[0]

    def quit(self, event: Event) -> bool:
        return event.type == pygame.QUIT


class Text:
    def __init__(
        self,
        text: str,
        font: Font = NORMAL,
        color: Color = WHITE
    ) -> None:
        self.text = text
        self.font = font
        self.color = color
        self.render()

    def render(self) -> None:
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()

    def draw(self, screen: Surface) -> None:
        screen.blit(self.surface, self.rect)

    def align(self, position: Tuple[int, int]) -> None:
        self.rect.center = position


class Title(Text):
    def __init__(self, title: str, color: Color = WHITE) -> None:
        super().__init__(title, MEDIUM, color)


class Rectangle:
    def __init__(
        self,
        left: float,
        top: float,
        width: float,
        height: float,
        background: Color = WHITE
    ) -> None:
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.background = background
        self.render()

    @property
    def position(self) -> Tuple[float, float]:
        return (self.left, self.top)

    @property
    def size(self) -> Tuple[float, float]:
        return (self.width, self.height)

    @position.setter
    def position(self, position: Tuple[float, float]) -> None:
        self.left, self.top = position

    @size.setter
    def size(self, size: Tuple[float, float]) -> None:
        self.width, self.height = size

    def render(self) -> None:
        self.rect = Rect(self.left, self.top, self.width, self.height)

    def draw(self, screen: Surface, width: int = 0) -> None:
        pygame.draw.rect(screen, self.background, self.rect, width)


class Button(Rectangle):
    def __init__(
        self,
        text: str,
        left: float,
        top: float,
        width: float,
        height: float,
        color: Color = BLACK,
        background: Color = WHITE
    ) -> None:
        super().__init__(left, top, width, height, background)
        self.text = text
        self.color = color

    def draw(self, screen: Surface, width: int = 0) -> None:
        super().draw(screen, width)
        text = Text(self.text, color=self.color)
        text.align(self.rect.center)
        text.draw(screen)

    def onclick(self, function: Callable[..., any]) -> None:
        self.onclick = function

    def handle_click(self, *args, **kwargs):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            time.sleep(0.3)
            return self.onclick(*args, **kwargs)

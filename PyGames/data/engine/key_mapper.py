from dataclasses import dataclass

import pygame


@dataclass
class KeyMapper:
    move_left: int = 0
    move_right: int = 0
    move_up: int = 0
    move_down: int = 0

    action_1: int = 0
    action_2: int = 0
    action_3: int = 0

    @classmethod
    def from_set_1(cls):
        return cls(
            move_left=pygame.K_LEFT,
            move_right=pygame.K_RIGHT,
            move_up=pygame.K_UP,
            move_down=pygame.K_DOWN,
            action_1=pygame.K_q,
            action_2=pygame.K_w,
            action_3=pygame.K_e,
        )

    @classmethod
    def from_set_2(cls):
        return cls(
            move_left=pygame.K_a,
            move_right=pygame.K_d,
            move_up=pygame.K_w,
            move_down=pygame.K_s,
            action_1=pygame.K_i,
            action_2=pygame.K_o,
            action_3=pygame.K_p,
        )

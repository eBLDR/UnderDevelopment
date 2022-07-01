import pygame

from empires.manager import Manager

if __name__ == '__main__':
    pygame.init()
    manager = Manager()

    # TEST ONLY
    manager.test()

    manager.main()
    pygame.quit()

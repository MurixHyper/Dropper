from dropper_service import DropperService
from user_refactor_service import UserInterfaceService


def print_hi():
    dropper = DropperService()
    resetter = UserInterfaceService(dropper)
    while True:
        resetter.start()


if __name__ == '__main__':
    print_hi()

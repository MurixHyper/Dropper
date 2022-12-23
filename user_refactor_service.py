from dropper_service import DropperService

MENU = ("1. Get list from all users\n" +
      "2. Get info about current user\n" +
      "3. Drop or update the password\n" +
      "4. Exit from program\n")


class UserInterfaceService:
    def __init__(self, dropper: DropperService):
        self.__dropper = dropper

    def start(self):
        print("=" * 50)
        print(MENU)
        print("=" * 50)

        category = int(input())

        if category == 1:

            print("Available users:\n")
            print("\n".join(self.__dropper.get_all_users()))
            print("Want to see current user information? (y/n): ")

            username_checker = input()

            if username_checker == "y":
                print("Enter the username: ")
                additional_username = input()

                user_info = self.__dropper.get_current_user_info(additional_username)

                print(user_info)
                print("Do you want to drop or update password for this user? (y/n): ")

                agree_checker = input()

                if agree_checker == "y":
                    print("Enter the new password: ")

                    new_password = input()
                    self.__dropper.refresh_current_user_password(additional_username, new_password)

                elif agree_checker == "n":
                    print("Logging out")
                else:
                    print("Data is incorrect. Try again")
            elif username_checker == "n":
                print("Logging out")
            else:
                print("Data is incorrect. Try again")

        elif category == 2:
            print("Enter the username: ")

            username = input()

            user_info = self.__dropper.get_current_user_info(username)

            print(user_info)
            print("Do you want to drop or update password for this user? (y/n): ")

            agree_checker = input()

            if agree_checker == "y":
                print("Enter the new password: ")

                new_password = input()
                self.__dropper.refresh_current_user_password(username, new_password)

            elif agree_checker == "n":
                print("Logging out")
            else:
                print("Data is incorrect. Try again")

        elif category == 3:
            print("Enter the username: ")

            username = input()

            print("Enter the new password: ")

            new_password = input()
            self.__dropper.refresh_current_user_password(username, new_password)
        elif category == 4:
            pass
        else:
            print("Data is incorrect. Try again")

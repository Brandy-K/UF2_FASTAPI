from crud import read_users


def user_schema(user) -> dict:
    return {
        "id": user[0],
        "name": user[1],
        "surname": user[2],
    }


def users_schema(users) -> list:
    return [user_schema(user) for user in users]


def read():
    return read_users()

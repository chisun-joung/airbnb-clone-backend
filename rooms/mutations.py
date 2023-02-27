from strawberry.types import Info


def add_room(
    info: Info,
):
    print(user)
    user = info.context.request.user
    if user.is_authenticated:
        return user
    return None

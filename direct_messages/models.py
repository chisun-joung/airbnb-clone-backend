from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """ChattingRoom Model Definition"""

    user = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "ChattingRoom"


class Message(CommonModel):
    """Message Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.user} says: {self.text}"

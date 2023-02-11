from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """ChattingRoom Model Definition"""

    user = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms",
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
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.user} says: {self.text}"

import re

from rest_framework.exceptions import ValidationError


class YoutubeLinkValidator:

    def __init__(self, field_name):
        self.field = field_name

    def __call__(self, value):
        youtube_pattern = r"https://www.youtube.com/.*"
        if not re.search(youtube_pattern, value):
            raise ValidationError("Ссылка должна вести на YouTube")

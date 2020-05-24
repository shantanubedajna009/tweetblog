from django.dispatch import Signal

parsed_hastags = Signal(providing_args=["hashtag_list"])
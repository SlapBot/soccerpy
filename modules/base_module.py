from soccerpy.requester import Requester


class BaseModule:
    def __init__(self):
        self.r = Requester()

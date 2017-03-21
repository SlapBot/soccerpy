from soccerpy.modules.Fundamentals.fixtures import Fixtures


class FixturesAll:
    def __init__(self, data, headers):
        self.headers = headers
        self.time_frame_start = data['timeFrameStart']
        self.time_frame_end = data['timeFrameEnd']
        self.count = data['count']
        self.fixtures = Fixtures(data['fixtures'])

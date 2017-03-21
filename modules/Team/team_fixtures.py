from soccerpy.modules.Fundamentals.fixtures import Fixtures


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.team = links['team']['href']


class TeamFixtures:
    def __init__(self, data):
        self.links = Links(data['_links'])
        if 'timeFrameStart' in data:
            self.time_frame_start = data['timeFrameStart']
        if 'timeFrameEnd' in data:
            self.time_frame_end = data['timeFrameEnd']
        self.count = data['count']
        self.fixtures = Fixtures(data['fixtures'])

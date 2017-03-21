from soccerpy.modules.Fundamentals.fixtures import Fixture
from soccerpy.modules.Fundamentals.head2head import Head2Head


class FixturesSpecific:
    def __init__(self, data, headers):
        self.headers = headers
        self.fixture = Fixture(data['fixture'])
        self.head2head = Head2Head(data['head2head'])

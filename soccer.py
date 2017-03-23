from soccerpy.base import Base
from soccerpy import Competition, Fixture, Team


class Soccer(Base):
    def __init__(self, API_KEY="", response_format="full"):
        super(Soccer, self).__init__(API_KEY, response_format)
        self.competition = Competition(self.requester)
        self.fixture = Fixture(self.requester)
        self.Team = Team(self.requester)


if __name__ == "__main__":
    s = Soccer(API_KEY="05d52d8812a548c6a9f6f29ed60e8e00")

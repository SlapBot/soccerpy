import json
from soccerpy.base import Base
# from soccerpy import Competition, Fixture, Team


class Soccer(Base):
    def __init__(self, API_KEY=""):
        super(Soccer, self).__init__(API_KEY)
        # self.competition = Competition()
        # self.fixture = Fixture()
        # self.Team = Team()

    def set_API_KEY(self, API_KEY):
        self.API_KEY = API_KEY
        data = {"API_KEY": self.API_KEY}
        with open("api_key.txt", 'w') as outfile:
            json.dump(data, outfile)

if __name__ == "__main__":
    s = Soccer()
    s.set_API_KEY("05d52d8812a548c6a9f6f29ed60e8e00")
    # cs = s.competition.get_all()
    # print(cs)

from soccerpy.modules.base_module import BaseModule
from soccerpy.modules.Fixture.fixtures_all import FixturesAll
from soccerpy.modules.Fixture.fixtures_specific import FixturesSpecific


class Fixture(BaseModule):
    def __init__(self):
        super(Fixture, self).__init__()

    def get(self, time_frame=None, league=None, raw=False):
        data = self.r.request('fixtures', payload={"timeFrame": time_frame,
                                                   "league": league})
        if raw:
            return data
        return FixturesAll(data)

    def get_specific(self, fixture_id, head2head=None):
        data = self.r.request('fixture_specific', endpoint_format=fixture_id,
                              payload={"head2head": head2head})
        return FixturesSpecific(data)

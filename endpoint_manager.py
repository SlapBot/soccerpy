class EndpointManager:
    def __init__(self):
        self.base_url = "http://api.football-data.org"
        self.endpoints = self.get_endpoints()

    def get_endpoints(self):
        endpoints = {
            'competitions': self.base_url + '/v1/competitions/',
            # 'all_competitions': self.base_url + '/v1/competitions/',
            'competition_teams': self.base_url + '/v1/competitions/{}/teams',
            'competition_fixtures': self.base_url + '/v1/competitions/{}/fixtures',
            'fixture': self.base_url + '/v1/fixtures/',
            'all_fixtures': self.base_url + '/v1/fixtures/',
            'team': self.base_url + '/v1/teams/{}',
            'team_players': self.base_url + '/v1/teams/{}/players',
            'team_fixtures': self.base_url + '/v1/teams/{}/fixtures/',
            'league_table': self.base_url + '/v1/competitions/{}/leagueTable'
        }
        return endpoints

    def get_endpoint(self, name):
        return self.endpoints[name]

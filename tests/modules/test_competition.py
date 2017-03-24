import re
import unittest
import json
from soccerpy import Competition


class TestCompetition(unittest.TestCase):
    @staticmethod
    def do_init():
        c = Competition(API_KEY="05d52d8812a548c6a9f6f29ed60e8e00")
        return c

    @staticmethod
    def get_test_data():
        with open("testingdata/competition_tests_data.json") as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()
        return data

    @staticmethod
    def convert_to_snake_case(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def check_links(self, obj, key, value):
        temp_key = key[1:]
        for key2, value2 in value.items():
            sub_attribute = getattr(obj, temp_key)
            attribute_name = self.convert_to_snake_case(key2)
            if key2 == "self":
                attribute_name = self.convert_to_snake_case("url")
            attribute_value = getattr(sub_attribute, attribute_name)
            self.assertEqual(value2['href'], attribute_value)

    def check_location(self, obj, key, value):
        sub_attribute = getattr(obj, self.convert_to_snake_case(key))
        for key2, value2 in value.items():
            attribute_name = self.convert_to_snake_case(key2)
            attribute_value = getattr(sub_attribute, attribute_name)
            self.assertEqual(value2, attribute_value)

    def check_teams(self, obj, key, value):
        for key2, value2 in value.items():
            if key2 == "_links":
                self.check_links(obj, key2, value2)
            elif key2 == "squadMarketValue":
                continue
            elif key2 == "home" or key2 == "away":
                self.check_location(obj, key2, value2)
            elif key2 == "result":
                self.check_location(obj, key2, value2)
            else:
                attribute_name = self.convert_to_snake_case(key2)
                attribute_value = getattr(obj, attribute_name)
                self.assertEqual(value2, attribute_value)

    def test_competitions_all(self):
        c = self.do_init()
        comp = c.get_by_season(2015).competitions[0]
        data = self.get_test_data()['competitions_all']
        for key, value in data.items():
            if key == "_links":
                self.check_links(comp, key, value)
            else:
                attribute_name = self.convert_to_snake_case(key)
                attribute_value = getattr(comp, attribute_name)
                self.assertEqual(value, attribute_value)

    def test_competition_specific(self):
        c = self.do_init()
        comp = c.get_specific(398).competition
        data = self.get_test_data()['competition_specific']
        for key, value in data.items():
            if key == "_links":
                self.check_links(comp, key, value)
            else:
                attribute_name = self.convert_to_snake_case(key)
                attribute_value = getattr(comp, attribute_name)
                self.assertEqual(value, attribute_value)

    def test_competition_teams(self):
        c = self.do_init()
        comp = c.get_teams(398)
        data = self.get_test_data()['competition_teams']
        for key, value in data.items():
            if key == "_links":
                self.check_links(comp, key, value)
            elif key == "teams":
                self.check_teams(comp.teams[0], key, value[0])
            else:
                attribute_name = self.convert_to_snake_case(key)
                attribute_value = getattr(comp, attribute_name)
                self.assertEqual(value, attribute_value)

    def test_competition_league_table(self):
        c = self.do_init()
        comp = c.get_league_table_by_matchday(398, 28)
        data = self.get_test_data()['competition_league_table']
        for key, value in data.items():
            if key == "_links":
                self.check_links(comp, key, value)
            elif key == "standing":
                self.check_teams(comp.standing[0], key, value[0])
            else:
                attribute_name = self.convert_to_snake_case(key)
                attribute_value = getattr(comp, attribute_name)
                self.assertEqual(value, attribute_value)

    def test_competition_fixtures(self):
        c = self.do_init()
        comp = c.get_fixtures_by_matchday(398, 28)
        data = self.get_test_data()['competition_fixtures']
        for key, value in data.items():
            if key == "_links":
                self.check_links(comp, key, value)
            elif key == "fixtures":
                self.check_teams(comp.fixtures[0], key, value[0])
            else:
                attribute_name = self.convert_to_snake_case(key)
                attribute_value = getattr(comp, attribute_name)
                self.assertEqual(value, attribute_value)


if __name__ == "__main__":
    unittest.main()

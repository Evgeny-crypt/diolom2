import unittest
import diplom_2_VKinder as app
from unittest.mock import patch


class TestDiplom2(unittest.TestCase):
    token = '95834b030f75c1e776fd20a6fc0e3cdff6883c7e4d5a434a684aeed494969b36f5c3a3a702f1255babb4a'
    user = app.User(26472661)

    def test_get_list_top10_users(self):
        user_input = ["geter", "30", "35"]
        with patch('builtins.input', side_effect=user_input):
            list_top10_users = self.user.get_list_top10_users()
            self.assertIsInstance(list_top10_users, list)
            self.assertLessEqual(len(list_top10_users), 10)
            for user in list_top10_users:
                self.assertLessEqual(len(user['photos_top3']), 3)
                self.assertEqual(len(set(list(user.keys())).difference({"id", "weight", "photos_top3"})), 0)


if __name__ == '__main__':
    unittest.main()
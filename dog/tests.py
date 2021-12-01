from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from dog import views


class TestBreeds(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = views.BreedViewSet.as_view({'get': 'list'})
        self.uri = '/breeds/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        params = {
            "name": "qwerqwer",
            "size": "23",
            "friendliness": 21,
            "trainability": 21,
            "sheddingamount": 21,
            "exerciseneeds": 21
        }
        self.factory.post(self.uri, params)

    def test_update(self):
        params = {
            "name": "qqq"
        }
        self.factory.put(self.uri, params)

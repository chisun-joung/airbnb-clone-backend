from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):
    NAME = "test_amenity"
    DESC = "test_amenity_desc"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Status code should be 200",
        )

        self.assertIsInstance(
            data,
            list,
            "Data should be a list",
        )

        self.assertEqual(
            len(data),
            1,
            "Data should have 1 item",
        )

        self.assertEqual(
            data[0]["name"],
            self.NAME,
            "Name should be test_amenity",
        )

        self.assertEqual(
            data[0]["description"],
            self.DESC,
            "Description should be test_amenity_desc",
        )

    def test_create_amenity(self):
        new_amenity_name = "new_amenity"
        new_amenity_desc = "new_amenity_desc"

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_desc,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Status code should be 200",
        )

        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_desc,
        )

        response = self.client.post(self.URL)
        data = response.json()
        self.assertEqual(
            response.status_code,
            400,
            "Status code should be 400",
        )
        self.assertIn("name", data)


class TestAmenity(APITestCase):
    NAME = "test_amenity"
    DESC = "test_amenity_desc"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/999/")
        self.assertEqual(
            response.status_code,
            404,
            "Status code should be 404",
        )

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(
            response.status_code,
            200,
            "Status code should be 200",
        )

        data = response.json()
        self.assertEqual(
            data["name"],
            self.NAME,
            "Name should be test_amenity",
        )
        self.assertEqual(
            data["description"],
            self.DESC,
            "Description should be test_amenity_desc",
        )

    def test_put_amenity(self):
        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name": "updated_amenity",
                "description": "updated_amenity_desc",
            },
        )
        self.assertEqual(
            response.status_code,
            200,
            "Status code should be 200",
        )

        data = response.json()
        self.assertEqual(
            data["name"],
            "updated_amenity",
            "Name should be updated_amenity",
        )
        self.assertEqual(
            data["description"],
            "updated_amenity_desc",
            "Description should be updated_amenity_desc",
        )

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")
        self.assertEqual(
            response.status_code,
            204,
            "Status code should be 204",
        )

        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(
            response.status_code,
            404,
            "Status code should be 404",
        )


class TestRooms(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user",
        )
        user.set_password("test_password")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 403)
        self.client.force_login(self.user)

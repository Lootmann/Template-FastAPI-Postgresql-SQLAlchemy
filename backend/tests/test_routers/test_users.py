from random import randint, sample
from string import ascii_letters

from fastapi import status

from tests.init_client import client


def random_string(min_: int = 5, max_: int = 10) -> str:
    return "".join(sample(ascii_letters, randint(min_, max_)))


class TestGETUser:
    def test_get_all_user(self, client):
        resp = client.get("/users")
        assert resp.status_code == status.HTTP_200_OK


class TestPOSTUser:
    def test_create_user(self, client):
        resp = client.post("/users", json={"name": "hoge"})
        assert resp.status_code == status.HTTP_201_CREATED

    def test_create_many_users(self, client):
        for _ in range(10):
            resp = client.post("/users", json={"name": random_string()})
            assert resp.status_code == status.HTTP_201_CREATED

        resp = client.get("/users")
        assert resp.status_code == status.HTTP_200_OK
        assert len(resp.json()) == 10

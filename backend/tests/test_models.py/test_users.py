from api.models.users import User as UserModel


def test_model_repr():
    user = UserModel(id=1, name="Testmann")
    assert str(user) == f"<User (id, name) = (1, Testmann)>"

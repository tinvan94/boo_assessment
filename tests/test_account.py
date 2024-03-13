import json

from tests.base import BaseTestApp


class TestAccount(BaseTestApp):

    async def asyncSetUp(self) -> None:
        await super(TestAccount, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(TestAccount, self).asyncTearDown()

    async def test1(self):

        data = {
            "name"       : "A Martinez",
        }

        # create account
        response = self.client.post('/account',  json=data)
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['name'] == 'A Martinez'

        # get account
        response = self.client.get(f"/account/{str(resp['id'])}")
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['name'] == 'A Martinez'

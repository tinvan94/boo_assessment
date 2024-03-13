import json

from tests.base import BaseTestApp


class TestVote(BaseTestApp):

    async def asyncSetUp(self) -> None:
        await super(TestVote, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(TestVote, self).asyncTearDown()

    async def test1(self):

        data = {
            "account_id"       : "65f088afc2cf21e247b9fb83",
            "profile_id"       : "65f088afc2cf21e247b9fb83",
            "vote_option_id"   : "65f088afc2cf21e247b9fb83",
        }

        # like
        response = self.client.post('/vote',  json=data)
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['is_success']

        # unlike
        response = self.client.get(f"/votes")
        assert response.status_code == 200

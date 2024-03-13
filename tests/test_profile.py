import json

from tests.base import BaseTestApp


class TestProfile(BaseTestApp):

    async def asyncSetUp(self) -> None:
        await super(TestProfile, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(TestProfile, self).asyncTearDown()

    async def test1(self):

        data = {
            "name"       : "A Martinez",
            "description": "Adolph Larrue Martinez III.",
            "mbti"       : "ISFJ",
            "enneagram"  : "9w3",
            "variant"    : "sp/so",
            "tritype"    : 725,
            "socionics"  : "SEE",
            "sloan"      : "RCOEN",
            "psyche"     : "FEVL",
            "image"      : "https://soulverse.boo.world/images/1.png",
        }

        # create profile
        response = self.client.post('/profile',  json=data)
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['name'] == 'A Martinez'

        # get profile
        response = self.client.get(f"/profile/{str(resp['id'])}")
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['name'] == 'A Martinez'

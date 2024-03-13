
import json

from tests.base import BaseTestApp


class TestComment(BaseTestApp):

    async def asyncSetUp(self) -> None:
        await super(TestComment, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(TestComment, self).asyncTearDown()

    async def test1(self):

        data = {
            "title"       : "some title",
            "content"       : "some content",
            "account_id"       : "65f088afc2cf21e247b9fb83",
            "profile_id"       : "65f088afc2cf21e247b9fb83",
        }

        # create comment
        response = self.client.post('/comment',  json=data)
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['title'] == 'some title'

        # get comment
        params = {'profile_id': '65f088afc2cf21e247b9fb83'}
        response = self.client.get(f"/comments", params=params)
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp

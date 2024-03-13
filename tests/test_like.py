import json

from boo_app.database import like_collection
from tests.base import BaseTestApp


class TestLike(BaseTestApp):

    async def asyncSetUp(self) -> None:
        await super(TestLike, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(TestLike, self).asyncTearDown()

    async def test1(self):

        data = {
            "account_id"       : "65f088afc2cf21e247b9fb83",
            "comment_id"       : "65f088afc2cf21e247b9fb83",
        }

        # like
        response = self.client.post('/like',  json=data)
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['is_success']

        # unlike
        like = await like_collection.find_one({"comment_id": '65f088afc2cf21e247b9fb83'})
        response = self.client.delete(f"/like/{like['_id']}")
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp['is_delete']
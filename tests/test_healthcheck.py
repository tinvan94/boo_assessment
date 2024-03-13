
from tests.base import BaseTestApp

class TestHealthCheck(BaseTestApp):

    async def asyncSetUp(self) -> None:
        await super(TestHealthCheck, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(TestHealthCheck, self).asyncTearDown()

    async def test_succeed(self):
        response = self.client.get('/healthcheck')
        assert response.status_code == 200
        assert response.text == '{"system":"Boo App"}'

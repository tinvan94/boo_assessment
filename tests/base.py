try:
    import testtools as unittest
except ImportError:  # pragma: nocover
    import unittest  # type: ignore

from fastapi.testclient import TestClient

from boo_app.app import app


class BaseTestApp(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        self.client = TestClient(app)
        await super(BaseTestApp, self).asyncSetUp()

    async def asyncTearDown(self):
        await super(BaseTestApp, self).asyncTearDown()

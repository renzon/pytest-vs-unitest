import pytest

from setup_classes import Session, Connection


@pytest.fixture(scope='session', autouse=True)
def db_connection():
    conn = Connection()
    yield conn
    conn.close()


@pytest.fixture(scope='function')
def db_session():
    session = Session()
    yield session
    session.close()

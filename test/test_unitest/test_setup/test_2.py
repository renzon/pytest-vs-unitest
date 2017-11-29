from test.test_unitest.test_setup.base import SetupBaseTestCase


class Setup2TestCase(SetupBaseTestCase):
    def test_db_access_save(self):
        """Test db save"""
        print('######## running save')

    def test_db_access_delete(self):
        """Test db deletion"""
        print('######## running delete')

    def test_non_db_action(self):
        """Test does not depend on DB"""
        print('######## running non db')

# import server
# import unittest


# class DataBaseTesting(unittest.TestCase):
#     """Examples of integration tests: testing Flask server."""
#      def setUp(self):
#         """Stuff to do before every test."""

#         app.config["TESTING"] = True
#         app.config["SECRET_KEY"] = "key"
#         self.client = app.test_client()

#         # Connect to test database
#         connect_to_db(app, db_uri="postgresql:///testdb")
#         db.create_all()
#         load_all()

#         # Put user1 into session.
#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess["current_user"] = 1
#                 sess["model_year"] = 2011
#                 sess["make"] = "CHEVROLET"
#                 sess["model"] = "Cruze"

#     def tearDown(self):
#         """Do at end of every test."""

#         db.session.close()
#         db.drop_all()

#     def test_existing_user_correct(self):
#         client = server.app.test_client()
#         result = client.get('/login', data=)
#         self.assertIn(b'<h1>Color Form</h1>', result.data)


# if __name__ == '__main__':
#     unittest.main()
from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MaintTest(TestCase):
    def create_app(self):
        app.config["TESTING"]=True
        app.config["WTF_CSRF_ENABLED"]=False
        return app
    
    def test_app_exist_web(self):
        self.assertIsNotNone(current_app)

    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_auth_blueprint_exist(self):
        self.assertIn("auth",self.app.blueprints)

    def test_auth_blueprint_login_get(self):
        response = self.client.get(url_for("auth.login"))
        self.assert200(response)

    def test_auth_blueprint_login_template(self):
        self.client.get(url_for("auth.login"))
        self.assertTemplateUsed("login.html")
        self.ass


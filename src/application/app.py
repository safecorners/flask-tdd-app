from typing import Tuple

from flask import Flask, Response, jsonify

from application.endpoint import batch, person

# from application.imperative_database import db_session


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(person.bp)
    app.register_blueprint(batch.bp)
    # import application.imperative_models
    # from application.imperative_database import init_db

    # init_db()

    # u = application.imperative_models.User("hello", "hello@example.com")
    # db_session.add(u)
    # db_session.commit()
    # app.logger.info("intialized database.")

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     db_session.remove()

    @app.route("/health-check/")
    def health_check() -> Tuple[Response, int]:
        return jsonify({"status": "healthy"}), 200

    return app

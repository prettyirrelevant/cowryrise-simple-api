import os
import uuid
from datetime import datetime

from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)
BASE_DIR = app.root_path

# loads the configuration from ./settings/dev.py
app.config.from_pyfile(f"{os.path.join(BASE_DIR, 'settings', 'dev.py')}")

#  datastore for uuid
all_uuids = []


class UUIDView(MethodView):
    """
    Endpoint that returns all uuids generated while the server is running
    """

    def get(self):
        new_uuid = {datetime.now().isoformat(): uuid.uuid4()}
        all_uuids.append(new_uuid)

        return jsonify(all_uuids[::-1])


app.add_url_rule("/new-uuid", view_func=UUIDView.as_view("uuid-view"))

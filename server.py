
from flask import Flask

from model import connect_to_db, db

import crud 

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

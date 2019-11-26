from flask import jsonify

import connexion

# Creating the application instance.

app = connexion.App(__name__, specification_dir="./")

# Reading the yaml file to configure the endpoints.

app.add_api("cpu.yaml")


# Creating a URL route in our application for "/"

@app.route("/")
def home():
    msg = {"msg": "It's working!"}

    return jsonify(msg)


if __name__ == "__main__":
    app.run(port=8080, debug=True)

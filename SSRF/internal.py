from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🏠 Internal Admin Service - Forbidden"

@app.route("/secret")
def secret():
    return "🔐 FLAG{ssrf_access_to_internal_network_success}"

if __name__ == "__main__":
    app.run(port=9000)

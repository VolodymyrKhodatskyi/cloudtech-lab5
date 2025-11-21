from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "world")
    region = os.getenv("REGION", "unknown")
    runtime = "python"
    
    return jsonify({
        "hello": name,
        "runtime": runtime,
        "region": region
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

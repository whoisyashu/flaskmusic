from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

YOUTUBE_API_KEY = "AIzaSyCDdSKo8wARy2MfKT66hCvaJe5Npd5JjQE"
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

# Default Sidhu Moosewala Song
DEFAULT_SONG = "295 Sidhu Moosewala"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", DEFAULT_SONG)  # Use default song if no query

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    data = response.json()

    if "items" in data and data["items"]:
        video_id = data["items"][0]["id"]["videoId"]
        return jsonify({"videoId": video_id})

    return jsonify({"error": "No results found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

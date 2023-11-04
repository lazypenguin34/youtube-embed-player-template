from flask import Flask, render_template, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic()

@app.route('/')
def default():
    return render_template("player.html")

@app.route('/getVideoId/<query>', methods=['GET'])
def get_video_id(query):
    search = ytmusic.search(query, filter="songs")
    song_id = search[0]['videoId']
    return jsonify({'videoId': song_id})

app.run()
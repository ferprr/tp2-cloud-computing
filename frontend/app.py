from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/recommend', methods=['POST'])
def recommend_playlist():
    try:
        top3_playlists = [115,65, 76]
        response_data = {
            'playlist_ids': top3_playlists,
            'version': "image_tag",
            'model_date': "date"
        }
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=32180)
from flask import Flask, request, jsonify
import pandas as pd
import pickle

def getRelatedPlaylists(trackName):
    relatedPlaylists = []

    for trackName in trackName:
        relevantRules = model[
            model['antecedents'].apply(lambda x: trackName in str(x)) 
            | model['antecedents'].apply(lambda x: trackName in str(x))
        ]
        relevantRules = relevantRules.sort_values(by='confidence', ascending=False)
        for index, row in relevantRules.iterrows():
            if trackName in row['antecedents']:
                relatedPlaylists.extend(row['consequents'])
            if trackName in row['consequents']:
                relatedPlaylists.extend(row['antecedents'])

    return list(set(relatedPlaylists))

def countMatchingTracks(playlist, trackName):
    matchingCount = 0
    for trackName in trackName:
        if trackName in playlist:
            matchingCount += 1
    return matchingCount

def recommendPlaylists(trackName):
    playlist_counts = {}

    for index, row in ds1.iterrows():
        playlistName = row['pid']
        playlistTracks = row['trackName'].split(', ')
        matchingCount = countMatchingTracks(playlistTracks, trackName)
        matchingCount = 0
        for trackName in trackName:
            if trackName in playlistTracks:
                matchingCount += 1
        if playlistName in playlist_counts:
          playlist_counts[playlistName] += matchingCount
        else:
          playlist_counts[playlistName] = matchingCount

    sortedPlaylist = sorted(playlist_counts.items(), key=lambda x: x[1], reverse=True)
    top3Playlists = sortedPlaylist[:3]

    return [sublist[0] for sublist in top3Playlists]


app = Flask(__name__)

# Load your recommendation model here
model = pickle.load(open('./trained_model.pkl', "rb"))
file_path1 = './Datasets/2023_spotify_ds1.csv'
ds1 = pd.read_csv(file_path1)

@app.route('/api/recommend', methods=['POST'])
def recommend_playlist():
    try:
        data = request.get_json(force=True)
        songs = data['songs']

        recommendations = []

        recommendations = getRelatedPlaylists(songs)
        top3_playlists = recommendPlaylists(recommendations)

        response_data = {
            'playlist_ids': top3_playlists,
            'version': '1.0',  # Replace with your app version
            'model_date': '2023-11-02'  # Replace with the model update date
        }
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=32192)  # Adjust port and host as needed

"""A simple Flask application for emotion detection."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer() -> str:
    """Analyze the sentiment of the provided text and return the dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    detector = emotion_detector(text_to_analyze)

    if detector['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return jsonify(detector)

@app.route("/")
def render_index_page() -> str:
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
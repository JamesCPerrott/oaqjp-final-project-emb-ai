"""
This function initiates the application of emotion detection to be
executed over the Flask channel and deplyed on localhost:5000.
"""
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    This function renders the main application page
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """
    This code receivers text from the HTML interface and runs the emotion
    detector on it. The resulting dictionary is then returned to the HTML.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    #Submit input to analyzer
    response = emotion_detector(text_to_analyze)

    #error checking for no input
    if response['dominant_emotion'] == 'none':
        return "Invalid text! Please try again!"

    return response

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

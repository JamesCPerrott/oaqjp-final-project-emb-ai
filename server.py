"""
This function initiates the application of emotion detection to be
executed over the Flask channel and deployed on localhost:5000.
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
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}.</b>"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

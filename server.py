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

    #Check for no entered text
    if text_to_analyze == "":
        return "Invalid Input! Please enter some text."
    
    #Submit input to analyzer
    response = emotion_detector(text_to_analyze)

    return response

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function formats and POSTs a given text phrase to the Emotion Predict
    Library of the Watson Library
    """

    #generate the format, header, and location variables for the POST request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    #execute Post request
    response = requests.post(url, json = myobj, headers=header)

    #format response into json
    formatted_response = json.loads(response.text)

    # Access the first element in the list
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    
    #create a simplified response
    simplified_response = {
        "anger": emotion_data['anger'],
        "disgust": emotion_data['disgust'],
        "fear": emotion_data['fear'],
        "joy": emotion_data['joy'],
        "sadness": emotion_data['sadness']
    }

    #determine the dominant emotion and add to response
    dominant_emotion = max(simplified_response, key=simplified_response.get)
    simplified_response["dominant_emotion"] = dominant_emotion

    #console print for validation
    print(simplified_response)
    
    return simplified_response
    
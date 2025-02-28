import requests
import json

def emotion_detector(text_to_analyse):

    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Get the emotions dict
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Get the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Add the dominant emotion to the emotions dictionary
    emotions["dominant_emotion"] = dominant_emotion

    # Return the emotions dictionary
    return emotions
    




"""
from emotion_detection import emotion_detector
response = emotion_detector("I am so happy I am doing this")
print(response)

{
   "emotionPredictions":[
      {
         "emotion":{
            "anger":0.01364663,
            "disgust":0.0017160787,
            "fear":0.008986978,
            "joy":0.9719017,
            "sadness":0.055187024
         },
         "target":"",
         "emotionMentions":[
            {
               "span":{
                  "begin":0,
                  "end":27,
                  "text":"I love this new technology."
               },
               "emotion":{
                  "anger":0.01364663,
                  "disgust":0.0017160787,
                  "fear":0.008986978,
                  "joy":0.9719017,
                  "sadness":0.055187024
               }
            }
         ]
      }
   ],
   "producerId":{
      "name":"Ensemble Aggregated Emotion Workflow",
      "version":"0.0.1"
   }
}

"""

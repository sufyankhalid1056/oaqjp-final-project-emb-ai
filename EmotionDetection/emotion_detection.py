import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        jsonresponse = json.loads(response.text)

        emotions = jsonresponse["emotionPredictions"][0]["emotion"]

        max_score = max([emotionscore for emotionscore in emotions.values()])

        emotions["dominant_emotion"] = [emotion for emotion, score in emotions.items() if score == max_score][0]
        
        return emotions
    elif response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        return emotions
    else:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        return emotions
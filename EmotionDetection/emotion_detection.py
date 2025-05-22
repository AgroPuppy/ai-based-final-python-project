import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id":"emotion_aggregated-workflow_lang_en_stock"}
    jobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json =jobj , headers=header )

    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        joy_score = None
        fear_score = None
        sadness_score = None
        dominant_emotion = None
    else:
        analyzed_text = json.loads(response.text)

        emotions = analyzed_text['emotionPredictions'][0]['emotion']
        anger_score = emotions ['anger']
        disgust_score = emotions ['disgust']
        joy_score = emotions ['joy']
        fear_score = emotions ['fear']
        sadness_score = emotions ['sadness']
        
        dom_val = 0
        # Get largest value
        for key, val in emotions.items():
            if dom_val < val:
                dom_val = val
                dominant_emotion = key
    
    return { 'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion }
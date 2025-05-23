'''
Executing this function initiates the application of emotion
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_analyzer():
    '''This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detection()
        function. The output returned shows the emotions and thier
        respective scores, as well as the dominent emotion from a 
        given input.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text. Please try again"
    message = f'''For the given statement, the system response is
    'anger': {response['anger']}, 'disgust': {response['disgust']},
    'fear': {response['fear']}, 'joy': {response['joy']} and 
    'sadness': {response['sadness']}. The dominant emotion is 
    {response['dominant_emotion']}'''
    return message

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

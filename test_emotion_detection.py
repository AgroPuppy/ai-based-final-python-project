import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector(self):
        # Joy test
        joy_test = emotion_detector('I am glad this happened')
        self.assertEqual(joy_test['dominant_emotion'],'joy' )
        #Anger test
        anger_test = emotion_detector('I am really mad about this')
        self.assertEqual(anger_test['dominant_emotion'],'anger' )
        # Disgust test
        disgust_test = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_test['dominant_emotion'],'disgust' )
        # Sad test
        sad_test = emotion_detector('I am so sad about this')
        self.assertEqual(sad_test['dominant_emotion'],'sadness' )
        # Fear test
        fear_test = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_test['dominant_emotion'],'fear' )

unittest.main()
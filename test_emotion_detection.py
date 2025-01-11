from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):

        dominant_1 = emotion_detector('I am glad this happened')
        self.assertEqual(dominant_1['dominant_emotion'], 'joy')

        dominant_2 = emotion_detector('I am really mad about this')
        self.assertEqual(dominant_2['dominant_emotion'], 'anger')

        dominant_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(dominant_3['dominant_emotion'], 'disgust')

        dominant_4 = emotion_detector('I am so sad about this')
        self.assertEqual(dominant_4['dominant_emotion'], 'sadness')

        dominant_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(dominant_5['dominant_emotion'], 'fear')
        

unittest.main()
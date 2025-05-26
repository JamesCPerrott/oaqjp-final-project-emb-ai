from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase)
    def test_emotion_detector(self):
        #Test case for dominant joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqal(result_1['dominant_emotion'], 'joy')

        #Test case for dominant anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqal(result_2['dominant_emotion'], 'anger')

        #Test case for dominant disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqal(result_3['dominant_emotion'], 'disgust')

        #Test case for dominant sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqal(result_4['dominant_emotion'], 'sadness')

        #Test case for dominant fear
        result_5 = emotion_detector('I am reall afraid that htis will happen')
        self.assertEqal(result_5['dominant_emotion'], 'fear')

unittest.main()
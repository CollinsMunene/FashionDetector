import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey=os.environ.get('IBMBETHKEY'))

with open('<enter location of your saved image>', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='tops_1416667987').get_result()

print(json.dumps(classes, indent=2))
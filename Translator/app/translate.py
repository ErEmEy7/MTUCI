import os, requests, uuid, json
from key import subscription_translate_key, translate_location


def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_translate_key,
        'Ocp-Apim-Subscription-Region': translate_location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()

''' 
This module uses Watson APIs to create functions for translating from English to French 
and from French to English. 
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3 (
    version=VERSION_LT,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    ''' This function translate text input in English to French, and returns French text. '''

    translation_response = language_translator.translate(englishText, model_id='en-fr')
    translation = translation_response.get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    ''' This function translate text input in French to English, and returns English text. '''

    translation_response = language_translator.translate(frenchText, model_id='fr-en')
    translation = translation_response.get_result()
    englishText = translation['translations'][0]['translation']
    return englishText

'''This is a program to translate English text to French and
French text to English
using Watson Language Translator.'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2022-06-11' ,
    authenticator = auth
)
language_translator.set_service_url(url)
def english_to_french(english_text):
    '''This function translates English text to French'''
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    '''This function translates French text to English'''
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text

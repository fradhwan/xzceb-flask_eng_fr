"""
translation function
translate from english to french
and from french to english
"""
from deep_translator import MyMemoryTranslator as myTr

def english_to_french(english_text):
    """Translate from English to French"""    
    french_text = myTr(source='english',target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate from French to English"""    
    english_text = myTr(source='french',target='english').translate(french_text)
    return english_text
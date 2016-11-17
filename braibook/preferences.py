import yaml

class Preferences:
    PREF_PATH = 'resources/preferences.yml'
    ENCODING = {
        'EIGHT_DOT': 0,
        'SIX_DOT': 1}
    
    def __init__(self):
        self.speed = 1
        self.encoding = 0
        self.language = 0
        self.book_name = 0
        self.page_number =0
        self.current_word =0
        self.localization = 0
        
        
    def save_prefs(self):
        
    
    def load_prefs(self):
    
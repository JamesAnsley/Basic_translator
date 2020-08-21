from translate import Translator
from datetime import *
try:
    org_file = input("What file to translate (include extension please)  ")
    translator = Translator(to_lang='ja')
    with open(f'{org_file}', mode='r+') as to_trans:
        to_trans.seek(0)
        translation = translator.translate(to_trans.read())
        print(translation)
        to_trans.close()

    with open(f'.\\translated-files\\{org_file} translated-{datetime.now().strftime("%y%m%d-%H%M%S")}.txt', mode='w') as translated:
        print(str(translation))
        translated.close()
except FileNotFoundError as err:
    print('File not found')
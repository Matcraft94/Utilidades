import time
import keyboard
import random

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(characters)

time.sleep(5)


st = time.time()

count_characters = 0

tf = 60 * 30
while time.time() - st < tf:
    
    try:
        idx = random.randint(0, len(characters) - 1)
        keyboard.write(characters[idx])
        count_characters += 1
        wt = random.uniform(0, 2)
        time.sleep(wt)
    except:
        print('No se escribió un caracter')
    if count_characters == 1000:
        try:
            for i in range(count_characters):
                keyboard.send_keys("<backspace>")
            print(f'Se borraron {count_characters} caracteres')
            count_characters = 0
        except:
            print('No se pudieron borrar')
# keyboard.write("A")
print(f'Se escribieron {count_characters} caracteres')




import subprocess
from subprocess import CalledProcessError

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = meta_data.decode('utf-8', errors='backslashreplace')

data = data.split('\n')

profiles = []
for i in data:
    if 'ALL User Profile' in i:
        i = i.split(':')
        i = i[1]
        # print(f'Nombre del wifi:{i}')

        i = i[1:-1]
        # print(f'la contrasena es:{i}')

        profiles.append(i)

# print(profiles)

print('{:<30}|{:<}'.format('Wifi', 'Contrasena'))
print('-----------------------------------------------------')
for i in profiles:
    try:
        results = meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key = clear'])

        results = results.decode('utf-8', errors='backslashreplace')
        results = results.split('\n')

        results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
        try:
            print('{:<30}|{:<}'.format(i, results[0]))
        except IndexError:
                print('{:<30}|{:<}'.format(i),'')
    # except:
    #     print('Hubo un error')
    except subprocess.CalledProcessError:
        print('Hubo un error de decodficidado')

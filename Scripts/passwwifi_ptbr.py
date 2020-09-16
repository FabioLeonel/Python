#Pegar senha wifi em windows pt-br
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin-1').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "Todos os Perfis de Usu\xa0rios" in i]
print(f'{"Senha WiFi":^50}')
print('-' * 50)
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('latin-1').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Conte\xa3do da Chave" in b]
        try:
            print(f'{i:<30}|  {results[0]:<}')
        except IndexError:
            print(f'{i:<30}|  {"":<}')
    except subprocess.CalledProcessError:
        print(f'{i:<30}|  {"ENCODING ERROR":<}')
input("")

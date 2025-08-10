import os
import sys
import uuid
import base64
import json
import re
import hashlib
import datetime
import subprocess
import socket
import requests
import shutil
from difflib import unified_diff
from http.server import HTTPServer, SimpleHTTPRequestHandler

try:
    import qrcode
except ImportError:
    os.system('pip install qrcode[pil]')
    import qrcode

TODO_FILE = "todo.md"

# Utilidades Básicas

def help():
    print("uuid: Gera um UUID")
    print("genpass: Gera uma senha forte aleatória")
    print("timestamp: Mostra o timestamp atual (epoch e formato legível)")
    print("dateconv <ts>: Converte timestamp para data legível")
    print("base64enc <txt>: Codifica texto em Base64")
    print("base64dec <txt>: Decodifica texto em Base64")
    print("calc: Calculadora de terminal (suporta expressões)")
    print("color <hex>: Mostra cor RGB a partir de hex e vice-versa")
    print("qrgen <txt>: Gera um QR code a partir de texto/url")
    print("ls: Lista arquivos da pasta atual")
    print("cd <dir>: Muda de diretório")
    print("mkdir <nome>: Cria uma nova pasta")
    print("open <arquivo>: Abre arquivo no editor padrão")
    print("search <termo>: Busca por arquivos com o nome que contenha <termo>")
    print("read <arquivo>: Lê o conteúdo de um arquivo no terminal")
    print("touch <nome>: Cria um novo arquivo vazio")
    print("gitstatus: Mostra status atual do repositório Git")
    print("gitbranch: Lista branches")
    print("gitlog: Mostra últimos 5 commits")
    print("gitreset: Reset hard para o último commit (requer confirmação)")
    print("gpush: Atalho para git add . && git commit -m "" && git push")
    print("ip: Mostra IP local e público")
    print("ping <site>: Faz ping e mede latência")
    print("httpget <url>: Requisição GET e exibe JSON formatado")
    print("headers <url>: Exibe cabeçalhos HTTP da URL")
    print("speedtest: Testa velocidade de download e upload da sua rede Wi-Fi")
    print("jsonfmt <arquivo>: Formata arquivo JSON")
    print("jsonval <arquivo>: Valida sintaxe JSON")
    print("regex <texto> <exp>: Testa expressão regular")
    print("minify <arquivo>: Minifica HTML, CSS ou JS")
    print("diff <arq1> <arq2>: Mostra diferenças entre dois arquivos")
    print("hash <texto>: Gera hash SHA256")
    print("comparehash <t1> <t2>: Compara dois hashes")
    print("securedel <arq>: Deleta um arquivo com sobrescrita segura")
    print("serve: Sobe um servidor HTTP simples na pasta atual (requer confirmação)")
    print("portscan <ip>: Escaneia portas abertas em um IP")
    print("dockerps: Lista containers Docker em execução")
    print("dockerstart <id>: Inicia container Docker")
    print("ssh <host>: Acessa um servidor via SSH")
    print("todo: Lista tarefas do dev (em arquivo markdown)")
    print("addtodo '<tarefa>': Adiciona uma tarefa")
    print("deltodo <id>: Remove tarefa específica")
    print("exit: Fecha a janela do DevShell")

def generate_uuid():
    print(uuid.uuid4())

def generate_password():
    import secrets, string
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(16))
    print(password)

def current_timestamp():
    ts = int(datetime.datetime.now().timestamp())
    print(f"Epoch: {ts}\nData: {datetime.datetime.now()}")

def convert_timestamp(ts):
    print(datetime.datetime.fromtimestamp(int(ts)))

def base64_encode(text):
    print(base64.b64encode(text.encode()).decode())

def base64_decode(text):
    print(base64.b64decode(text.encode()).decode())

def calculator():
    try:
        expr = input("Digite a expressão: ")
        print(eval(expr))
    except:
        print("Expressão inválida.")

def color(hexcode):
    if hexcode.startswith('#'):
        hexcode = hexcode[1:]
    if len(hexcode) == 6:
        r, g, b = tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4))
        print(f"RGB: ({r}, {g}, {b})")
    elif ',' in hexcode:
        r, g, b = map(int, hexcode.split(','))
        print('#{:02x}{:02x}{:02x}'.format(r, g, b))

def qrgen(text):
    img = qrcode.make(text)
    img.show()

# Manipulação de arquivos e sistema
def ls():
    print('\n'.join(os.listdir()))

def cd(dir):
    os.chdir(dir)

def mkdir(name):
    os.makedirs(name, exist_ok=True)

def open_file(file):
    os.system(f'start {file}' if os.name == 'nt' else f'xdg-open {file}')

def search(term):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if term in file:
                print(os.path.join(root, file))

def read(file):
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())

def touch(name):
    open(name, 'a').close()

# Git helpers
def git_status(): os.system("git status")
def git_branch(): os.system("git branch")
def git_log(): os.system("git log -5")
def git_reset():
    confirm = input("Tem certeza? (s/n): ")
    if confirm.lower() == 's':
        os.system("git reset --hard")
def gpush():
    msg = input("Mensagem do commit: ")
    os.system(f"git add . && git commit -m \"{msg}\" && git push")

# Rede e API
def ip():
    print(f"Local: {socket.gethostbyname(socket.gethostname())}")
    print(f"Público: {requests.get('https://api.ipify.org').text}")

def ping(site):
    os.system(f"ping {'-n' if os.name == 'nt' else '-c'} 4 {site}")

def httpget(url):
    r = requests.get(url)
    print(json.dumps(r.json(), indent=2))

def headers(url):
    r = requests.head(url)
    print(dict(r.headers))

def speedtest():
    try:
        # tenta rodar o binário externo
        exit_code = os.system("speedtest --secure")
        if exit_code != 0:
            raise RuntimeError("Comando externo falhou")
    except Exception:
        print("[Aviso] O comando externo 'speedtest' falhou ou não está disponível.")
        print("Executando teste de velocidade via biblioteca Python integrada...")
        try:
            import speedtest as st
        except ImportError:
            os.system('pip install speedtest-cli')
            import speedtest as st
        
        s = st.Speedtest()
        s.get_best_server()
        print(f"Ping: {s.results.ping} ms")
        print(f"Download: {s.download()/1_000_000:.2f} Mbps")
        print(f"Upload: {s.upload()/1_000_000:.2f} Mbps")


# Codificação, JSON, Regex
def jsonfmt(file):
    with open(file, 'r+') as f:
        data = json.load(f)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def jsonval(file):
    try:
        json.load(open(file))
        print("JSON válido")
    except Exception as e:
        print(f"Erro: {e}")

def regex(text, expr):
    matches = re.findall(expr, text)
    print(matches)

def minify(file):
    with open(file, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.write(re.sub(r"\s+", " ", content))
        f.truncate()

def diff(f1, f2):
    with open(f1) as a, open(f2) as b:
        print(''.join(unified_diff(a.readlines(), b.readlines())))

# Segurança
def hash_text(text):
    print(hashlib.sha256(text.encode()).hexdigest())

def compare_hash(t1, t2):
    print("Iguais" if t1 == t2 else "Diferentes")

def securedel(file):
    with open(file, 'ba+') as f:
        f.seek(0)
        f.write(os.urandom(os.path.getsize(file)))
    os.remove(file)

# DevOps e servidores
def serve():
    print("ATENÇÃO: APÓS A CONFIRMAÇÃO, O SERVIÇO NA PORTA 8000 SERÁ INFINITO")
    print("(A MENOS QUE FORCE UMA PARADA). DESEJA REALMENTE CONTINUAR?")
    confirm = input("Digite s/n: ")
    if confirm.lower() == 's':
        HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler).serve_forever()
    else:
        print("Serviço cancelado.")

def portscan(ip):
    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                print(f"Porta {port} aberta")

def dockerps(): os.system("docker ps")
def dockerstart(cid): os.system(f"docker start {cid}")
def ssh(host): os.system(f"ssh {host}")

# Projetos e organização
def list_todo():
    if os.path.exists(TODO_FILE):
        print(open(TODO_FILE).read())
    else:
        print("Nenhuma tarefa registrada.")

def add_todo(task):
    with open(TODO_FILE, 'a') as f:
        f.write(f"- {task}\n")

def del_todo(index):
    lines = open(TODO_FILE).readlines()
    with open(TODO_FILE, 'w') as f:
        for i, line in enumerate(lines):
            if i != int(index):
                f.write(line)

# Dispatcher
COMMANDS = {
    "help": help
    "uuid": generate_uuid,
    "genpass": generate_password,
    "timestamp": current_timestamp,
    "dateconv": lambda arg: convert_timestamp(arg),
    "base64enc": lambda arg: base64_encode(arg),
    "base64dec": lambda arg: base64_decode(arg),
    "calc": calculator,
    "color": lambda arg: color(arg),
    "qrgen": lambda arg: qrgen(arg),
    "ls": ls,
    "cd": lambda arg: cd(arg),
    "mkdir": lambda arg: mkdir(arg),
    "open": lambda arg: open_file(arg),
    "search": lambda arg: search(arg),
    "read": lambda arg: read(arg),
    "touch": lambda arg: touch(arg),
    "gitstatus": git_status,
    "gitbranch": git_branch,
    "gitlog": git_log,
    "gitreset": git_reset,
    "gpush": gpush,
    "ip": ip,
    "ping": lambda arg: ping(arg),
    "httpget": lambda arg: httpget(arg),
    "headers": lambda arg: headers(arg),
    "speedtest": speedtest,
    "jsonfmt": lambda arg: jsonfmt(arg),
    "jsonval": lambda arg: jsonval(arg),
    "regex": lambda txt, expr: regex(txt, expr),
    "minify": lambda arg: minify(arg),
    "diff": lambda a1, a2: diff(a1, a2),
    "hash": lambda arg: hash_text(arg),
    "comparehash": lambda t1, t2: compare_hash(t1, t2),
    "securedel": lambda arg: securedel(arg),
    "serve": serve,
    "portscan": lambda ip: portscan(ip),
    "dockerps": dockerps,
    "dockerstart": lambda cid: dockerstart(cid),
    "ssh": lambda host: ssh(host),
    "todo": list_todo,
    "addtodo": lambda task: add_todo(task),
    "deltodo": lambda idx: del_todo(idx)
}

def main():
    while True:
        try:
            cmd = input("devshell> ").strip()
            if not cmd:
                continue
            if cmd == "exit":
                break
            parts = cmd.split()
            c = parts[0]
            args = parts[1:]
            if c in COMMANDS:
                func = COMMANDS[c]
                func(*args)
            else:
                print("Comando desconhecido.")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()





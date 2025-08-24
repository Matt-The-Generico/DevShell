# COMANDOS DO DEVSHELL #
### 1. Utilidades básicas

Comando	| Função

help  Mostra todos os comandos do DevShell

uuid	Gera um UUID
genpass	Gera uma senha forte aleatória

timestamp	Mostra o timestamp atual (epoch e formato legível)

dateconv <ts>	Converte timestamp para data legível

base64enc <txt>	Codifica texto em Base64

base64dec <txt>	Decodifica texto em Base64

calc	Calculadora de terminal (suporta expressões: 2+2*3)

color <hex>	Mostra cor RGB a partir de hex e vice-versa

qrgen <txt>	Gera um QR code a partir de texto/url

### 2. Manipulação de arquivos e sistema
Comando |	Função

ls	Lista arquivos da pasta atual

cd <dir>	Muda de diretório

mkdir <nome>	Cria uma nova pasta

open <arquivo>	Abre arquivo no editor padrão

search <termo>	Busca por arquivos com o nome que contenha <termo>

read <arquivo>	Lê o conteúdo de um arquivo no terminal

touch <nome>	Cria um novo arquivo vazio

### 3. Git helpers (acessos rápidos)

Comando	| Função

gitstatus	Mostra status atual do repositório Git

gitbranch	Lista branches

gitlog	Mostra últimos 5 commits

gitreset	Reset hard para o último commit (com confirmação)

gpush	Atalho para git add . && git commit -m "" && git push

### 4. Rede e API

Comando |	Função

ip	Mostra IP local e público

ping <site>	Faz ping e mede latência

httpget <url>	Requisição GET e exibe JSON formatado

headers <url>	Exibe cabeçalhos HTTP da URL

speedtest Faz teste de download e upload da sua rede Wi-Fi

### 5. Codificação, JSON, Regex

Comando |	Função

jsonfmt <arquivo>	Formata arquivo JSON

jsonval <arquivo>	Valida sintaxe JSON

regex <texto> <exp>	Testa expressão regular

minify <arquivo>	Minifica HTML, CSS ou JS

diff <arq1> <arq2>	Mostra diferenças entre dois arquivos

### 6. Segurança

Comando |	Função

hash <texto>	Gera hash SHA256

comparehash <t1> <t2>	Compara dois hashes

securedel <arq>	Deleta um arquivo com sobrescrita segura

### 7. DevOps e servidores

Comando |	Função

serve	Sobe um servidor HTTP simples na pasta atual

portscan <ip>	Escaneia portas abertas em um IP

dockerps	Lista containers Docker em execução

dockerstart <id>	Inicia container Docker

ssh <host>	Acessa um servidor via SSH

### 8. Projetos e organização

Comando |	Função

todo	Lista tarefas do dev (em arquivo markdown)

addtodo "<tarefa>"	Adiciona uma tarefa

deltodo <id>	Remove tarefa específica

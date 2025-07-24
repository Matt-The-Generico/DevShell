DevShell é uma ferramenta de terminal para desenvolvedores, feita em Python, que fornece dezenas de comandos úteis, desde utilidades básicas até ferramentas DevOps, rede, segurança e produtividade.

Criado para desenvolvedores que querem um terminal mais inteligente, completo e ágil.

⚙️ Instalação
Baixe o repositório:

git clone https://github.com/seu-usuario/DevShell.git
cd DevShell

Execute o DevShell:
DevShell.py

🧠 Comandos disponíveis
Organizados em categorias:

🔹 Utilidades básicas
uuid – Gera um UUID.

genpass – Gera uma senha aleatória forte.

timestamp – Mostra o timestamp atual.

dateconv <ts> – Converte timestamp para data.

base64enc <txt> – Codifica em Base64.

base64dec <txt> – Decodifica Base64.

calc – Calculadora com expressões.

color <hex> – Converte HEX ↔ RGB.

qrgen <txt> – Gera QR code.

🧩 Arquivos e sistema
ls, cd, mkdir, touch, read, search, open

⚙️ Git Helpers
gitstatus, gitbranch, gitlog, gitreset, gpush

🌐 Rede e API
ip, ping, httpget, headers, portscan

🧪 JSON, Regex, Codificação
jsonfmt, jsonval, regex, minify, diff

🔐 Segurança
hash, comparehash, securedel

🚀 DevOps e Servidores
serve, portscan, dockerps, dockerstart, ssh

🛠️ Produtividade do Dev
todo, addtodo, deltodo

❗Avisos
Alguns comandos exigem Docker instalado, acesso à internet ou permissões administrativas.

O DevShell é uma ferramenta local e não coleta nenhum dado do usuário.

Use com responsabilidade. Ferramentas como securedel e gitreset são destrutivas.

Copyright (c) [2025] Matttz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software (DevShell) and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

1. O aviso de copyright e esta permissão deverão ser incluídos em todas as cópias
ou partes substanciais do Software.

2. O Software é fornecido "no estado em que se encontra", sem garantias de qualquer tipo,
expressas ou implícitas, incluindo, mas não se limitando a garantias de comercialização,
adequação a uma finalidade específica e não violação.

3. Em nenhuma hipótese os autores ou detentores dos direitos poderão ser responsabilizados
por qualquer reivindicação, dano ou outra responsabilidade, seja em ação contratual,
tortuosa ou de outra forma, decorrente de ou em conexão com o Software ou o uso
ou outros negócios no Software.

4. O usuário assume total responsabilidade por **operações destrutivas** realizadas com comandos como:
   - `securedel`
   - `gitreset`
   - `dockerstart`
   - `ssh`

5. O DevShell **não deve ser utilizado para fins maliciosos**, invasivos ou ilegais, incluindo:
   - Escaneamento de portas sem autorização (`portscan`)
   - Ataques automatizados ou extração de dados via `httpget` ou `headers`

6. O uso desta ferramenta implica na **aceitação total destes termos**.


📧 Contato
Tem sugestões, bugs ou ideias novas de comando?
Entre em contato: genericgamesgg@gmail.com ou abra uma Issue no GitHub!

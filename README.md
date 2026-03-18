# Netspecter Pro Max

## Descrição
Netspecter Pro Max é uma ferramenta avançada de monitoramento de rede que fornece **informações em tempo real sobre tráfego, desempenho e alertas de segurança**.  
Ideal para administradores que querem **controlar e analisar suas redes** de forma rápida e prática.

---

## Funcionalidades
- Monitoramento de tráfego em tempo real
- Coleta de métricas de desempenho
- Alertas de segurança
- Interface amigável
- Suporte multi-plataforma (Windows, Linux, macOS)

---

## Instalação e Execução no Linux (Kali, Ubuntu, etc)

Siga estes passos **exatamente**, sem pular nada:

1. Abra o terminal.  
2. Atualize os pacotes do sistema:
   ```bash
   sudo apt update && sudo apt upgrade -y

Instale pacotes necessários:

sudo apt install -y python3 python3-pip git build-essential

Clone o repositório:

git clone https://github.com/luanisaque3/netspecter-pro-max.git

Entre na pasta do projeto:

cd netspecter-pro-max

Crie um ambiente virtual Python (recomendado):

python3 -m venv venv
source venv/bin/activate

Instale todas as dependências do projeto:

pip install -r requisitos.txt

Dê permissão de execução para o script:

chmod +x netspecter.py

Rode o aplicativo:

sudo python3 netspecter.py

⚠️ Obs: sudo é necessário para capturar pacotes de rede em Linux/Kali.

Uso do Netspecter

Abra o aplicativo.

Configure suas preferências na aba Configurações.

Clique em Start Monitoring para iniciar a captura de pacotes.

Clique em Stop Monitoring para parar a captura.

Gere relatórios conforme necessário.

Capturas de Tela

Painel Principal: Estatísticas e alertas em tempo real

Configurações: Personalize monitoramento e alertas

Relatórios: Gera relatórios detalhados do uso da rede

Solução de Problemas

Aplicativo não inicia: Certifique-se de ter instalado todas as dependências.

Permissão negada: Execute chmod +x netspecter.py ou use sudo.

Problemas ao clonar: Verifique a instalação do Git e a conexão com a internet.

Licença

MIT License – veja LICENSE
 para detalhes

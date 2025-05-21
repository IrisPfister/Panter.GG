import requests
from bs4 import BeautifulSoup
import json

url_lolesports = "https://maisesports.com.br/campeonatos/league-of-legends-lta-sul-split-2-2025/"

try:
    response = requests.get(url_lolesports)
    response.raise_for_status()
    html_content = response.text
    print("Página acessada com sucesso!")
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a página: {e}")
    html_content = None

next_data_json = None
if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')
    print("HTML da página parseado com sucesso!")

    # Tenta encontrar o script com o id "__NEXT_DATA__"
    next_data_script = soup.find('script', {'id': '__NEXT_DATA__'})
    if next_data_script:
        print("Script '__NEXT_DATA__' encontrado!")
        try:
            next_data_json = json.loads(next_data_script.string)
            print("Dados JSON extraídos com sucesso!")
            # Podemos imprimir um trecho para ver o que tem dentro
            # import pprint
            # pprint.pprint(next_data_json['props']['pageProps']['serie'])
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON.")
    else:
        print("Script com id '__NEXT_DATA__' não encontrado.")
else:
    print("Não foi possível obter o conteúdo da página.")

def processar_pergunta(pergunta):
    """
    Processa a pergunta do usuário e tenta identificar a intenção.
    Retorna uma resposta ou uma mensagem de "não entendi".
    """
    pergunta = pergunta.lower()

    palavras_chave_proxima_partida = ["quando", "próximo", "jogo", "partida", "vai jogar", "proximo jogo"]
    palavras_chave_ultimo_resultado = ["resultado", "último", "ultimojogo", "perdeu", "ganhou"]
    palavras_chave_escalacao = ["escalação", "jogadores", "quem joga"]
    palavras_chave_assistir = ["onde", "assistir", "ver", "transmitir"]
    palavras_chave_saudacao = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "e aí"]
    palavras_chave_agradecimento = ["obrigado", "obrigada", "valeu"]

    if any(palavra in pergunta for palavra in palavras_chave_proxima_partida):
        if next_data_json:
            return "Buscando a próxima partida da Fúria..."
        else:
            return "Não consegui acessar os dados das partidas no momento."

    elif any(palavra in pergunta for palavra in palavras_chave_ultimo_resultado):
        if next_data_json:
            return "Buscando o último resultado da Fúria..."
        else:
            return "Não consegui acessar os dados das partidas no momento."

    elif any(palavra in pergunta for palavra in palavras_chave_escalacao):
        return "A escalação atual da Fúria em LoL geralmente inclui: [Nome do Topo], [Nome do Caçador], [Nome do Meio], [Nome do Atirador] e [Nome do Suporte]. Para a escalação específica do próximo jogo, consulte a página oficial!"

    elif any(palavra in pergunta for palavra in palavras_chave_assistir):
        return "Você pode assistir aos jogos da Fúria nos canais oficiais da Riot Games na Twitch e YouTube."

    elif any(palavra in pergunta for palavra in palavras_chave_saudacao):
        return "Olá, Furiano! Como posso te ajudar hoje?"

    elif any(palavra in pergunta for palavra in palavras_chave_agradecimento):
        return "De nada! Sempre à disposição para a torcida Furiosa!"

    else:
        return "Desculpe, não entendi sua pergunta. Posso te ajudar com informações sobre a Fúria, como próximos jogos, resultados ou escalação."

# Loop principal para interação com o usuário (para testar no terminal)
if __name__ == "__main


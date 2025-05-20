def processar_pergunta(pergunta):
    """
    Processa a pergunta do usuário e tenta identificar a intenção.
    Retorna uma resposta ou uma mensagem de "não entendi".
    """
    pergunta = pergunta.lower() # Converte a pergunta para minúsculas para facilitar a comparação

    # Listas de palavras-chave para diferentes intenções
    palavras_chave_proxima_partida = ["quando", "próximo", "jogo", "partida", "vai jogar", "proximo jogo"]
    palavras_chave_ultimo_resultado = ["resultado", "último", "ultimojogo", "perdeu", "ganhou"]
    palavras_chave_escalacao = ["escalação", "jogadores", "quem joga"]
    palavras_chave_assistir = ["onde", "assistir", "ver", "transmitir"]
    palavras_chave_saudacao = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "e aí"]
    palavras_chave_agradecimento = ["obrigado", "obrigada", "valeu"]

    # Lógica para identificar a intenção
    if any(palavra in pergunta for palavra in palavras_chave_proxima_partida):
        return "A Fúria joga contra a [Nome do Adversário] no dia [Data] às [Horário] pelo [Campeonato]. Fique ligado!"
    
    elif any(palavra in pergunta for palavra in palavras_chave_ultimo_resultado):
        return "No último jogo, a Fúria [Resultado, ex: venceu/perdeu] a [Nome do Adversário] por [Placar, ex: 2x1] pelo [Campeonato]."

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
if __name__ == "__main__":
    print("Olá! Eu sou o Panter.GG, seu bot da Fúria!")
    print("Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Até a próxima, Furiano! Go Fúria!")
            break
        
        resposta_bot = processar_pergunta(user_input)
        print(f"Panter.GG: {resposta_bot}")

import requests
from bs4 import BeautifulSoup

url_lolesports = "https://lolesports.com/pt-BR/news/welcome-to-the-lta"

try:
    response = requests.get(url_lolesports)
    response.raise_for_status()  # Lança uma exceção para status de erro HTTP
    html_content = response.text
    print("Página acessada com sucesso!")
    # print(html_content[:500]) # Imprime os primeiros 500 caracteres para visualização
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a página: {e}")
    html_content = None

if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')
    # usar o 'soup' para encontrar informações específicas no HTML
    print("HTML da página parseado com sucesso!")
else:
    print("Não foi possível obter o conteúdo da página.")

# O restante do seu código (função processar_pergunta e loop principal) pode vir aqui
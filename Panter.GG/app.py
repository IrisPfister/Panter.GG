from flask import Flask, request, jsonify
from flask_cors import CORS
import beautifulsoup4

app = Flask(__name__)
CORS(app)

def buscar_proximo_jogo():
    try:
        url = "https://api.aureom.tech/api/schedule"
        resposta = resposta.get(url)

        if resposta.status_code != 200:
            return "Erro ao acessar o site de partidas."

        dados = resposta.json()

        for partida in dados:
            if "FURIA" in (partida.get("team1", "") + partida.get("team2", "")):
                nome1 = partida.get("team1")
                nome2 = partida.get("team2")
                data = partida.get("start_time", "")[:10]
                hora = partida.get("start_time", "")[11:16]

                adversario = nome2 if nome1 == "FURIA" else nome1
                return f"O próximo jogo da FURIA será contra {adversario} no dia {data} às {hora}."

        return "Nenhum jogo da FURIA encontrado na programação."
    except Exception as e:
        return f"Erro ao buscar dados: {str(e)}"

def buscar_ultimo_jogo():
    try:
        url = "https://api.aureom.tech/api/schedule"
        resposta = resposta.get(url)

        if resposta.status_code != 200:
            return "Erro ao acessar o site de partidas."

        dados = resposta.json()

        for partida in dados:
            if "FURIA" in (partida.get("team1", "") + partida.get("team2", "")):
                nome1 = partida.get("team1")
                nome2 = partida.get("team2")
                data = partida.get("start_time", "")[:10]
                hora = partida.get("start_time", "")[11:16]

                adversario = nome2 if nome1 == "FURIA" else nome1
                return f"O último jogo da FURIA foi contra {adversario} no dia {data} às {hora}."

        return "Nenhum jogo da FURIA encontrado na programação."
    except Exception as e:
        return f"Erro ao buscar dados: {str(e)}"

@app.route("/mensagem", methods=["POST"])
def responder():
    dados = request.get_json()
    pergunta = dados.get("mensagem", "").strip().lower()

    
    if "próximo jogo" in pergunta or "quando a fúria joga" in pergunta:
        return jsonify({"resposta": buscar_proximo_jogo()})
    if "contra quem jogou" in pergunta or "último adversário" in pergunta:
        return jsonify({"resposta": buscar_ultimo_jogo()})

    respostas = {
        "contra quem a fúria jogou na final?": "A FURIA enfrentou a LOUD",
        "onde posso assistir ao replay do jogo da fúria?": "Você pode assistir no canal oficial da Riot Games no YouTube.",
        "há alguma previsão ou análise para o próximo confronto?": "A FURIA está em boa fase e é considerada favorita. Inclusive venceu o Lta Sul 2025",
        "qual foi o resultado do último jogo da fúria?": "A FURIA venceu por 3x0 contra a paiN Gaming.",
        "quem jogou pela fúria na última partida?": "fGuigo (Top), Tatu (Jungle), Tutsz (Mid), Ayu (ADC) e JoJo (Sup).",
        "qual foi o placar da série contra a loud?": "A FURIA perdeu por 2x0.",
        "onde posso ver o replay da última partida?": "No canal LoL Esports BR no YouTube.",
        "quem foram os destaques da fúria no último jogo?": "O Tatu teve uma performance excelente.",
        "em qual campeonato a fúria está jogando agora?": "A FURIA volta ao servidor no próximo dia 27 de junho para a disputa do MSI 2025, que vai até o dia 12 de julho. Depois, na Esports World Cup, o time estreia no dia 16 de julho na disputa que vai até o dia 20 do mesmo mês!.",
        "quando será a final do cblol 2025?": "A final será no dia 10 de agosto.",
        "qual é a escalação atual da fúria?": "Guigo (Top), Tatu (Jungle), Tutsz (Mid), Ayu (ADC) e JoJo (Sup).",
        "quem são os jogadores da fúria?": "Guigo (Top), Tatu (Jungle), Tutsz (Mid), Ayu (ADC) e JoJo (Sup) .",
        "houve alguma mudança recente na equipe?": "Não houve mudanças na equipe da FURIA.",
        "quais informações você pode me dar?": "Posso falar sobre jogos, escalações, resultados e o campeonato atual da FURIA.",
        "como você funciona?": "Recebo sua pergunta, comparo com o que sei e respondo sobre a FURIA Esports!"
    }

    resposta = respostas.get(pergunta, "Desculpe, não entendi sua pergunta. Pode reformular?")
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)


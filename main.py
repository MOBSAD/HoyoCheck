import requests
from dotenv import load_dotenv
import os

# carrega o dotenv
load_dotenv()

# pega os dados de dentro do env
ltoken_v2 = os.getenv("LTOKEN_V2")
ltuid_v2 = os.getenv("LTUID_V2")

# define cookies
COOKIES = f"ltoken_v2={ltoken_v2}; ltuid_v2={ltuid_v2};"

# jogos os quais vão ser feitos os check-in
GAMES = {
    "Genshin Impact": {
        "url": "https://sg-hk4e-api.hoyolab.com/event/sol/sign",
        "act_id": "e202102251931481",
    },
    "Honkai: Star Rail": {
        "url": "https://sg-public-api.hoyolab.com/event/luna/os/sign",
        "act_id": "e202303301540311",
    },
    "Zenless Zone Zero": {
        "url": "https://sg-public-api.hoyolab.com/event/luna/zzz/os/sign",  # endpoint novo
        "act_id": "e202406031448091",
        "extra_headers": {"x-rpc-signgame": "zzz"},
    },
}

BASE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": COOKIES,
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Origin": "https://act.hoyolab.com",
    "Referer": "https://act.hoyolab.com/",
    "x-rpc-app_version": "2.34.1",
    "x-rpc-client_type": "4",
}


def executar_checkin():
    print("[ CHECK-IN AUTOMATICO HOYOLAB INICIADO ]\n")

    for game_name, data in GAMES.items():
        headers = {**BASE_HEADERS, **data.get("extra_headers", {})}
        payload = {"act_id": data["act_id"]}
        try:
            response = requests.post(
                data["url"], headers=headers, json=payload)
            res_data = response.json()

            if res_data.get("retcode") == 0:
                print(
                    f"[ INFO ] - [{game_name}]: Check-in realizado com sucesso!")
            elif res_data.get("retcode") == -5003:
                print(
                    f"[ INFO ] - [{game_name}]: Você já realizou o check-in de hoje.")
            else:
                print(f"[ AVISO ] - [{game_name}]: {res_data.get(
                    'message')} ({res_data.get('retcode')})")

        except Exception as e:
            print(f"[ ERRO ] - [{game_name}]: Erro: {e}")


if __name__ == "__main__":
    executar_checkin()

import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    bitcoin_price = data["bitcoin"]["usd"]
    ethereum_price = data["ethereum"]["usd"]

    print("\n===== CRYPTO PRICE TRACKER =====\n")

    print(f"Bitcoin Price : ${bitcoin_price}")
    print(f"Ethereum Price: ${ethereum_price}")

except requests.exceptions.RequestException as error:

    print("\nError while connecting to API:")
    print(error)

except KeyError:

    print("\nUnexpected response received from API.")

except Exception as error:

    print("\nAn unexpected error occurred:")
    print(error)
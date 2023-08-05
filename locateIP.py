import requests


def geolocate_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print(f"Adresse IP: {data['query']}")
        print(f"Pays: {data['country']}")
        print(f"Région: {data['regionName']}")
        print(f"Ville: {data['city']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Fournisseur d'accès Internet: {data['isp']}")
    else:
        print("Impossible de géolocaliser cette adresse IP.")
print("    ______  ______  ___  ___ _   __")
print("   / __/\ \/ / __ \/ _ \/ _ | | / /")
print("  / _/   \  / /_/ / // / __ | |/ /") 
print(" /___/   /_/\____/____/_/ |_|___/")

if __name__ == "__main__":
    ip_address = input("Entrez une adresse IP à géolocaliser : ")
    geolocate_ip(ip_address)
print("    ______  ______  ___  ___ _   __")
print("   / __/\ \/ / __ \/ _ \/ _ | | / /")
print("  / _/   \  / /_/ / // / __ | |/ /") 
print(" /___/   /_/\____/____/_/ |_|___/")

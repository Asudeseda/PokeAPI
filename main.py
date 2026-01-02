import json
import requests
import tkinter
import random

pokemon_list = ["bulbasaur","ivysaur","venusaur","charmander","charmeleon","charizard","squirtle"]

def get_pokemon():
    pokemon = random.choice(pokemon_list)  # listeden rastgele seç
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"  # url oluştur

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        name_label.config(text=f"Name: {data['name']}")
        id_label.config(text=f"ID: {data['id']}")
        types_label.config(text="Types: " + ", ".join(t["type"]["name"] for t in data["types"]))
        error_label.config(text="")  # hata yazısı varsa temizle

    except requests.exceptions.HTTPError:
        error_label.config(text="İstek hatası (HTTP).")
    except requests.exceptions.RequestException:
        error_label.config(text="Diğer istek hatası.")


window = tkinter.Tk()
window.title("Pokemons APIs")
window.config(bg="yellow")
window.config(padx=50, pady=50)

name_label = tkinter.Label(window, text="Name:")
name_label.pack(pady=5)
name_label.config(fg="black",bg="yellow")
id_label = tkinter.Label(window, text="ID:")
id_label.pack(pady=5)
id_label.config(fg="black",bg="yellow")
types_label = tkinter.Label(window, text="Types:")
types_label.pack(pady=5)
types_label.config(fg="black", bg="yellow")
error_label = tkinter.Label(window)
error_label.pack(pady=5)
fetch_button = tkinter.Button(window, text="Get Pokémon", command=get_pokemon)
fetch_button.config(bg="yellow")
fetch_button.pack(pady=10)




tkinter.mainloop()
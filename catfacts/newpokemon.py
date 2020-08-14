import requests
import wget

#player 1
def api_pull():
    choice = input("What Pokemon would you like a picture of? ")
    # code goes here!
    url = 'https://pokeapi.co/api/v2/pokemon/' + choice
    pokemon = requests.get(url)

    return pokemon # the value of url must be a valid url concatenated with user input!

#player 2
def json_conv(pokemon):
    json2python = pokemon.json()

    return json2python # the value of json2python is the whole dictionary of bulbasaur!

# json_conv(https://pokeapi.co/api/v2/pokemon/bulbasaur) # this is just a url to use for testing


#player 3
def api_slice(json2python):
    poke_pic = json2python["sprites"]["front_default"]
    return poke_pic

# api_slice(https://pokeapi.co/api/v2/pokemon/bulbasaur/) # this is a temporary link

#player 4
def wget_pic(imagelink):
    wget.download(imagelink,"/home/student/mycode/pokemon.png")

    # code goes here!
    # image must be saved to /home/student/mycode

wget_pic("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png")

def main():
    wget_pic(api_slice(json_conv(api_pull())))

main()

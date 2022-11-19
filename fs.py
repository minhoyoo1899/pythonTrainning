import json

info_dict = {
  "id" : 1,
  "name" : "돼지",
  "별명" : "개돼지"
}

with open("./pokemon_dict.json", "w", encoding="UTF-8") as file:
  json.dump(info_dict, file, indent=2, ensure_ascii=False)
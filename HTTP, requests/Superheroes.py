import json
import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
her_list = json.loads(resp.text)
def max_hero_intel(her_list):
    hero_name, hero_name2, hero_name3 = str(input('Input hero`s name: ')), str(input('Input second hero name: ')), str(
        input('Input third hero name: '))
    hero_list = []
    for heroes in her_list:
        if heroes.get('name') == hero_name:
            hero_list.append(heroes)
        elif heroes.get('name') == hero_name2:
            hero_list.append(heroes)
        elif heroes.get('name') == hero_name3:
            hero_list.append(heroes)
    power_name_list = []
    for needed_heroes in hero_list:
        power_name_list.append(needed_heroes.get('name'))
        power_name_list.append(needed_heroes.get('powerstats'))
    power_stats = []
    for stats in power_name_list:
        if 'intelligence' in stats:
            power_stats.append(stats)
    intel_list = []
    for value in power_stats:
        intel_list.append(value.get('intelligence'))
    hero_name_list = []
    if hero_name or hero_name2 or hero_name3 not in hero_name_list:
        hero_name_list.append(hero_name)
        hero_name_list.append(hero_name2)
        hero_name_list.append(hero_name3)
    hero_name_list.sort()
    smart_dict = dict(zip(hero_name_list, intel_list))
    try:
        max_val_key = max(smart_dict, key=smart_dict.get)
        return max_val_key
    except ValueError:
        return 'none'
print(f'Smartest hero is {max_hero_intel(her_list)}.')


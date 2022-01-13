import requests
import json


death_dict = {}
max_death_dict = {
    'episode_id': None,
    'season': None,
    'episode': None,
    'number_of_deaths': 0,
    'killed': None
}


def sorting():
    for death in data:
        season_number = death['season']
        if season_number in death_dict.keys():

            episode_number = death['episode']
            if episode_number in death_dict[season_number].keys():
                death_dict[season_number][episode_number]['number_of_deaths'] += death['number_of_deaths']
                death_dict[season_number][episode_number]['killed'].append(death['death'])
            else:
                death_dict[season_number][episode_number] = {
                    'number_of_deaths': death['number_of_deaths'],
                    'killed': [death['death']]
                }
        else:
            death_dict[season_number] = {
                death['episode']: {
                    'number_of_deaths': death['number_of_deaths'],
                    'killed': [death['death']]
                }
            }


def ex_max():
    for i_season, episodes in death_dict.items():
        for i_episode, values in episodes.items():
            if values['number_of_deaths'] > max_death_dict['number_of_deaths']:
                max_death_dict['season'] = i_season
                max_death_dict['episode'] = i_episode
                max_death_dict['number_of_deaths'] = values['number_of_deaths']
                max_death_dict['killed'] = values['killed']


all_death_req = requests.get('https://www.breakingbadapi.com/api/deaths')
data = json.loads(all_death_req.text)

sorting()
ex_max()

episode_id_req = requests.get('https://www.breakingbadapi.com/api/episodes')
data_ep = json.loads(episode_id_req.text)
for episode in data_ep:
    if (episode['season'] == str(max_death_dict['season'])) and (
            episode['episode'] == str(max_death_dict['episode'])):
        max_death_dict['episode_id'] = episode['episode_id']

print(max_death_dict)

with open('breaking_bad.json', 'w') as file:
    json.dump(max_death_dict, file, indent=4)




geo_logs = [
	    {'visit1': ['Москва', 'Россия']},
	    {'visit2': ['Дели', 'Индия']},
	    {'visit3': ['Владимир', 'Россия']},
	    {'visit4': ['Лиссабон', 'Португалия']},
	    {'visit5': ['Париж', 'Франция']},
	    {'visit6': ['Лиссабон', 'Португалия']},
	    {'visit7': ['Тула', 'Россия']},
	    {'visit8': ['Тула', 'Россия']},
	    {'visit9': ['Курск', 'Россия']},
	    {'visit10': ['Архангельск', 'Россия']}
	]

geo_logs1=[]

for visits in geo_logs:
    if 'Россия' in list(visits.values())[0]:
         geo_logs1.append(visits)
print(geo_logs1)

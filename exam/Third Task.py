def forecast(*args):
    dict_weather = {}
    for idx in args:
        location, weather = idx
        if weather not in dict_weather:
            dict_weather[weather] = []
        dict_weather[weather].append(location)
    result = ''
    for k, v in dict_weather.items():
        v = sorted(v)
        if k == 'Sunny':
            for town in v:
                result += f"{town} - {k}" + '\n'
    for k, v in dict_weather.items():
        v = sorted(v)
        if k == 'Cloudy':
            for town in v:
                result += f"{town} - {k}" + '\n'
    for k, v in dict_weather.items():
        v = sorted(v)
        if k == 'Rainy':
            for town in v:
                result += f"{town} - {k}" + '\n'
    return result

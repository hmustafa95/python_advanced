def flights(*args):
    flights_dict = {}
    for idx in range(0, len(args), 2):
        if args[idx] == 'Finish':
            break
        if args[idx] not in flights_dict:
            flights_dict[args[idx]] = 0
        flights_dict[args[idx]] += int(args[idx + 1])
    return flights_dict

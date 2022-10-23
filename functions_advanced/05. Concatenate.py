def concatenate(*args, **kwargs):
    sentence = ''.join(args)
    for k, v in kwargs.items():
        if k in sentence:
            sentence = sentence.replace(k, v)
    return sentence

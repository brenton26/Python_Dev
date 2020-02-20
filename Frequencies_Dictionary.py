
def freq_dict(data):
    freq = {}
    for element in data:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq

print(freq_dict("I'm gonna beat you up cause you can't whoop me."))

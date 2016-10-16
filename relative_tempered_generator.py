from __future__ import division


def nextNoteFrecuency(note_frecuency, distance):
    interval_proportion_dic = {1: 25/24, 2: 9/8, 3: 6/5, 4: 5/4, 5: 4/3, 6: 45/32, 7: 3/2, 8: 8/5, 9: 5/3, 10: 9/5, 11: 15/8, 12: 2}
    if distance == 0:
        return note_frecuency
    elif distance > 0:
        if distance > 12:
            octaves = distance // 12
            nDistance = distance % 12
            return (note_frecuency * interval_proportion_dic[nDistance]) * 2 ^ octaves
        else:
            return note_frecuency * interval_proportion_dic[distance]
    elif distance < 0:
        if distance < -12:
            octaves = abs(distance) // 12
            nDistance = abs(distance) % 12
            return (note_frecuency / interval_proportion_dic[abs(distance)]) / 2 ^ octaves
        else:
            return note_frecuency / interval_proportion_dic[abs(distance)]


def chord(root, listOfDistances):
    res = [root]
    for d in listOfDistances:
        res.append(nextNoteFrecuency(root, d))
    return res


def getKeysDistance(key_origin, key_destiny):
    pass


def noteHarmonic(note_frecuency):
    pass

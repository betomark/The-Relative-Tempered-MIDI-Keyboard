from pygame import pypm
def nextNote(note,distance):
    dic={1:25/24,2:9/8,3:6/5,4:5/4,5:4/3,6:45/32,7:3/2,8:8/5,9:5/3,10:9/5,11:15/8,12:2}
    if distance==0:
        return note
    elif distance>0:
        if distance>12:
            octaves=distance//12
            nDistance=distance % 12
            return (note*dic[nDistance])*2^octaves 
        else:
            return note*dic[distance]
    elif distance<0:
        if distance<-12:
            octaves=abs(distance)//12
            nDistance=abs(distance) % 12
            return (return note/dic[abs(distance)])/2^octaves 
        else:
            return note/dic[abs(distance)]
        

def chord(root,listOfDistances):
    res=[root]
    for d in listOfDistances:
        res.append(nextNote(root,d))
    return res

import math

from pygame import Vector2

def objectlookattarget(object, target):
    sx = object.rect.center[0] - target.rect.center[0]
    sy = object.rect.center[1] - target.rect.center[1]

    a = math.atan2(sx, sy)
    d = math.degrees(a) 

    return d + 90

def objectlookatposition(object, position=[0,0]):
    sx = object.rect.center[0] - position[0]
    sy = object.rect.center[1] - position[1]

    a = math.atan2(sx, sy)
    d = math.degrees(a) 

    return d + 90

def positionlookatposition(position1 = [0, 0], position2=[0,0]):
    sx = position1[0] - position2[0]
    sy = position1[1] - position2[1]

    a = math.atan2(sx, sy)
    d = math.degrees(a) 

    return d + 90

def getpositionlookatpositionvector(position, target):
    d = positionlookatposition(position, target)
    r = math.radians(d)
    f = [math.cos(r), -math.sin(r)]
    return Vector2(f)

def getpositionlookatvector(object, target):
    d = objectlookatposition(object, target)
    r = math.radians(d)
    f = [math.cos(r), -math.sin(r)]
    return Vector2(f)

def getobjectlookatvector(object, target):
    d = objectlookattarget(object, target)
    r = math.radians(d)
    return [round(math.cos(r), 3), -round(math.sin(r), 3)]


def getvectorfromrotation(rotation):
    v = Vector2(float(math.cos(math.radians(rotation))), float(math.sin(math.radians(rotation))))
    return v
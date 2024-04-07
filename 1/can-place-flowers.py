def can_place_flowers(flowerbed:list,spot:int):
    flowerbed = [0] + flowerbed + [0]
    return not bool(flowerbed[spot] + flowerbed[spot+1] + flowerbed[spot+2])
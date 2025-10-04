def solution(players, callings):
    position ={}
    for rank, player in enumerate(players):
        position[player] = rank
        
    for call in callings:
        index = position[call]
        players[index-1] , players[index] = players[index],players[index-1]
        position[players[index-1]] = index-1
        position[players[index]] = index
    return players
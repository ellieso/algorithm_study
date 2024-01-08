def solution(friends, gifts):
    gift_count = {friend: 0 for friend in friends}

    total_gift_count = {friend: [{f: 0 for f in friends}, 0, 0] for friend in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        total_gift_count[giver][0][receiver] += 1
        total_gift_count[giver][1] += 1
        total_gift_count[receiver][2] += 1

    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            giver = friends[i]
            receiver = friends[j]
            if total_gift_count[giver][0][receiver] < total_gift_count[receiver][0][giver] :
                gift_count[receiver] += 1
            elif total_gift_count[giver][0][receiver] > total_gift_count[receiver][0][giver] :
                gift_count[giver] += 1
            elif total_gift_count[giver][0][receiver] == total_gift_count[receiver][0][giver] :
                if (total_gift_count[giver][1] - total_gift_count[giver][2]) < (total_gift_count[receiver][1] - total_gift_count[receiver][2]) :
                    gift_count[receiver] += 1
                elif (total_gift_count[giver][1] - total_gift_count[giver][2]) > (total_gift_count[receiver][1] - total_gift_count[receiver][2]) :
                    gift_count[giver] += 1

    return max(gift_count.values())
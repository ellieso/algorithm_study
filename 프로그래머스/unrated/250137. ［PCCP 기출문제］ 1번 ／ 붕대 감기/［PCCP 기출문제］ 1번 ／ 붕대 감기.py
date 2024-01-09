def solution(bandage, health, attacks):
    final_attack = attacks[-1][0]
    
    for i in range(1, final_attack+1):
        if attacks[i-1][0] != i:
            attacks.insert(i-1, [i,0])
    print(f"new_attack : {attacks}")
    
    answer = health
    heal_time = 0
    
    for i in range(final_attack):
        print(f"{i+1}초")
        if attacks[i][1] != 0:
            answer = answer - attacks[i][1]
            heal_time = 0
            print(f"공격받았습니다. 현재 체력 : {answer}, 힐 연속시간 : {heal_time}초")
            if answer <= 0:
                # 체력이 0 이하이면 캐릭터가 사망
                answer = -1
                print("캐릭터가 사망하였습니다.")
                return answer
        else:
            heal_time += 1
            
            if heal_time != bandage[0]:
                answer = min(answer + bandage[1], health)
                print(f"공격받지 않아 붕대감기를 시작합니다. 현재 체력 : {answer}, 힐 연속시간 : {heal_time}초")
            else:
                answer = min(answer + bandage[1] + bandage[2], health)
                heal_time = 0
                print(f"힐 지속시간 최대치로 추가 체력을 회복합니다. 현재 체력 : {answer}, 힐 연속시간 : {heal_time}초")
    return answer
def solution(bandage, health, attacks):

    bandage_time = 0
    additional_health = 0
    final_health = health

    while len(attacks) > 0:
        attack = attacks[0]

        # 캐릭터의 체력이 0 이하가 되면 -1을 리턴
        if final_health <= 0:
            final_health = -1
            break

        # 공격시간과 경과 시간이 같으면 health에서 피해량 빼기 / 공격성공이므로 연속성공 초기화
        if attack[0] == bandage_time:
            final_health -= attack[1]
            additional_health = 0
            attacks.pop(0)
        # 공격시간과 경과 시간이 다르면 회복
        else:
            # 최대 체력과 동일하지 않으면 연속공격이 성공했을 때만 추가회복
            if final_health < health:
                additional_health += 1

            # 연속 공격에 성공하면 추가회복
            if additional_health == bandage[0]:
                final_health = min(final_health + bandage[1] + bandage[2], health)
                additional_health = 0
            # 연속 공격에 성공하지 않으면 기본 값만 회복
            else:
                final_health = min(final_health + bandage[1], health)

        bandage_time += 1
    
    return final_health if final_health > 0 else -1
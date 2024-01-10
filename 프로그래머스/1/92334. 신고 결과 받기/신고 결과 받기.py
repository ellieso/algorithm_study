def solution(id_list, report, k):
    # 중복된 항복이 있을 수 있으니 제거 후 count 
    report = list(set(report))

    id_dict = {id_l: [{i: 0 for i in id_list},0,0] for id_l in id_list}
    
    # 신고현황표 작성
    for r in report :   
        reporter, suspension = r.split()
        id_dict[reporter][0][suspension] += 1
    
    # 유저별로 신고당한 횟수 count와 최종 신고당하는 사람 확인
    final_suspension = []
    
    for i in id_list :
        for j in id_list :
            id_dict[i][1] += id_dict[j][0][i]
        if id_dict[i][1] >= k :
            final_suspension.append(i)

    # 유저가 받은 메일 수
    for i in id_list :
        for s in final_suspension :
            if id_dict[i][0][s] >= 1 :
                id_dict[i][2] += 1
                
    return [id_dict[i][2] for i in id_list]
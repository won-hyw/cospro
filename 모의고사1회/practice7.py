def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info: # f = jpeg,all.jpg,500
        splited = f.split(",") # splited = ["jpeg", "all.jpg", "500"]
        if splited[0] == "jpeg" and int(splited[2]) < 1000:
            sucess += 1
        else:
            fail += 1
    return sucess, fail

print(solution(["jpeg,all.jpg,500", "mpeg,all.mp3,500"]))
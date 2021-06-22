jordan_belfort = {"calls": 178, "meetings":17, "sales":6}
Calle_bäck = {"calls": 130, "meetings":5, "sales":4}




def total_score(dict):
    calls_score = dict["calls"]*10
    meetings_score = dict["meetings"]*30
    sale_score = dict["sales"]*100

    total_score_person = calls_score+meetings_score+sale_score
    print(total_score_person)

    if dict["calls"]>150 or dict["meetings"] or dict["sales"]*100:
        total_score_person = total_score_person+100

        dict["score"]=total_score_person

    else:
        dict["score"]=total_score_person
    
    



total_score(Calle_bäck)
print(Calle_bäck)
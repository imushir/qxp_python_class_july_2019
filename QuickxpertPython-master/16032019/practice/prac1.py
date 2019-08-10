statement = "This IS VERY Cool"
uppr_cnt = 0
lower_cnt = 0
for each_letter in statement:
    if(each_letter.isupper()):
        uppr_cnt = uppr_cnt + 1
    elif(each_letter.islower()):
        lower_cnt = lower_cnt + 1
    else:
        continue
print("%d letters are Upper and %d letters are Lower" \
           % (uppr_cnt, lower_cnt))
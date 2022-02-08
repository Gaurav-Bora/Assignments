def not_bad(s):
    if s.find('not') != -1:
        notindex = s.find('not')
        if s.find('bad') != -1:
            badindex = s.find('bad') + 3
            if badindex > notindex and badindex > 0 and notindex >0:
                removetxt = s[notindex : badindex]
                news = s.replace(removetxt, "good")
            else:
                news = s
        else:
             news = s
              
    else:
         news = s
    print (news)

not_bad("food is not bad")
not_bad("the lyrics is not that bad")
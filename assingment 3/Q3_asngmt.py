def string_test (s):
    d = {"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
                d["LOWER_CASE"]+=1
        else:
            pass
        print(f"oringnal string",s)
        print("number of upper case alphabets:",d["UPPER_CASE"])
        print("number of lower case alphabets:",d["LOWER_CASE"])
string_test("pYthong is A pRoGraMMinG")

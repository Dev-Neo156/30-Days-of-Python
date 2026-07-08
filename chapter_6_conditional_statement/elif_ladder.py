cls = int(input(("Enter you class: ")))
while cls>0:
    if(cls == 11 or cls == 12):
        print("Higher secondary education")
        break;
    elif(cls < 11 and cls >= 6):
        print("secondary education")
        break;
    else:
        print("Elemenatry education")
    break;
else:
    print("Enter a valid class")
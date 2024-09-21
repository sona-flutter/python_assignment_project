l=[]
while True:
    c=int(input('''
      1 Push Element
      2 Pop Element
      3 Peek Elemnet
      4 Display Element
      5 Exit
      '''))
    if c==1:
      n=input("Enter the Value");
      l.append(n)
      print(l)
    elif c==2:
        if len(l)==0:
                print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
          if len(l)
            
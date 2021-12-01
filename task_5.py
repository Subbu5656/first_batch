
      # PROGRAM TO PRINT FIRST LETTER CAPITAL WITHOUT USING CAPITALIZE,TITLE
      
s = 'iam coming to the class'
l={i[0].upper()+i[1::] for i in s.split()}
l=[i[0].upper()+i[1::] for i in s.split()]
print(l)

print([i.upper()[0]+i[1::] for i in s.split()])


S1=int(input("write first site of tringle"))
S2=int(input("write second site of tringle"))
S3=int(input("write third site of tringle"))
if S1==S2==S3:
    print("equilateral tringle")
elif S1==S2 or S1==S3 or S2==S3:
   print("isosceles")
elif S1!=S2!=S3:
   print("scalence")

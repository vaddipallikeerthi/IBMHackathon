age=input("AGE    :")
print("please enter 1 for YES and 0 for NO")
print("Any previous medication taken")
Prediag=int(input())
print("Are you feeling tired")
Tired=int(input())
print("Are you suffering from cold frequently")
Cold=int(input())
print("Wounds heal slow")
Heal=int(input())
print("Stress level is high")
Stress=int(input())
print("Lots of tummy troubles")
Tummy=int(input())
print("Frequent infections")
Infect=int(input())
print("Do you have any CORONA related symptoms")
symptoms=int(input())
Immune_system=((Tired+Cold+Heal+Stress+Tummy+Infect)/7)*100
print(Immune_system)
if(Immune_system>60 and Prediag==1):
    if(symptoms==1):
        print("IMMEDIATE CONSULTATION REQUIRED")
    else:
        print("INTAKE OF IMMUNE RICH DIET")
else:
    print("GOOD, BUT STAY SAFE")

            



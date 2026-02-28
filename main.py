
scores=[]

def scorer(m1,m2,m3,a=0):
    if m1==10 :
        a+=1
    if m2==0 :
        a+=1
    if m3==42 :
        a+=1
    return a
    
    
def avg(scores):
    return sum(scores)/len(scores)

def lowest(scores):
    return min(scores)

def highest(scores):
    return max(scores)


for i in range(5):
    print(f"\n Student {i+1}")
    m1=int(input("2+8="))
    m2=int(input("2-2="))
    m3=int(input("2+40="))
    
    result=scorer(m1,m2,m3)
    scores.append(result)
    print(f"\nstudent {i+1} score: {result}/3")
    
print("\n" + "_"*15)
print("FINAL RESULTS")
print("_"*15 + "\n")
print(f"All scores: {scores}")
print(f"Average: {avg(scores):.3f}")
print(f"Highest: {highest(scores)}")
print(f"Lowest: {lowest(scores)}")
    

if __name__ == "__main__":
    print("WELCOME TO THE QUIZ SCORER!")
    

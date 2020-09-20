print("Calculating radioactive decay")
N = 100
lambdaDecay = -(1/6)
t = 0
#deltaT = 2
R = 0

results = []

while N > 0.01:
    results.append((t,round(N,5))) #only rounds after being placed into list
    R = (lambdaDecay * N)
    N = N + R
    t = t+1
print("Decay rate is: ", lambdaDecay)
print("Time\t","Nuclei")
for (t,N) in results:
    print(t,"\t",N)

#def outputCSV():
#print("Contents output to radioactivedecay.csv")


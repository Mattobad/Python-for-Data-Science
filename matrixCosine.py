#matrix multiplication
import numpy as np
import math



m=np.random.randint(0,99,[6,5])
print(m,"\n")
q=np.random.randint(0,99,[1,5])

print(q,"\n")

"""
cosine
"""

m_sqr = m*m
q_sqr = q*q

numo = []
deno = []

cosineTheta=[]

"""
to change array into vertical np.vstack(array_name)
"""
def product(x,y,results):
    for i in range(0,6,1):
        num=0
        for j in range(0,5,1):
            num += (x[i,j]*y[0,j])
      
     
        results.append(num)
      
product(m,q,numo)
print("Numerator")
print(np.vstack(numo),"\n")
product(m_sqr,q_sqr,deno)
print("Denominator")
print(np.vstack(deno))
for i in range(0,6,1):
    deno_sqrt = (math.ceil(math.sqrt(deno[i])))
    cosineTheta.append(numo[i]/deno_sqrt)

print("Cosine Theta Value")
cosineTheta
cosineTheta =(np.vstack(cosineTheta))

print(cosineTheta)







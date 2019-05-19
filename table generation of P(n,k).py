from tabulate import tabulate
p = [ [ 0 for i in range(30) ] for j in range(30) ] 

kind = [0]*30;
for i in range(30):
	kind[i] = i+1;

for i in range(0,30):
 p[i][0] = 1;

#n is i, and k is j
for n in range(0,30):
    for k in range(1,30):
     if n == k: 
         p[n][k] = 1;
     elif n > k:
         p[n][k] = p[n - k - 1][k+1] + p[n-1][k-1];

print (tabulate(p,headers = kind))


		

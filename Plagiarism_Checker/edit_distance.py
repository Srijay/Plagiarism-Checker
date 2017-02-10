

def computeDistance(str1,str2):
	l1=len(str1)+1;
	l2=len(str2)+1;
	dist=[];
	for i in range(l1):
		temp=[];
		for j in range(l2):
			temp.append(0);
		
		dist.append(temp);
		
	for i in range(l1):
		for j in range(l2):
			if i==0:
				dist[i][j]=j;
			elif j==0:
				dist[i][j]=i;
			elif str1[i-1]==str2[j-1]:
				dist[i][j]=dist[i-1][j-1];
			else:
				v1= dist[i-1][j];
				v2= dist[i][j-1];
				v3= dist[i-1][j-1];
				
				dist[i][j]=1+min(v1,v2,v3);
				
	#print dist;
	return dist[l1-1][l2-1];
			

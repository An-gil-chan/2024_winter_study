#백준 2798번
#첫째줄에 카드개수 2종
#둘째줄에는 카드에 쓰여있는 수 <100000
#합이 m이 넘지 않는 카드 3장을 찾을 수 있는경우만 입력 

#출력 
#M이 넘지 않으면서 M에  최대한 가까운 카드 3장의 합 출력 

n,m = map(int, input().split())
li_1 = list(map(int, input().split()))

result = 0

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      now = li_1[i]+li_1[j]+li_1[k]

      if now <= m :
        result = max(now,result)
        
      
print(result)   
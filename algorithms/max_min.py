N = input()
K = input()
lists = [input() for _ in range(0,N)]
def calc(lists,k,n):
    lists.sort()
    val=lists[k-1]-lists[0]
    for l in xrange(n-1,k-1,-1):
        v1=lists[l]-lists[l-k+1]
        if v1<val:
            val=v1
    print(val)
    return val
min_diff = calc(lists,K,N)## Write code here to compute the answer using (n, k, candies)



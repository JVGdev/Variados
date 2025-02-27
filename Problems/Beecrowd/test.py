def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(change+1):
      
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                print(j, cents, minCoins)

        minCoins[cents] = coinCount
        print(cents, coinCount)
    return minCoins[change]

def main():
    amnt = 100
    clist = [1, 10, 90, 91]
    coinCount = [0]*(amnt+1)

    print("Fazendo troco para",amnt,"requer")
    print(dpMakeChange(clist,amnt,coinCount),"moedas")

main()

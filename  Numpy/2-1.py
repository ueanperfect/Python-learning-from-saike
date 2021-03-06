import numpy as np
A = np.array([[672,670,771,308,476,413,221],
             [685,619,204,990,802,789,497],
             [411,696,445,612,390,963,351],
             [926,604,528,280,844,328,710],
             [459,815,327,842,875,447,924],
             [396,294,254,748,690,305,261],
             [208,965,816,348,169,976,118]])

B = np.array([[221,494,780,354,989,569,915],
              [497,665,896,291,570,764,730],
              [351,833,362,575,214,510,432],
              [710,400,916,564,298,130,830],
              [924,486,801,584,994,870,536],
              [261,948,349,250,946,582,545],
              [118,133,856,442,392,215,304]])

C = np.array([[915,750,201,440,846,954,952],
              [730,483,908,609,981,752,642],
              [432,453,380,256,245,168,860],
              [830,828,205,857,729,904,387],
              [536,430,369,774,533,456,806],
              [545,689,375,949,192,804,335],
              [304,176,402,290,632,183,450]])

D = np.array([[952,100,112,346,618,925,672],
              [642,843,633,598,507,705,685],
              [860,356,532,827,147,687,411],
              [387,978,576,772,515,423,926],
              [806,725,649,831,667,537,459],
              [335,727,310,920,798,309,396],
              [450,246,996,834,889,172,208]])

E = np.array([[952,954,846,440,201,750,915],
              [100,544,822,512,253,345,569],
              [112,546,426,207,980,820,989],
              [346,255,531,463,284,516,354],
              [618,529,141,608,361,493,780],
              [925,955,744,198,945,876,494],
              [672,670,771,308,476,413,221]])

F = np.array([[208,965,816,348,169,976,118],
              [172,105,195,910,548,156,133],
              [889,554,418,573,610,170,856],
              [834,700,930,671,697,517,442],
              [996,125,166,674,222,974,392],
              [246,429,986,123,382,975,215],
              [450,183,632,290,402,176,304]])
flag = -1
N = np.zeros((6,49), dtype=int)
for j in [A, B, C, D, E, F]:
    flag += 1
    n = -1
    G = j.ravel()
    for num in G:
          for i in range(2, num):
              if num % i == 0:
                  break
          else:
                  n += 1
                  N[flag][n] = num
    print('%s'%['A','B','C','D','E','F'][flag], list(N[flag,0:n+1]))
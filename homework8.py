import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
import time


#quicksortの関数
def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)-1
        quicksort(A,p,q)
        quicksort(A,q+1,r-1)

#partitionの関数
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i=i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    # print(A)
    return i+1

# A = [2,8,7,1,3,5,6,4]
# p = 0
# r = len(A)-1
# quicksort(A,p,r)
# print(A)

#計算時間の計測
average_time = [] # 平均時間を記録するリスト
for n in range(100, 1001, 100): # n を 100 から 1000 まで 100 刻みで繰り返す．
    quicksort_time = [] # クイックソートの計算時間を記録するリスト
    A = []
    for i in range(100):
    ###### インスタンスファイルからリスト A を作成する #####
        with open('./instances/n'+str(n)+'id'+str(i)+'.txt','r') as f:
            lines = f.read()
            A = lines.split()
                
        start_time = time.perf_counter()
        quicksort(A, 0, len(A) - 1)
        end_time = time.perf_counter()
        # 実行時間を記録する．
        quicksort_time.append(end_time - start_time)
    # 平均実行時間を計算し，単位をミリ秒に変換する．
    average_time.append((sum(quicksort_time) / 100) * 1000)


#グラフの作成
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.set_xlim([100, 1000])
ax.set_xlabel('input size')
ax.set_ylim([0, 2]) # 自分の PC の性能に応じて範囲を調整する．
ax.set_ylabel('average computation time [ms]')
# グラフの描画
ax.plot(list(range(100, 1001, 100)), average_time, '-',
linewidth = 1, label='quicksort')
plt.legend(loc='best') # 判例の表示
pp = PdfPages('result.pdf') # pdf ファイルの初期化
pp.savefig() # グラフを pdf 形式で保存する．
pp.close() # pdf ファイルをクローズする．

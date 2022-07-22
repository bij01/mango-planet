import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Hancom MalangMalang'
plt.rc('font', size=20)
plt.rc('')

colors = ["#FF2D00","#E023D6","#3840F2"]
aaa = [27,35,25]
ratio = (aaa[0],aaa[1],aaa[2])
labels = ['맛있다', '괜찮다', '별로']
explode = [0, 0.20, 0.10]

plt.pie(ratio, labels=labels, autopct='%.2f%%', startangle=260, counterclock=False, shadow=True, explode=explode, colors=colors,textprops={'color':"w"})
plt.show()

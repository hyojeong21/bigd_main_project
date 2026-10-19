import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"

# 윈도우
plt.rcParams["font.family"] = "Malgun Gothic"
# 공통 (OS 무관) 마이너스 기호가 깨지는 것을 막아준다
plt.rcParams["axes.unicode_minus"] = False

# 저번주 기온
prices = [27, 22, 22, 25, 21]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")
    
ax.set_title("내첫그래프")
fig.savefig("my_first_chart.png")
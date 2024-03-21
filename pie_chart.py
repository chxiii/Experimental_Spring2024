import matplotlib.pyplot as plt

# data for the pie plot
labels = ["University", "Upper Secondary School", "Lower Secondary School", "Primary School", "Non-education"]
levels = [.43, .02, .04, .03, .48]
colors = ["#F7FBFC", "#D6E6F2", "#B9D7EA", "#769FCD", "#526D82"]
explode = [0.08, 0, 0, 0, 0.08]

# draw a pie plot
plt.pie(levels, labels=labels, colors=colors, autopct="%1.1f%%", explode=explode,
        textprops={"fontsize":9.5, "color": "black"},
        wedgeprops={"linewidth": .8, "edgecolor": "black"})
# plt.show()
plt.savefig("literature_statistics.pdf")

plt.clf()

labels = ["Positive", "Neutral", "Negative"]
levels = [.72, .25, .03]
colors = ["#F7FBFC", "#D6E6F2", "#B9D7EA"]

# draw a pie plot
plt.pie(levels, labels=labels, colors=colors, autopct="%1.1f%%",
        textprops={"fontsize":9.5, "color": "black"},
        wedgeprops={"linewidth": .8, "edgecolor": "black"})
# plt.show()
plt.savefig("results_statistics.pdf")

plt.clf()
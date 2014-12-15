from pylab import *
from numpy import *
from scipy.stats import beta

def runExperiment(poll, names, poller, experiments):

    candidates = len(poll)
    colors = ['b','g','c','m','y','k']

    #Times a candidate finish in a position
    simulationsPositions = zeros(shape=(candidates,candidates ))

    #Percentage of experiments a candidate finish a position...to get first and ballotage position
    simulationsPercentages = zeros(shape=(candidates,candidates ))

    #Sample dirichlet for n = experiments times
    simulations = random.dirichlet(poll, size=experiments)

    #Get positions in simulations
    for candidate in range(candidates):
        for simulation in simulations:
            position = argsort(simulation)[::-1][candidate]
            simulationsPositions[candidate][position] += 1

    simulationsPercentages = simulationsPositions / experiments

    #Get times that candidate win election
    firstPosition = simulationsPercentages[:,0]

    #Get times that candidate is in a ballotage position
    ballotagePosition = simulationsPercentages[:,0] + simulationsPercentages[:,1]



    #####Make Graphs#####

    width = 0.35
    ind = np.arange(candidates)
    maxAxis = 0.0

    #Graph intervals results with bars
    ax1 = subplot2grid((1,3), (0,0), colspan=2)
    for i in range(candidates):
        simulation = simulations[:,i]*100
        p0 = np.percentile(simulation,0)
        p5 = np.percentile(simulation,5)
        p95 = np.percentile(simulation,95)
        p100 = np.percentile(simulation,100)
        mean = simulation.mean()

        ax1.plot([p0, p5], [i,i], "-", linewidth=70, color = 'b', alpha=0.2, solid_capstyle="butt")
        ax1.plot([p5, p95], [i,i], "-", linewidth=70, color = 'b', alpha=0.4, solid_capstyle="butt")
        ax1.plot([p95, p100], [i,i], "-", linewidth=70, color = 'b', alpha=0.2, solid_capstyle="butt")
        ax1.plot(mean, i, "o", markersize=10, color = 'r')
        maxAxis = max(maxAxis, max(simulation))
        ax1.text(mean, i-0.2, round(mean,2), ha='center', va='bottom')
        if i == 0:
            ax1.annotate('5% de probabilidad\n de pertenecer\n a este rango',xy=((p0 + p5) / 2, i), arrowprops=dict(arrowstyle='->'), xytext=(p0-7.5, i-0.2))
            ax1.annotate('90% de probabilidad\n de pertenecer\n a este rango',xy=((p5 + mean) / 2, i-0.2), arrowprops=dict(arrowstyle='->'), xytext=(((p5 + mean) / 2)-2.5, i-0.8))
            ax1.annotate('Valor mas probable',xy=(mean, i), arrowprops=dict(arrowstyle='->'), xytext=(mean-2.5, i+0.5))


    yticks(ind, names )
    ax1.axis([0.0,maxAxis + 5.0,-1.0,candidates])
    xlabel('% Votos')
    ax1.legend()

    ax1.xaxis.set_major_locator(MultipleLocator(5))
    ax1.xaxis.set_minor_locator(MultipleLocator(1))
    ax1.xaxis.grid(True,'minor')
    ax1.xaxis.grid(True,'major',linewidth=2)

    title(poller)


    #Graph Ballotage
    ax2 = subplot2grid((1,3), (0, 2))
    ax2.barh(ind,ballotagePosition, width,color = 'b', alpha=0.4,)
    yticks(ind+0.15, names)
    ax2.xaxis.set_minor_locator(MultipleLocator(0.05))
    ax2.xaxis.grid(True,'minor')
    ax2.axis([0.0,1.0,-1.0,candidates])
    for i in range(candidates):
        if ballotagePosition[i] > 0.8:
            ax2.text(ballotagePosition[i]-0.04, i+0.13, round(ballotagePosition[i],2), ha='center', va='bottom')
        else:
            ax2.text(ballotagePosition[i]+0.04, i+0.13, round(ballotagePosition[i],2), ha='center', va='bottom')
    xlabel('Probabilidad de disputar un ballotage')
    title(poller)

    show()

if __name__ == '__main__':

    polls=[[991,833,769,587,202,587 ],[252,214,205,140,121],[400,392,307,214,30,257]]
    pollers = ['Aresco - Agosto 2014', 'Isonomia - Agosto 2014', 'm & f - Julio 2014']
    candidatesNames = [["Scioli", "Massa", "Macri", "Cobos", "Altamira", "Otro/NS/NC"],["Scioli", "Macri", "Massa", "Cobos", "Otro/NS/NC"],["Massa", "Scioli", "Macri", "Binner", "Altamira", "Otro/NS/NC"]]

    experiments = 1000000

    #for i in range(len(polls)):
    for i in range(1):
        runExperiment(polls[i], candidatesNames[i], pollers[i], experiments )





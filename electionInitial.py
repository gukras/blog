from pylab import *
from numpy import *
from scipy.stats import beta

def runExperiment(poll, names, poller):

    totalVotes = float(np.array(poll).sum())

    candidates = len(poll)
    colors = ['b','g','c','m','y','k']


    #####Make Graphs#####

    width = 0.35
    ind = np.arange(candidates)
    maxAxis = 0.0

    #Graph intervals results with bars
    ax1 = subplot2grid((1,1), (0,0))

    for i in range(candidates):

        ax1.plot([0, (poll[i]/totalVotes)*100], [i,i], "-", linewidth=70, color = 'b', alpha=0.4, solid_capstyle="butt")
        ax1.text((poll[i]/totalVotes)*100 +1.5, i-0.2, str(round((poll[i]/totalVotes)*100,2))+'%', ha='center', va='bottom')

    yticks(ind, names )
    ax1.axis([0.0,50,-1.0,candidates])
    xlabel('% Votos')
    ax1.legend()

    ax1.xaxis.set_major_locator(MultipleLocator(5))
    ax1.xaxis.set_minor_locator(MultipleLocator(1))
    ax1.xaxis.grid(True,'minor')
    ax1.xaxis.grid(True,'major',linewidth=2)

    title(poller)

    show()

if __name__ == '__main__':

    polls=[[991,833,769,587,202,587 ],[252,214,205,140,121],[400,392,307,214,30,257]]
    pollers = ['Aresco - Agosto 2014', 'Isonomia - Agosto 2014', 'm & f - Julio 2014']
    candidatesNames = [["Scioli", "Massa", "Macri", "Cobos", "Altamira", "Otro/NS/NC"],["Scioli", "Macri", "Massa", "Cobos", "Otro/NS/NC"],["Massa", "Scioli", "Macri", "Binner", "Altamira", "Otro/NS/NC"]]

    for i in range(len(polls)):
        runExperiment(polls[i], candidatesNames[i], pollers[i])




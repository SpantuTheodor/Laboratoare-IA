"""
((xs,ys),(xf,yf),(xa,ya))
x,y = coordonate 
s = start
f = final
a = actual

stare initiala = (xs,ys,xf,yf,xs,ys)
stare finala = (xs,ys,xf,yf,xf,yf)


def Initialize (xs,ys,xf,yf) : 
    return [xs,ys,xf,yf,xs,ys]

def isFinal (list) :
    if (list[4] == list[2] and list[5] == list[3]) :
        return true
    return false


x_next,y_next componente ale unui vector de directie
def transition (list, x_next,y_next,visited) : 
    if visited[list[4] + x_next][list[5] + y_next] == 0 and
    list[4] + x_next > 0 and
    list[4] + x_next < n and
    list[5] + y_next > 0 and
    list[5] + y_next < m :
        list[4] = list[4] + x_next
        list[5] = list[5] + y_next
        visited[list[4]][list[5]] = 1
        return list 
    else
        return false

Initialize(1,1,6,6)

"""


import matplotlib.pyplot as plt


def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
 
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
         
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
        
    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    plt.show()


def main():
    x = int(-3)
    y = int(3)
    xEnd = int(-1)
    yEnd = int(3)
    color = "r."
    DDALine(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()

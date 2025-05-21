import matplotlib
import matplotlib.pyplot as plt
from cube import Cube

matplotlib.use('TkAgg')

if __name__ == '__main__':

    c = Cube()
    c.draw_interactive()

    plt.show()

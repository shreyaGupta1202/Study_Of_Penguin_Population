import matplotlib.pyplot as plt
import numpy as np



def plot_adelie_slider(adelie_slope, adelie_y_int):
    x = np.linspace(-5, 35, 100)
    adelie_y = (adelie_slope * x) + adelie_y_int
    adelie_plot, =plt.plot(x, (adelie_slope * x)+ adelie_y_int, color='c')
    axcolor='w'
    adelie_slope_slider = plt.axes([.1, .008, 0.3, 0.03], facecolor=axcolor)
    adelie_y_slider = plt.axes([.1, .05, 0.3, 0.03], facecolor=axcolor)

    adelie_m_slide = plt.Slider(adelie_slope_slider, label='Slope', valmin=(-50), valmax=50, valinit=adelie_slope, valstep=1)
    adelie_b_slide = plt.Slider(adelie_y_slider, label='Y-intercept', valmin=(0), valmax=1500, valinit=adelie_y_int, valstep=20)

    def update(val):
        slope = adelie_m_slide.val
        y_int = adelie_b_slide.val
        adelie_plot.set_ydata((slope*x)+y_int)
        fig.canvas.draw_idle()

    adelie_m_slide.on_changed(update)
    adelie_b_slide.on_changed(update)
    plt.show()
    
    return adelie_plot, adelie_m_slide, adelie_b_slide

    
    
    
def plot_chinstrap_slider(chinstrap_slope, chinstrap_y_int):    
    x = np.linspace(-5, 35, 100)
    chinstrap_y = (chinstrap_slope * x)+ chinstrap_y_int
    chinstrap_plot, =plt.plot(x, (chinstrap_slope * x)+ chinstrap_y_int, color='y')
    axcolor='w'
    chinstrap_slope_slider = plt.axes([.1, .008, 0.3, 0.03], facecolor=axcolor)
    chinstrap_y_slider = plt.axes([.1, .05, 0.3, 0.03], facecolor=axcolor)

    chinstrap_m_slide = plt.Slider(chinstrap_slope_slider, label='Slope', valmin=(-20), valmax=20, valinit=chinstrap_slope, valstep=1)
    chinstrap_b_slide = plt.Slider(chinstrap_y_slider, label='Y-intercept', valmin=(0), valmax=700, valinit=chinstrap_y_int, valstep=20)

    def update(val):
        slope = chinstrap_m_slide.val
        y_int = chinstrap_b_slide.val
        chinstrap_plot.set_ydata((slope*x)+y_int)
        fig.canvas.draw_idle()
    
    chinstrap_m_slide.on_changed(update)
    chinstrap_b_slide.on_changed(update)
    plt.show()


def plot_gentoo_slider(gentoo_slope, gentoo_y_int):
    x = np.linspace(-5, 35, 100)
    gentoo_y = (gentoo_slope * x)+ gentoo_y_int
    gentoo_plot, =plt.plot(x, (gentoo_slope * x)+ gentoo_y_int, color='r')
    axcolor='w'
    gentoo_slope_slider = plt.axes([.15, .008, 0.3, 0.03], facecolor=axcolor)
    gentoo_y_slider = plt.axes([.15, .05, 0.3, 0.03], facecolor=axcolor)

    gentoo_m_slide = plt.Slider(gentoo_slope_slider, label='Slope', valmin=(-50), valmax=50, valinit=gentoo_slope, valstep=1)
    gentoo_b_slide = plt.Slider(gentoo_y_slider, label='Y-intercept', valmin=(0), valmax=2000, valinit=gentoo_y_int, valstep=20)

    def update(val):
        slope = gentoo_m_slide.val
        y_int = gentoo_b_slide.val
        gentoo_plot.set_ydata((slope*x)+y_int)
        fig.canvas.draw_idle()
    
    gentoo_m_slide.on_changed(update)
    gentoo_b_slide.on_changed(update)
    plt.show()
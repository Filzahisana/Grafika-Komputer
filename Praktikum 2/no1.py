import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.pyplot import figure

points = np.array([[-1,1,1,-1,-1],[1,1,-1,-1,1]])

def transformation_matrix(x, y):
    return np.array([[1,0,x],[0,1,y],[0,0,1]])

def scale_matrix(x, y):
    return np.array([[x,0,0], [0,y,0],[0,0,1]])

def Rot_matrix(angle):
    return np.array([[np.cos(np.deg2rad(angle)),-np.sin(np.deg2rad(angle)),0],[np.sin(np.deg2rad(angle)),np.cos(np.deg2rad(angle)),0],[0,0,1]])

def Gen_rot_slide(val):
    scale_mat = scale_matrix(x_scale_slider.val, y_scale_slider.val)
    rotate_matrix = Rot_matrix(rotp_slider.val)
    trans_matrix_back = transformation_matrix(x_trans_slider.val, y_trans_slider.val)
    rotate2_matrix = Rot_matrix(roto_slider.val)
    res_mat = np.dot(rotate2_matrix, np.dot(trans_matrix_back, np.dot(rotate_matrix, scale_mat)))
    normalized = np.vstack((points, np.ones((1,5))))
    normalized = np.dot(res_mat, normalized)
    normalized = np.delete(normalized, (2), axis=0)
    line.set_ydata(normalized[1])
    line.set_xdata(normalized[0])
    fig.canvas.draw_idle()

def res(mouse_event):
    x_trans_slider.reset()
    y_trans_slider.reset()
    x_scale_slider.reset()
    y_scale_slider.reset()
    rotp_slider.reset()
    roto_slider.reset()

fig, ax = plt.subplots(figsize = (7,7))

fig.subplots_adjust(left = 0.1, bottom = 0.3)
ax.set_xlim([-10,10])   #for limits of x and y axes
ax.set_ylim([-10,10])
plt.axvline(0,linestyle = ':',color = 'k')
plt.axhline(0,linestyle = ':',color = 'k')
[line] = plt.plot(points[0],points[1])

x_trans_slid = fig.add_axes([0.15,0.22,0.65,0.02])
x_trans_slider = Slider(x_trans_slid,'X transform',-9,9,valinit = 0,color='green')

y_trans_slid = fig.add_axes([0.15,0.19,0.65,0.02])
y_trans_slider = Slider(y_trans_slid,'Y transform',-9,9,valinit = 0,color='green')

x_scale_slid = fig.add_axes([0.15,0.16,0.65,0.02])
x_scale_slider = Slider(x_scale_slid,'X scale',0.1,4,valinit = 1,color='green')

y_scale_slid = fig.add_axes([0.15,0.13,0.65,0.02])
y_scale_slider = Slider(y_scale_slid,'Y scale',0.1,4,valinit = 1,color='green')

rotp_slid = fig.add_axes([0.15,0.10,0.65,0.02])
rotp_slider = Slider(rotp_slid,'rotate(pivot)',0,360,valinit = 0,color='green')

roto_slid = fig.add_axes([0.15,0.07,0.65,0.02])
roto_slider = Slider(roto_slid,'rotate(origin)',0,360,valinit = 0,color='green')

reset_button_axis = fig.add_axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(reset_button_axis, 'Reset')

x_trans_slider.on_changed(Gen_rot_slide)
y_trans_slider.on_changed(Gen_rot_slide)
x_scale_slider.on_changed(Gen_rot_slide)
y_scale_slider.on_changed(Gen_rot_slide)
rotp_slider.on_changed(Gen_rot_slide)
roto_slider.on_changed(Gen_rot_slide)
reset_button.on_clicked(res)

plt.show()
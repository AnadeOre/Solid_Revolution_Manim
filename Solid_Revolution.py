from manim import * 
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk    

class Solid_Revolution(ThreeDScene):
    def construct(self):

        axes = (
            ThreeDAxes(
                x_range=[-6, 6, 1],
                x_length=7,
                y_range=[-6, 6, 1],
                y_length=7,
                z_range=[-6, 6, 1],
                z_length=7
            )
        )

        f_text = MathTex(
            r'f(x) = \sqrt{x}'
            )
        g_text = MathTex(
            r'g(x) = x'
        )
        integral = MathTex(
            r'\int_{0}^{a} \pi(f(x)^2 - g(x)^2)\, dx'
        )

        f_text.set_color(BLUE_D).shift(2*RIGHT + 2*UP).scale(0.8)
        g_text.set_color(RED_D).shift(4*LEFT + UP).scale(0.8)
        integral.shift(3.2*RIGHT + 2*DOWN)

        integral[0][5:9].set_color(BLUE_D)
        integral[0][11:15].set_color(RED_D)

        curve_1 = axes.plot(lambda x: 2*np.sqrt(x), x_range=[0, 4.5], color=BLUE_D).set_shade_in_3d(True)
        curve_2 = axes.plot(lambda x: x, x_range=[0, 4.5], color=PURE_RED).set_shade_in_3d(True)

        area = axes.get_area(curve_2, [0, 4], bounded_graph=curve_1, color=GREY, opacity=0.5)
        
        surface_line = Surface(
            lambda u, v: axes.c2p(
                u, u*np.cos(v), u*np.sin(v)
            ),
            u_range=[0, 4.1],
            v_range = [0, 2*PI],
            checkerboard_colors=[RED_C, RED_C],
        ).set_fill(opacity=0.5)
        
        
        surface_sqrt = Surface(
            lambda u, v: axes.c2p(
                (v**2)/4, v*np.cos(u), v*np.sin(u)
            ),
            u_range=[0, 2*PI],
            v_range = [0,4.1],
            checkerboard_colors=[BLUE_C, BLUE_C],
        ).set_fill(opacity=0.5)
    


        self.set_camera_orientation(phi=-60*DEGREES, theta=-30*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
            LaggedStart(Create(axes), Create(curve_1), Create(curve_2)),
            run_time=2,
            lag_ratio=0.4
        )    
        self.wait(0.2)
        self.play(Create(area))
        self.wait(0.5)
        self.play(Create(surface_line))
        self.wait(2)
        self.play(Create(surface_sqrt))
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=-60*DEGREES, theta=85*DEGREES)
        self.play(surface_line.animate.set_color(GRAY), surface_sqrt.animate.set_color(GRAY))
        self.wait(0.1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.play(surface_sqrt.animate.set_color(BLUE_D), Write(f_text))
        self.wait(1)
        self.play(surface_sqrt.animate.set_color(GRAY))
        self.add_fixed_in_frame_mobjects(g_text)
        self.play(surface_line.animate.set_color(RED_D), Write(g_text))
        self.wait(1)
        self.play(surface_line.animate.set_color(GRAY))
        # self.add_fixed_in_frame_mobjects(f_text)
        # self.play(surface_sqrt.animate.set_color(BLUE_D), Write(f_text))
        # self.wait(1)
        # self.play(surface_sqrt.animate.set_color(GRAY))
        self.add_fixed_in_frame_mobjects(integral)
        self.play(Write(integral))
        self.wait(4)
# manim -pql -t Solid_Revol.py Solid_Revolution

from manim import * 
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk    

class Solid_Revolution(ThreeDScene):

    def construct(self):

      text = Text('Problemathic', font_size=100, font='CHAWP')
      text2 = Text('Follow us for more!', font_size=80, font='CHAWP')

      Youtube= ImageMobject("media/images/YouTubeLogo.png")
      Instagram= ImageMobject("media/images/InstagramLogo.png")
      Youtube.scale(0.05).shift(LEFT + DOWN)
      Instagram.scale(0.07).shift(RIGHT + DOWN)
      text2.shift(UP)

      axes = ThreeDAxes(
        x_range = [0,5,2],
        x_length = 5,
        y_range = [-4,4.1,2],
        y_length = 5,
        z_range = [-4,4,2],
        z_length = 5,
      )

      e = ValueTracker(2 * PI)

      f_text = MathTex(
            r'f(x) = \frac{x^2}{4}'
            )
      integral = MathTex(
            r'V = \pi\int_{0}^{a} [f(x)]^2\, dx'
        )
      
      f_text.set_color(YELLOW).shift(1.5*LEFT +  UP).scale(0.8).rotate(35 * DEGREES)
      integral.shift(4*RIGHT + 3*UP)

      integral[0][7:11].set_color(YELLOW)

      function = axes.plot(lambda x: 0.25 * x ** 2, x_range=[0, 4], color=YELLOW)
      area = axes.get_area(graph = function, x_range = [0,4], color = [BLUE_B, BLUE_D])

      surface = Surface(
        lambda u, v: axes.c2p(
          v, 0.25 * v **2 * np.cos(u), 0.25 * v ** 2 * np.sin(u)
        ),
        u_range = [0, 2 * PI],
        v_range = [0, 4],
        checkerboard_colors = [BLUE_B, BLUE_D],
      )

      self.play(Write(text))
      self.play(FadeOut(text))

      self.begin_ambient_camera_rotation()
      self.set_camera_orientation(phi = 45 * DEGREES, theta = -45 * DEGREES)
      self.play(
        LaggedStart(Create(axes), Create(function), Create(area), Write(f_text)),
        run_time = 4,
        lag_ratio = 0.5,
      )
      self.wait(0.5)
      self.play(FadeOut(f_text))
      self.play(Create(surface))
      self.play(
        Rotating(
            VGroup(function, area),
            axis=RIGHT,
            radians=2 * PI,
            about_point=axes.c2p(0, 0, 0),
        ),
        e.animate.set_value(2 * PI),
        run_time=5,
        rate_func=linear,
      )
      self.stop_ambient_camera_rotation()
      self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
      self.add_fixed_in_frame_mobjects(integral)
      self.play(Write(integral))
      self.wait(2)
      self.play(FadeOut(integral, surface, function, axes, area))
      self.add_fixed_in_frame_mobjects(text2)
      self.play(Write(text2))
      self.add_fixed_in_frame_mobjects(Youtube)
      self.add_fixed_in_frame_mobjects(Instagram)
      self.play(FadeIn(Youtube, Instagram))
      self.wait(2)
from manim import *

class SolidClassification(Scene):
    def construct(self):
        # Title
        title = Text("Classification of Solids").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Amorphous Solid
        amorphous_label = Text("Amorphous").next_to(title, DOWN, buff=0.5)
        amorphous_atoms = VGroup(*[
            Dot(point=ORIGIN + np.random.uniform(-0.5, 0.5, 3))
            for _ in range(50)
        ])
        amorphous_group = VGroup(amorphous_label, amorphous_atoms).arrange(DOWN).scale(0.8)

        # Crystalline Solid
        crystalline_label = Text("Crystalline").scale(0.8)
        crystalline_grid = VGroup(*[
            Dot(point=ORIGIN + np.array([x, y, 0]) * 0.2)
            for x in range(-5, 6) for y in range(-5, 6)
        ])
        crystalline_group = VGroup(crystalline_label, crystalline_grid).arrange(DOWN).scale(0.8)

        # Polycrystalline Solid
        polycrystalline_label = Text("Polycrystalline").scale(0.8)
        polycrystalline_clusters = VGroup(*[
            VGroup(*[
                Dot(point=np.array([x, y, 0]) * 0.1 + np.random.uniform(-0.05, 0.05, 3) + cluster_center)
                for x in range(-3, 4) for y in range(-3, 4)
            ])
            for cluster_center in [LEFT * 0.2 + UP * 0.2, RIGHT * 0.2 + UP * 0.2, LEFT * 0.2 + DOWN * 0.2, RIGHT * 0.2 + DOWN * 0.2]
        ])
        polycrystalline_group = VGroup(polycrystalline_label, polycrystalline_clusters).arrange(DOWN).scale(0.8)

        # Arrange all groups in a row
        all_groups = VGroup(amorphous_group, crystalline_group, polycrystalline_group).arrange(RIGHT, buff=1.5).shift(DOWN * 1.5)

        self.play(FadeIn(all_groups))
        self.wait(10)

if __name__ == "__main__":
    from manim import config
    config.background_color = WHITE
    scene = SolidClassification()
    scene.render()

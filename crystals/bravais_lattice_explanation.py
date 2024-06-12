from manim import *

class BravaisLatticeExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Bravais Lattice Explanation").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(FadeOut(title))

    
        # 1. Explain Bravais lattice with a diagram
        bravais_label = Text("Bravais Lattice").scale(0.8).to_edge(UP)
        bravais_explanation = Text(
            "A Bravais lattice is a repeating arrangement of points \n"
            "that completely fills up a space.", 
            font_size=24
        ).next_to(bravais_label, DOWN)
        bravais_points = VGroup(*[
            Dot(point=ORIGIN + np.array([x, y, 0]) * 0.6)
            for x in range(-3, 3) for y in range(-3, 3)
        ])
        bravais_diagram = VGroup(bravais_label, bravais_explanation, bravais_points)

        # Add space between title and matrix
        self.wait(1)

        self.play(FadeIn(bravais_diagram))
        self.wait(7)
        self.play(FadeOut(bravais_diagram))

        # 2. Explain lattice vectors
        lattice_vectors_label = Text("Lattice Vectors").scale(0.8).to_edge(UP)
        lattice_vectors_explanation = Text(
            "Lattice vectors are the vectors that connect two arbitrary \n"
            "lattice points, representing the type of translation symmetry.", 
            font_size=24
        ).next_to(lattice_vectors_label, DOWN)
        lattice_vectors = VGroup(
            Arrow(ORIGIN, RIGHT, buff=0, color=BLUE),
            Arrow(ORIGIN, UP, buff=0, color=GREEN),
        )
        lattice_vector_texts = VGroup(
            Text("a1", color=BLUE).next_to(lattice_vectors[0], DOWN),
            Text("a2", color=GREEN).next_to(lattice_vectors[1], LEFT)
        )
        lattice_vectors_diagram = VGroup(lattice_vectors_label, lattice_vectors_explanation, lattice_vectors, lattice_vector_texts)

        self.play(FadeIn(lattice_vectors_diagram))
        self.wait(2)
        self.play(FadeOut(lattice_vectors_diagram))

        # 3. Explain unit vectors
        unit_vectors_label = Text("Unit Vectors").scale(0.8).to_edge(UP)
        unit_vectors_explanation = Text(
            "Unit vectors are the smallest lattice vectors. \n"
            "In a 2D lattice, there are two unit vectors.", 
            font_size=24
        ).next_to(unit_vectors_label, DOWN)
        unit_vectors = VGroup(
            Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=BLUE),
            Arrow(ORIGIN, UP * 0.5, buff=0, color=GREEN),
        )
        unit_vector_texts = VGroup(
            Text("a1", color=BLUE).next_to(unit_vectors[0], DOWN),
            Text("a2", color=GREEN).next_to(unit_vectors[1], LEFT)
        )
        unit_vectors_diagram = VGroup(unit_vectors_label, unit_vectors_explanation, unit_vectors, unit_vector_texts)

        self.play(FadeIn(unit_vectors_diagram))
        self.wait(2)
        self.play(FadeOut(unit_vectors_diagram))

        # 4. Explain general lattice points
        general_lattice_label = Text("General Lattice Point").scale(0.8).to_edge(UP)
        general_lattice_explanation = Text(
            "A general lattice point can be represented as a combination \n"
            "of unit lattice vectors: R = c1 * a1 + c2 * a2",
            font_size=24
        ).next_to(general_lattice_label, DOWN)
        general_lattice_text = MathTex("R = c_1 a_1 + c_2 a_2").scale(0.8).next_to(general_lattice_explanation, DOWN)
        general_lattice_point = Dot(point=RIGHT * 1.5 + UP * 2.5, color=RED)
        general_lattice_vectors = VGroup(
            Arrow(ORIGIN, RIGHT * 1.5, buff=0, color=BLUE, stroke_width=3),
            Arrow(RIGHT * 1.5, RIGHT * 1.5 + UP * 2.5, buff=0, color=GREEN, stroke_width=3),
        )
        general_lattice_diagram = VGroup(general_lattice_label, general_lattice_explanation, general_lattice_text, general_lattice_point, general_lattice_vectors)

        self.play(FadeIn(general_lattice_diagram))
        self.wait(2)
        self.play(FadeOut(general_lattice_diagram))

        # 5. Explain Bravais Lattice
        final_bravais_label = Text("Bravais Lattice").scale(0.8).to_edge(UP)
        final_bravais_explanation = Text(
            "A Bravais lattice is a set of infinite points generated \n"
            "by a set of discrete translation operations described by \n"
            "lattice vectors. Each point has an identical environment.", 
            font_size=24
        ).next_to(final_bravais_label, DOWN)
        final_bravais_points = VGroup(*[
            Dot(point=ORIGIN + np.array([x, y, 0]) * 1.2)
            for x in range(-3, 4) for y in range(-3, 4)
        ])
        final_bravais_vectors = VGroup(
            Arrow(ORIGIN, RIGHT, buff=0, color=BLUE),
            Arrow(ORIGIN, UP, buff=0, color=GREEN),
        )
        final_bravais_texts = VGroup(
            Text("a1", color=BLUE).next_to(final_bravais_vectors[0], DOWN),
            Text("a2", color=GREEN).next_to(final_bravais_vectors[1], LEFT)
        )
        final_bravais_diagram = VGroup(final_bravais_label, final_bravais_explanation, final_bravais_points, final_bravais_vectors, final_bravais_texts)

        self.play(FadeIn(final_bravais_diagram))
        self.wait(2)
        self.play(FadeOut(final_bravais_diagram))

        # Final Hold
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.background_color = WHITE
    scene = BravaisLatticeExplanation()
    scene.render()

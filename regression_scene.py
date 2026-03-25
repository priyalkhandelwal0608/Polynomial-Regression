from manim import *
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

class RegressionScene(Scene):
    def construct(self):
        # --- Task 1 & 2: Generate Data ---
        np.random.seed(42)
        # X needs to be 2D for sklearn, but we'll flatten it for plotting
        X = np.sort(np.random.rand(20, 1) * 6 - 3, axis=0)
        y = np.sin(X).ravel() + np.random.normal(0, 0.2, X.shape[0])

        # --- Task 7: Create Sets of Axes ---
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_tip": True},
            x_length=10,
            y_length=6
        ).shift(DOWN * 0.5)
        
        # --- Task 9: Add Labels and Heading ---
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        title = Title("Polynomial Regression Analysis", include_underline=True)
        
        # Create a dynamic degree tracker text
        degree_text = Text("Degree: 0", font_size=24, color=BLUE).to_edge(UL, buff=1.5)
        
        self.add(axes, labels, title)

        # --- Task 8: Plot Data Points ---
        # We use .item() or float() to ensure Manim gets a scalar, not a 1-element array
        dots = VGroup(*[
            Dot(axes.c2p(x.item(), y_val), color=WHITE, radius=0.08) 
            for x, y_val in zip(X, y)
        ])
        self.play(Create(dots), Write(degree_text))
        self.wait(1)

        # --- Task 10, 11 & 12: Prepare and Animate Transformations ---
        current_graph = None
        error_msg = Text("MSE: 0.0000", font_size=24, color=RED).to_edge(UR, buff=1.5)
        self.add(error_msg)

        # Degrees to visualize
        degrees = [1, 2, 3, 7, 15]

        for deg in degrees:
            # --- Task 4 & 5: Model and Predict ---
            poly_features = PolynomialFeatures(degree=deg)
            X_poly = poly_features.fit_transform(X)
            model = LinearRegression().fit(X_poly, y)
            
            # Predict over a smooth range for the graph line
            def poly_func(x):
                x_p = poly_features.transform(np.array([[x]]))
                return model.predict(x_p)[0]

            # Create the new graph object
            new_graph = axes.plot(poly_func, color=YELLOW, x_range=[-3, 3])
            
            # --- Task 6: Calculate Error ---
            mse_val = mean_squared_error(y, model.predict(X_poly))
            
            # Prepare new labels for transformation
            new_degree_text = Text(f"Degree: {deg}", font_size=24, color=BLUE).move_to(degree_text)
            new_error_msg = Text(f"MSE: {mse_val:.4f}", font_size=24, color=RED).move_to(error_msg)

            # --- Task 12: Add Transformations ---
            if current_graph is None:
                self.play(
                    Create(new_graph),
                    Transform(degree_text, new_degree_text),
                    Transform(error_msg, new_error_msg),
                    run_time=1
                )
            else:
                self.play(
                    Transform(current_graph, new_graph),
                    Transform(degree_text, new_degree_text),
                    Transform(error_msg, new_error_msg),
                    run_time=1.5
                )
            
            current_graph = new_graph # Keep track of the current object to morph it next time
            self.wait(1)

        self.wait(2)
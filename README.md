# Polynomial Regression Visualization with Manim

This project uses the **Manim Community Edition** to create a mathematical animation of **Polynomial Regression**. It demonstrates how increasing the degree of a polynomial affects the model's fit, transitioning from underfitting to overfitting.

##  Features
- **Data Generation:** Synthetic noisy sine wave data created using NumPy.
- **Machine Learning:** Regression models built using `scikit-learn`.
- **Animations:** - Smooth transformations between polynomial degrees ($n=1$ to $n=15$).
    - Real-time display of **Mean Squared Error (MSE)**.
    - Dynamic axis and label rendering.

##  Technologies
- [Manim Community](https://www.manim.community/)
- Python 3.11+
- Scikit-Learn
- NumPy & SciPy

## Installation


   ```bash
   git clone [https://github.com/priyalkhandelwal0608/Polynomial-Regression.git](https://github.com/priyalkhandelwal0608/Polynomial-Regression.git)
   cd Polynomial-Regression
   pip install -r requirements.txt
   manim -pql regression_scene.py RegressionScene

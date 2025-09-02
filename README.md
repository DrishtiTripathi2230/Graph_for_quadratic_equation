# Quadratic Equation Solver & Grapher 📈

This Python project solves quadratic equations of the form:

\[
y = ax^2 + bx + c
\]

It calculates:
- *Discriminant (D)*  
- *Real roots* (if they exist)  
- *Vertex of the parabola*  
- *Y-intercept*  

and then plots the corresponding *parabola graph* with all these points marked.

---

## ✨ Features
- Handles all cases of discriminant:
  - *D < 0* → No real roots (parabola doesn’t touch x-axis)  
  - *D = 0* → One real root (parabola touches x-axis at vertex)  
  - *D > 0* → Two real roots (parabola cuts x-axis at two points)  
- Plots parabola using *matplotlib*  
- Marks:
  - Roots (if real)  
  - Vertex  
  - Y-intercept  
- Automatically adjusts x-range around vertex for a neat graph  

---

## 📦 Requirements
Make sure you have Python 3 installed, then install dependencies:

```bash
pip install matplotlib numpy


## EXAMPLE :
Enter values : 
<img width="478" height="145" alt="image" src="https://github.com/user-attachments/assets/4585d3db-4eb6-47de-94c0-0d6edaaef787" />

graph:
<img width="762" height="601" alt="image" src="https://github.com/user-attachments/assets/0581a56e-7ae6-4fe0-b2b5-736856f69e8b" />


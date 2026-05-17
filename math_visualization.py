{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1f014296",
   "metadata": {},
   "source": [
    "# Task 1: Mathematical Function Visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2c6fdd73",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# x range: -10 to 10, at least 200 points\n",
    "x1 = np.linspace(-10, 10, 250)\n",
    "\n",
    "# Functions\n",
    "y1 = x1\n",
    "y2 = x1**2\n",
    "y3 = np.sin(x1)\n",
    "y4 = np.exp(-0.1 * x1) * np.cos(x1)\n",
    "\n",
    "# Plotting\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(x1, y1, label='$y1 = x$', linestyle='-', color='blue')\n",
    "plt.plot(x1, y2, label='$y2 = x^2$', linestyle='--', color='orange')\n",
    "plt.plot(x1, y3, label='$y3 = sin(x)$', linestyle='-.', color='green')\n",
    "plt.plot(x1, y4, label='$y4 = e^{-0.1x} \\cdot cos(x)$', linestyle=':', color='red')\n",
    "\n",
    "plt.title('Mathematical Function Visualization')\n",
    "plt.xlabel('X-axis')\n",
    "plt.ylabel('Y-axis')\n",
    "plt.xlim(-10, 10)\n",
    "plt.ylim(-20, 20)  # y2 발산으로 인한 다른 그래프 묻힘 방지용 플롯 조정\n",
    "plt.legend()\n",
    "plt.grid(True)\n",
    "plt.savefig('function_plot.png', dpi=300)\n",
    "plt.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d34c78f5",
   "metadata": {},
   "source": [
    "# Task 2: Your Own Equation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "619ce4dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "x2 = np.linspace(-5, 5, 300)\n",
    "# [Short Comment] 이 방정식은 3차 함수와 코사인 함수를 결합하여 완만한 굴곡과 비대칭적 증가를 표현한 혼합 방정식입니다.\n",
    "y_own = 0.05 * x2**3 - 0.2 * x2**2 + np.cos(x2) + 3\n",
    "\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.plot(x2, y_own, label='$y = 0.05x^3 - 0.2x^2 + cos(x) + 3$', color='purple', linewidth=2)\n",
    "plt.title('Own Equation Plot (Mixed Cubic & Trigonometric)')\n",
    "plt.xlabel('X')\n",
    "plt.ylabel('Y')\n",
    "plt.grid(True)\n",
    "plt.legend()\n",
    "plt.savefig('own_equation.png', dpi=300)\n",
    "plt.close()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb4e9d25",
   "metadata": {},
   "source": [
    "# Task 3: Student Score Data Visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "33b2c1e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "students = [\"S1\", \"S2\", \"S3\", \"S4\", \"S5\", \"S6\", \"S7\", \"S8\", \"S9\", \"S10\"]\n",
    "midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])\n",
    "final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])\n",
    "\n",
    "# Calculate total score\n",
    "total = 0.4 * midterm + 0.6 * final\n",
    "\n",
    "# A. Scatter plot\n",
    "plt.figure(figsize=(6, 5))\n",
    "plt.scatter(midterm, final, color='darkblue', marker='o')\n",
    "plt.title('Midterm vs Final Exam Scores')\n",
    "plt.xlabel('Midterm Score')\n",
    "plt.ylabel('Final Score')\n",
    "plt.grid(True)\n",
    "plt.savefig('score_scatter.png', dpi=300)\n",
    "plt.close()\n",
    "\n",
    "# B. Histogram\n",
    "plt.figure(figsize=(6, 5))\n",
    "plt.hist(total, bins=5, color='skyblue', edgecolor='black', alpha=0.7)\n",
    "plt.title('Distribution of Total Scores')\n",
    "plt.xlabel('Total Score')\n",
    "plt.ylabel('Frequency')\n",
    "plt.grid(True)\n",
    "plt.savefig('score_histogram.png', dpi=300)\n",
    "plt.close()\n",
    "\n",
    "# C. Bar chart\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.bar(students, total, color='teal', edgecolor='black', alpha=0.8)\n",
    "plt.title('Total Score per Student')\n",
    "plt.xlabel('Students')\n",
    "plt.ylabel('Total Score')\n",
    "plt.grid(axis='y', linestyle='--')\n",
    "plt.savefig('score_bar_chart.png', dpi=300)\n",
    "plt.close()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5378b1e8",
   "metadata": {},
   "source": [
    "# Task 4: Best-Fit Line / Simple Prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ca4af440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Prediction Examples ---\n",
      "Predicted final score for midterm 50: 52.26\n",
      "Predicted final score for midterm 75: 74.88\n",
      "Predicted final score for midterm 100: 97.49\n",
      "\n",
      "All tasks completed successfully. Plots saved.\n"
     ]
    }
   ],
   "source": [
    "slope, intercept = np.polyfit(midterm, final, 1)\n",
    "\n",
    "# Generate line data for plotting\n",
    "x_line = np.linspace(55, 100, 100)\n",
    "y_line = slope * x_line + intercept\n",
    "\n",
    "plt.figure(figsize=(7, 5))\n",
    "plt.scatter(midterm, final, color='darkblue', label='Original Data Points')\n",
    "plt.plot(x_line, y_line, color='red', linestyle='--', label=f'Best-Fit Line ($y = {slope:.2f}x + {intercept:.2f}$)')\n",
    "plt.title('Midterm vs Final Score Prediction')\n",
    "plt.xlabel('Midterm Score')\n",
    "plt.ylabel('Final Score')\n",
    "plt.legend()\n",
    "plt.grid(True)\n",
    "plt.savefig('score_prediction.png', dpi=300)\n",
    "plt.close()\n",
    "\n",
    "# Print prediction examples\n",
    "print(\"\\n--- Prediction Examples ---\")\n",
    "\n",
    "test_midterms = [50, 75, 100]\n",
    "for m_score in test_midterms:\n",
    "    predicted_final = slope * m_score + intercept\n",
    "    print(f\"Predicted final score for midterm {m_score}: {predicted_final:.2f}\")\n",
    "\n",
    "print(\"\\nAll tasks completed successfully. Plots saved.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=3498DB&center=true&vCenter=true&width=700&lines=🚀+Dijkstra+Algorithm+Visualizer;Shortest+Path+Made+Interactive;Built+with+Python+%26+NetworkX" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-000000?style=for-the-badge&logo=networkx&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

<br/>

> **An interactive web application built with Python, Streamlit, and NetworkX to demonstrate and visualize Dijkstra's Algorithm in real-time.**

<br/>

[🚀 Features](#-features) • [📸 Screenshots](#-screenshots) • [⚙️ Installation](#️-installation) • [▶️ Usage](#️-usage) • [🛠️ Tech Stack](#️-tech-stack) • [👤 Author](#-author) • [📄 License](#-license)

---

</div>

## 📌 Overview

**Dijkstra-Visualizer** is a tool designed to help students and developers understand the internal workings of Dijkstra's Algorithm. It provides a clean, interactive interface to define a custom graph (nodes and weighted edges) and visualize the computation of the shortest path from a source node to all other nodes.

Whether you're studying for an exam or just curious about graph theory, this visualizer makes complex pathfinding concepts easy to grasp.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🕸️ **Custom Graph Input** | Define your own nodes and weighted edges via the sidebar |
| 📍 **Dynamic Shortest Path** | Instantly compute paths from any chosen start node |
| 🎨 **Visual Graph Rendering** | Real-time graph visualization using Matplotlib & NetworkX |
| 📑 **Step-by-Step Results** | View the shortest distance and actual path for every node |
| ⚡ **Interactive UI** | Fast and responsive interface powered by Streamlit |
| 🔍 **Algorithm Insight** | Observe how the greedy approach selects the best path |

---

## 📸 Screenshots

<div align="center">

### 📍 Path Calculation & Graph Output
<img src="https://raw.githubusercontent.com/aditya484/Dijkstra-Visualizer/main/screenshots/ouput1.png" alt="Path Calculation Output" width="100%"/>

<br/><br/>

### ⚙️ Sidebar Controls & Interaction
<img src="https://raw.githubusercontent.com/aditya484/Dijkstra-Visualizer/main/screenshots/Output2.png" alt="Sidebar Interaction" width="100%"/>

</div>

---

## 🛠️ Tech Stack

### 🖥️ Frontend / UI
| Library | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web interface and interactive components |
| [Matplotlib](https://matplotlib.org/) | Graph visualization and plot rendering |

### ⚙️ Backend Logic
| Library | Purpose |
|---|---|
| [Python 3.8+](https://python.org) | Core programming language |
| [NetworkX](https://networkx.org/) | Graph creation, manipulation, and pathfinding |
| [Heapq](https://docs.python.org/3/library/heapq.html) | Priority queue implementation for the algorithm |

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or above
- pip (Python package manager)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aditya484/Dijkstra-Visualizer.git
cd Dijkstra-Visualizer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the App

```bash
streamlit run app.py
```

### How to use:
1.  **Add Nodes:** Enter node names (e.g., A, B, C) in the sidebar.
2.  **Add Edges:** Define connections and their weights (e.g., A, B, 5).
3.  **Select Source:** Choose the starting node for the algorithm.
4.  **Visualize:** View the resulting graph and the shortest path table!

---

## 🧠 Dijkstra's Algorithm

Dijkstra's algorithm is a greedy algorithm that finds the shortest path between nodes in a graph, which may represent, for example, road networks. It works by:
1.  Assigning to every node a tentative distance value (0 for source, infinity for others).
2.  Setting the initial node as current.
3.  For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node.
4.  When we are done considering all neighbors of the current node, mark the current node as visited.

---

## 👤 Author

<div align="center">

### [Aditya Verma](https://github.com/aditya484)

[![GitHub](https://img.shields.io/badge/GitHub-aditya484-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aditya484)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aditya484/)
[![Email](https://img.shields.io/badge/Email-adityalkverma484@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:adityalkverma484@gmail.com)

</div>

---

## 🤝 Contributing

Contributions make the open-source community an amazing place!

1. 🍴 **Fork** the Project
2. 🌿 **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. ✅ **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. 📬 **Open a Pull Request**

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

⭐ Star this repo if you found it helpful!

</div>

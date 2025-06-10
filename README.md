# 🧪 Molecular Structure Isomorphism

## 🔬 Problem Statement

In chemical compound analysis, identifying whether two molecules have the same structure is a challenging task. Unlike typical graphs, **chemical structures** contain rich domain-specific information, such as atom types and covalent bonds. A **graph isomorphism** approach must take into account:

- **Atoms** as nodes with unique identification numbers.
- **Covalent bonds** as edges.
- Changing the ID of any node implies a structural change.

To solve this, we first **convert the molecular structure into a graph representation** and then apply graph isomorphism techniques. However, traditional algorithms may not handle these nuances effectively.

---

## ⚙️ Solution Approaches

### 1. VF2 Algorithm (Standard Graph Isomorphism)

We initially applied the **VF2 algorithm**, a well-established technique for subgraph and graph isomorphism.

#### 🔍 VF2 Matching Steps:
1. **Match empty set** with empty set — always valid.
2. **Attempt vertex-to-vertex matches** (e.g., match 1V with 1V′, 2V′, etc.).
3. If no match is found at a step, **backtrack** to the previous matching.
4. Repeat until all nodes are matched or a mismatch is confirmed.

> ✅ This method returns a **Boolean** value indicating whether two molecular graphs are isomorphic.

---

### 2. 🧠 Custom Backtracking Algorithm (Domain-Aware)

To enhance chemical accuracy and control, we implemented a **custom graph matcher** using a **backtracking algorithm**.

#### ✅ Features:
- Matches based on **degree sequences**.
- Compares **adjacency structures** between candidate nodes.
- Tracks **visited nodes** to prevent cycles and redundant comparisons.
- Uses **recursive backtracking** to explore all valid mappings.

#### 📁 Repository:
[🔗 Isomorphism of Organic Compounds – Backtracking Approach](https://github.com/GALI-SAI-SHANKAR/Isomorphism-of-Organic-Compounds)

---

## 🧪 Sample Code Snippet

```python
import numpy as np

def degrees(adj_matrix):
    return [np.count_nonzero(row == 1) for row in adj_matrix]

def degrees_positions(adj_matrix):
    return {i: [np.count_nonzero(row == 1)] for i, row in enumerate(adj_matrix)}

def next_positions(row):
    return [i for i, val in enumerate(row) if val == 1]

def GraphMatcher(adj_matrix_c1, adj_matrix_c2):
    if np.array_equal(adj_matrix_c1, adj_matrix_c2):
        return True
    if adj_matrix_c1.shape != adj_matrix_c2.shape:
        return False
    if sorted(degrees(adj_matrix_c1)) != sorted(degrees(adj_matrix_c2)):
        return False

    # Custom recursive backtracking implementation
    ...
```

---

## 📊 Results

Here’s how the comparison is performed step-by-step between two molecules (shown using adjacency matrices):

![Home](https://user-images.githubusercontent.com/80621346/176730119-ca79b1e3-98a8-4530-8506-4d323ec2f616.jpg)
![Results](https://user-images.githubusercontent.com/80621346/176730150-b2c2c285-dcbd-4002-bfdf-c70e3f7a8dea.jpg)

---

## ✅ Summary

| Feature                        | VF2 Algorithm   | Custom Backtracking Algorithm         |
| ------------------------------ | --------------- | ------------------------------------- |
| Flexibility for Chemical Rules | Limited         | High (custom logic can be integrated) |
| Performance on Small Graphs    | Fast            | Fast                                  |
| Customizable Matching          | Limited         | Fully customizable                    |
| Backtracking Control           | Internal to VF2 | Exposed for full user control         |
| Real-world Chemical Use Cases  | General-purpose | Optimized for molecule structures     |

---

## 🧑‍💻 Authors

* **Gali Sai Shankar**
* **Medhilesh**
* **Aumesh**
* **Krishna Ajay**
* Collaborators and contributors welcome!

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).


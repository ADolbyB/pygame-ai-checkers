<div align="center">

# 🎮 Pygame AI Checkers

### An Intelligent Checkers Game with Minimax Algorithm

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.2+-00C853?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![License](https://img.shields.io/github/license/ADolbyB/pygame-ai-checkers?style=for-the-badge)](LICENSE)
[![Build & Release Pygame Checkers](https://img.shields.io/github/actions/workflow/status/ADolbyB/pygame-ai-checkers/build-release.yml?style=for-the-badge&logo=github&logoColor=white&label=BUILD%20%26%20RELEASE)](https://github.com/ADolbyB/pygame-ai-checkers/actions/workflows/build-release.yml)

[![GitHub Stars](https://img.shields.io/github/stars/ADolbyB/pygame-ai-checkers?style=for-the-badge)](https://github.com/ADolbyB/pygame-ai-checkers/stargazers)
[![Forks](https://img.shields.io/github/forks/ADolbyB/pygame-ai-checkers?style=for-the-badge&logo=github)](https://github.com/ADolbyB/pygame-ai-checkers/network/members)
[![Repo Size](https://img.shields.io/github/repo-size/ADolbyB/pygame-ai-checkers?label=Repo%20Size&style=for-the-badge&logo=github)](https://github.com/ADolbyB/pygame-ai-checkers)

[Overview](#-overview) • 
[Features](#-features) • 
[Installation](#-installation) • 
[How to Play](#-how-to-play) • 
[Project Structure](#-project-structure) • 
[Algorithm](#-algorithm) • 
[Screenshots](#-screenshots)

</div>

---

## 📋 Overview

A fully functional checkers game built with Python and Pygame, featuring an AI opponent powered by the **Minimax algorithm using Alpha-Beta pruning**. This project demonstrates game development, AI decision-making, and object-oriented programming principles.

The AI opponent uses advanced game theory techniques to make intelligent moves, providing a challenging gameplay experience. Perfect for learning AI concepts, game development, or just enjoying a classic board game!

> **Note:** The baseline for this project was developed following [Tech With Tim's tutorial series](https://www.youtube.com/watch?v=vnd3RfeG3NM&list=PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3) as part of AI and game development research.

---

## ✨ Features

- 🤖 **Intelligent AI Opponent** - Powered by Minimax algorithm using Alpha-Beta pruning optimization.
- 🎨 **Clean Graphics** - Smooth animations and intuitive interface
- 🎯 **Valid Move Highlighting** - Shows all legal moves when a piece is selected
- 👑 **King Pieces** - Automatic promotion and enhanced movement
- ⚡ **Optimized Performance** - Alpha-beta pruning (coming soon) reduces computation time
- 🔄 **Turn-based Gameplay** - Alternating moves between player and AI

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher (for running from source)
- PyGame 2.5.2 or higher (for running from source)
- Conda or Mambaforge (recommended for development)
- Git

### Option 1: Download Pre-built Executable (Easiest) 🎯

**No Python installation required!** Just download and play.

#### Windows (64-bit)

1. **Download the latest release:**
   - Go to [Releases](https://github.com/ADolbyB/pygame-ai-checkers/releases/latest)
   - Download `Checkers-Windows-x64.zip`

2. **Extract and run:**
```bash
   # Extract the ZIP file to your preferred location
   # Double-click Checkers-Game.exe to play!
```

3. **Play the game:**
   - No installation needed
   - Just run `Checkers-Game.exe`

#### Linux (64-bit)

1. **Download the latest release:**
   - Go to [Releases](https://github.com/ADolbyB/pygame-ai-checkers/releases/latest)
   - Download `Checkers-Linux-x64.tar.gz`

2. **Extract and run:**
```bash
   # Extract the archive
   tar -xzf Checkers-Linux-x64.tar.gz
   cd Checkers-Linux
   
   # Run the game
   ./run.sh
   # OR
   ./Checkers-Game
```

> **Note:** Pre-built executables are standalone and don't require Python to be installed on your system.

---

### Option 2: Run from Source (For Development)

Perfect if you want to modify the code or contribute to the project.

#### Using Miniforge Environment (Recommended)

1. **Clone the repository:**
```bash
   git clone https://github.com/ADolbyB/pygame-ai-checkers.git
   cd pygame-ai-checkers
```

2. **Download Miniforge install script by Distro & Arch: Linux/MacOS/Win**

   - [Miniforge Releases](https://conda-forge.org/miniforge/)
   - GitHub [Repo](https://github.com/conda-forge/miniforge)

3. **Run Install Script & Initialize conda**
```bash
   bash Miniforge3-$(uname)-$(uname -m).sh
```

4. **Create and activate conda environment:**
```bash
   # Create environment with Python 3.10
   conda create -n checkers python=3.10
   
   # Activate the environment
   conda activate checkers
```

5. **Install dependencies:**
```bash
   # Install PyGame
   conda install conda-forge::pygame==2.5.2
```

6. **Run the game:**
```bash
   python checkersMain.py
```
---

### 🔧 System Requirements

#### For Pre-built Executables:
- **Windows:** Windows 10 or later (64-bit)
- **Linux:** Ubuntu 20.04+ or equivalent (64-bit)
- **RAM:** 512 MB minimum
- **Display:** 800x600 minimum resolution

#### For Running from Source:
- **Python:** 3.10 or higher
- **Pygame:** 2.5.2 or higher
- **OS:** Windows, Linux, or macOS

---

### ⚠️ Troubleshooting

**Windows - "Windows protected your PC" message:**
- Click "More info" → "Run anyway"
- This happens because the executable isn't digitally signed

**Linux - Permission denied:**
```bash
chmod +x Checkers-Game
./Checkers-Game
```

**Missing dependencies when running from source:**
```bash
pip install --upgrade pygame
```

---

## 🎯 How to Play

### Game Controls

- **🖱️ Left Click** - Select a piece and move it to a valid position (marked by blue dots)
- **❌ Window Close** - Exit the game

### Rules

1. **Red pieces** (you) move first
2. **Regular pieces** can only move diagonally forward
3. **Kings** (crowned pieces) can move diagonally in any direction
4. **Capture** opponent pieces by jumping over them
5. **Multiple jumps** are possible in a single turn
6. **Win** by capturing all opponent pieces or blocking all their moves

### Strategy Tips

- Control the center of the board early
- Advance pieces to the back row to create kings
- Force the AI into defensive positions
- Set up multi-jump opportunities
- Protect your back row to prevent AI kings

---

## 📁 Project Structure
```
pygame-ai-checkers/
│
├── checkers/                 # Core game modules
│   ├── __init__.py          # Package initialization
│   ├── board.py             # Game board logic and rendering
│   ├── constants.py         # Game constants (colors, dimensions)
│   ├── game.py              # Main game controller
│   └── piece.py             # Piece class and movement logic
│
├── minimax/                  # AI algorithm implementation
│   ├── __init__.py          # Package initialization
│   └── algorithm.py         # Minimax with alpha-beta pruning
│
├── assets/                   # Game assets
│   ├── GameBoard.png        # Screenshot for README
│   └── crown.png            # King piece indicator
│
├── checkersMain.py          # Entry point - run this file
├── __init__.py              # Root package initialization
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## 🧠 Algorithm

### Minimax (with Alpha-Beta Pruning)

The AI opponent uses the **Minimax algorithm with Alpha-Beta Pruning**, a decision-making algorithm for two-player games. It evaluates all possible moves and chooses the optimal one. The Alpha-Beta pruning version of minimax is an
optimized version to cut down AI decision time.

**Key Concepts:**

- **Minimax Tree**: Explores all possible game states up to a certain depth
- **Alpha-beta pruning**: reduces number of nodes evaluated by ~50-90%
- **Evaluation Function**: Scores board positions based on piece count and positioning
- **Recursive Search**: Explores future moves by simulating opponent responses

**Algorithm Flow:**

1. Generate all possible moves from current position
2. For each move, simulate the opponent's best response
3. Recursively evaluate positions to a set depth
5. Select the move with the highest evaluation score

**Performance:**
- Search depth: configurable (set to 5 levels currently)
- Evaluation function considers piece values and board control

---

## 📸 Screenshots

### Game Board

<div align="center">

![Game Board](checkers/assets/GameBoard.png)

*The classic 8x8 checkers board with red and white pieces. The AI plays as white.*

</div>

---

## 🎓 Learning Resources

This project demonstrates:

- **Object-Oriented Programming**: Classes for Board, Piece, and Game
- **Game Development**: Pygame fundamentals, event handling, and rendering
- **AI Algorithms**: Minimax decision-making with Alpha-Beta pruning optimization
- **Python Best Practices**: Clean code structure and modular design
- **Alpha-Beta Pruning**: Eliminates branches that won't affect the final decision, significantly reducing computation

### Project Next Steps

- Create a neural network-based AI
- Implement difficulty levels (varying search depth)
- Add a two-player mode
- Create a move history and undo feature
- Implement endgame databases
- Add sound effects and background music

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the GNU GPL v3 License - see the [License](https://github.com/ADolbyB/pygame-ai-checkers/blob/main/LICENSE.md) file for details.

---

## 👨‍💻 Author

**Joel Brigida**

- GitHub: [@ADolbyB](https://github.com/ADolbyB)
- Project Link: [https://github.com/ADolbyB/pygame-ai-checkers](https://github.com/ADolbyB/pygame-ai-checkers)

---

## Acknowledgments

- [Tech With Tim](https://www.youtube.com/c/TechWithTim) for the excellent tutorial series
- Pygame community for comprehensive documentation
- Minimax algorithm researchers for foundational AI concepts

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a star!

</div>
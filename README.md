# 🦋 Chronicles of Lumi

A 2D platformer game built with Python and Pygame Zero, featuring a pixel art aesthetic in black and white.

## 📖 Story

Welcome to the village, where you play as Lumi, a brave moth on a mission to collect scattered coins and defend the village from mysterious enemies.

## 🎮 Gameplay

- **Explore** a handcrafted platformer world
- **Collect** all coins scattered throughout the level
- **Defeat** enemies patrolling the territory
- **Avoid** deadly obstacles
- **Complete** the mission by collecting all coins and defeating all enemies

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ⬅️ **LEFT ARROW** | Move left |
| ➡️ **RIGHT ARROW** | Move right |
| ⬆️ **UP ARROW** | Jump |
| **D** | Attack |
| **SPACE** | Return to menu (Game Over/Win screen) |

## ✨ Features

- 🎨 Minimalist black and white pixel art
- 🎵 Background music and sound effects
- 👾 Enemy AI with patrol behavior
- ⚔️ Combat system with attack animations
- 🏃 Smooth character animations (idle, walk, jump, attack)
- 🎯 Challenging platformer mechanics
- 🏆 Win condition: collect all coins + defeat all enemies

## 📋 Requirements

- Python 3.7+
- Pygame Zero

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/poeisie/chronicles-of-lumi.git
cd chronicles-of-lumi
```

2. Install dependencies:
```bash
pip install pgzero pygame
```

3. Run the game:
```bash
python game.py
```

Or using pgzrun:
```bash
pgzrun game.py
```

## 📁 Project Structure

```
chronicles-of-lumi/
├── game.py                  # Main game file
├── platformer.py            # Game utilities and Actor classes
├── images/                  # Sprite images
│   ├── p_left.png
│   ├── p_right.png
│   ├── p_walk_left.png
│   ├── p_walk_right.png
│   ├── p_attack_left.png
│   ├── p_attack_right.png
│   ├── p_jump.png
│   ├── enemy_idle.png
│   ├── enemy_walk_left.png
│   ├── enemy_walk_right.png
│   └── tiles/               # Level tiles
├── music/                   # Background music (.ogg files)
│   ├── theme.ogg
│   ├── game_over.ogg
│   └── win.ogg
├── sounds/                  # Sound effects (.wav files)
│   ├── jump.wav
│   ├── coin.wav
│   └── attack.wav
└── *.csv                    # Level data files
```

## 🎨 Asset Credits

- **Graphics**: [1-Bit Platformer Pack](https://kenney.nl/assets/1-bit-platformer-pack) by Kenney
- **Music/Sounds**: [8-Bit RPG Adventure and Fantasy Music Pack - Pixel Adventures Vol. 1](https://domiwav.itch.io/8-bit-rpg-adventure-and-fantasy-music-pack-pixel-adventures-vol-1) by Dominik Wawszczyszyn (domiwav)

## 🎵 Audio Settings

The game includes options to toggle:
- **Music**: ON/OFF (background music)
- **Sounds**: ON/OFF (sound effects)

Access these settings from the main menu.

## 🏗️ Built With

- [Python](https://www.python.org/) - Programming language
- [Pygame Zero](https://pygame-zero.readthedocs.io/) - Game framework
- [Pygame](https://www.pygame.org/) - Multimedia library

## 👥 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

None at the moment. Please report any bugs you find!

## 📧 Contact

Created by [@poeisie](https://github.com/poeisie)

---

**Enjoy playing Chronicles of Lumi! 🦋✨**

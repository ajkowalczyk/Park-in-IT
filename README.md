# 🅿️ Park'in IT!

A 2D parking simulation / puzzle game built in Python.

The goal is simple… at least in theory:

Park your car perfectly without hitting obstacles, other vehicles, or your own patience limit.

This project doesn't aim to reinvent the genre.
It is inspired by the classic game *Parking Mania*, while the implementation and architecture are built from scratch.

The name is just a wordplay I found fun, and I simply wanted to build something fun.

Yes - parts of this README were generated with AI (and then edited).
Some sprites might also be AI-generated.

**The code itself is written by me.**

---

## 🎮 Features (Planned)

* [ ] 🚗 Player-controlled car
* [ ] 🅿️ Precision parking detection
* [ ] 🧱 Obstacles and tight parking spaces
* [ ] 🗺️ Multiple levels / parking maps
* [ ] ⏱️ Timers and scoring system
* [ ] 🔊 Sound effects & engine audio
* [ ] 💾 Save system
* [ ] 🤖 NPC traffic

---

## 📌 Project Status

Current phase: **Early Prototype**

Core driving physics and parking logic are currently in development.
Assets and level design are currently placeholders and work in progress.

---

## 📁 Project Structure

The project is organized into a modular structure to separate responsibilities and keep the codebase scalable:

```text
park-in-it/
├── README.md
├── main.py                  # Entry point of the application
│
└── src/
    ├── core/                # Main game control
    │   ├── config.py        # Game configuration and constants
    │   ├── game.py          # Main game class and game loop
    │   └── renderer.py      # Rendering layer / display logic
    │
    ├── entities/            # Game world objects
    │   └── car.py           # Car entity
    │
    └── systems/             # Game mechanics and logic
        ├── input.py         # Input abstraction / player actions
        ├── physics.py       # Movement and motion rules
        └── parking_logic.py # Parking validation logic
```

### 🧠 Architecture Overview

* **Core** → Controls the game flow and rendering
* **Entities** → Represent objects in the game world
* **Systems** → Handle mechanics such as input, movement, and parking rules

This separation keeps the project easier to maintain and makes future frontend or rendering changes more manageable.

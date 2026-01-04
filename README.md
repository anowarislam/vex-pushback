# VEX V5 Robot Project

A professional VEX V5 robot programming project using Python with VS Code + VEX Extension.

## Wiring Table

| Port | Device | Code Variable | Notes |
|------|--------|---------------|-------|
| 1 | Left Front Motor | `left_motor_front` | Green cartridge (18:1) |
| 2 | Left Back Motor | `left_motor_back` | Green cartridge (18:1) |
| 3 | Right Front Motor | `right_motor_front` | Green cartridge (18:1), Reversed |
| 4 | Right Back Motor | `right_motor_back` | Green cartridge (18:1), Reversed |
| 5 | (Available) | - | Reserved for Inertial Sensor |
| 6 | (Available) | - | |
| 7 | (Available) | - | |
| 8 | (Available) | - | |

## Project Structure

```
vex/
├── src/
│   ├── main.py           # Entry point - downloads to Brain
│   ├── robot_config.py   # Motor/sensor configuration
│   ├── autonomous.py     # Autonomous routines
│   ├── driver_control.py # Tank/arcade drive control
│   └── utils.py          # Helper functions
├── tests/                # Pytest test suite
│   ├── conftest.py       # VEX module mocks
│   └── test_*.py         # Test files
├── docs/
│   └── adr/              # Architecture Decision Records
├── venv/                 # Python virtual environment
├── .vscode/              # VS Code settings
├── Makefile              # Build/test commands
└── README.md             # This file
```

## Setup

### Prerequisites
- VS Code with VEX Robotics Extension
- Python 3.8+

### Installation

1. Open this folder in VS Code
2. The virtual environment is already created with VEX stubs for IntelliSense
3. Install the VEX Robotics extension if not already installed

### Activate Virtual Environment (for terminal use)

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```powershell
venv\Scripts\activate
```

## Usage

### Download to Robot

1. Connect V5 Brain via USB-C
2. Click the VEX icon in VS Code sidebar
3. Select `src/main.py` as your project file
4. Click Download button in toolbar
5. Select program slot (1-8)
6. Run from Brain or click Play

### Drive Modes

**Tank Drive** (default): Left stick controls left motors, right stick controls right motors.

**Arcade Drive**: Uncomment in `main.py` to use - left stick forward/back and turn.

## Autonomous

Edit `src/autonomous.py` to implement your competition strategy:

- `autonomous_routine()` - Main 15-second autonomous
- `skills_autonomous()` - 60-second skills routine
- `autonomous_left()` / `autonomous_right()` - Position-specific routines

## Competition Mode

For competitions, uncomment the Competition class section in `main.py`. This enables proper autonomous/driver period switching.

## Modifying Hardware

1. Update port numbers in `src/robot_config.py`
2. Update the wiring table above
3. Add sensors by uncommenting examples in `robot_config.py`

## Testing

Run tests locally without robot hardware:

```bash
make test          # Run all 48 tests
make test-cov      # Run with coverage report
make test-watch    # Auto-rerun on file changes
```

Tests use mocked VEX modules to verify logic without hardware. See [ADR-0001](docs/adr/0001-local-testing-strategy.md) for details on the testing strategy.

## Tutorials

**New to robotics?** Start with our comprehensive tutorial series designed for 8th-grade students:

📚 **[Start Learning →](docs/tutorials/README.md)**

The tutorials cover:
- **Physics Foundations** - Forces, gears, friction
- **Robot Anatomy** - Brain, motors, sensors
- **Python Basics** - Variables, functions, loops
- **Drive Control** - Tank and arcade drive
- **Autonomous** - Programming your robot to move on its own
- **Competition Strategy** - Push Back 2025-2026 game tactics
- **Advanced Topics** - PID control, sensor integration, skills programming

## Documentation

Architecture Decision Records (ADRs) document key project decisions:

| ADR | Title | Status |
|-----|-------|--------|
| [0001](docs/adr/0001-local-testing-strategy.md) | Local Testing Strategy | Accepted |

## Resources

- [VEX V5 Python API](https://api.vex.com/v5/home/python/index.html)
- [VEX Knowledge Base](https://kb.vex.com/hc/en-us/categories/360002333191-V5)
- [VEX Forum](https://www.vexforum.com)
- [VEXcode VR](https://vr.vex.com) - Virtual robot for strategy prototyping

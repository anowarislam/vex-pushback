# ADR-0001: Local Testing Strategy for VEX V5 Robot Code

## Metadata
| Field | Value |
|-------|-------|
| **Date** | 2026-01-03 |
| **Status** | Accepted |
| **Supersedes** | N/A |
| **Superseded by** | N/A |

## Context

VEX V5 robot code is written in Python using the `vex` module, which only exists on the V5 Brain hardware. This creates a challenge for local development:

1. **Hardware dependency**: The `vex` module provides `Brain`, `Motor`, `Controller`, and other classes that interface directly with hardware
2. **Slow feedback loop**: Without local testing, every code change requires downloading to the robot
3. **Limited availability**: Robot hardware may not always be accessible (shared team resources, travel, etc.)
4. **Competition risk**: Untested code deployed during competition can cause failures

We evaluated multiple simulation options to enable local testing of VEX V5 Python code.

## Decision

We will use **pytest with comprehensive VEX module mocks** as our primary local testing strategy.

### Implementation Details

1. **Mock the entire `vex` module** in `tests/conftest.py` using pytest fixtures
2. **Track state in mocks** (velocity, spinning, commands) to verify behavior
3. **Auto-inject mocks** before each test using `@pytest.fixture(autouse=True)`
4. **Separate test categories**: unit tests (pure logic), integration tests (module interactions)

### Deferred Decisions

- **VEXLib integration**: Will evaluate if autonomous algorithms become complex enough to warrant Dijkstra/PID simulation tools
- **VEXcode VR workflow**: May create separate VR-compatible files for high-level strategy prototyping

## Consequences

### Positive
- **Fast feedback loop**: 48 tests execute in 0.04 seconds
- **No hardware required**: Can develop and test anywhere
- **CI/CD ready**: Tests can run in automated pipelines
- **Logic verification**: Catches bugs in control flow, state management, math
- **Regression prevention**: Tests document expected behavior

### Negative
- **No physics simulation**: Cannot test motor torque, friction, inertia, weight distribution
- **No sensor simulation**: Cannot simulate real sensor noise or timing
- **API drift risk**: Mocks may diverge from actual VEX API over time
- **False confidence**: Passing tests don't guarantee hardware behavior

### Neutral
- Still requires hardware testing for final validation (this was always true)
- Mocks need maintenance as robot configuration changes

## Alternatives Considered

### Alternative 1: VEXcode VR
**Description:** Official browser-based VEX robot simulator at [vr.vex.com](https://vr.vex.com)

**Pros:**
- Official VEX product, well-maintained
- Visual simulation with physics
- Competition field playgrounds available

**Cons:**
- Uses `from vexcode import *` not `from vex import *` (different API)
- Pre-configured robot only (can't test custom 4-motor tank drive)
- Code doesn't transfer directly to physical robot
- Browser-based, not integrated with local dev workflow

**Why not chosen:** API incompatibility means we can't test our actual code

### Alternative 2: VEX Virtual Skills
**Description:** Competition-specific virtual playgrounds for V5RC season games

**Pros:**
- Similar API to physical V5
- Competition field with game elements
- GPS and sensor simulation

**Cons:**
- Pre-configured robot (not our custom configuration)
- Web-based, not local
- Season-specific (changes yearly)

**Why not chosen:** Cannot test custom robot configuration

### Alternative 3: VEX V5 Simulator (GitHub Community Project)
**Description:** C++/SDL2 simulator at [github.com/BA-Robotics-Unofficial/Vex-V5-Simulator](https://github.com/BA-Robotics-Unofficial/Vex-V5-Simulator)

**Pros:**
- Open source, community-driven
- Plans for C++ and Python support

**Cons:**
- Very early development stage
- Only basic rendering implemented
- No code execution capability yet
- Windows-only testing

**Why not chosen:** Not mature enough for practical use

### Alternative 4: VEXLib Framework
**Description:** Python framework with simulation tools at [deekb.github.io/VEXlib](https://deekb.github.io/VEXlib/vexlib.html)

**Pros:**
- Dijkstra pathfinding simulation
- PID analysis tools
- Unit/integration testing framework
- Log sync from robot

**Cons:**
- Additional framework to learn
- May duplicate our pytest setup
- Overkill for current project scope

**Why not chosen (for now):** Current algorithm complexity doesn't warrant it. **May revisit** if autonomous routines become more sophisticated.

## References

- [VEX V5 Python API Documentation](https://api.vex.com/v5/home/python/index.html)
- [VEXcode VR API Documentation](https://api.vex.com/vr/home/)
- [VEX Python Stubs (IntelliSense)](https://github.com/GraderThan/vex-v5-python-interface)
- [VEXLib Framework](https://deekb.github.io/VEXlib/vexlib.html)
- [Project Test Suite](/tests/)

---

## Implementation Checklist

- [x] Create `tests/conftest.py` with comprehensive VEX mocks
- [x] Create `tests/test_utils.py` for utility function tests
- [x] Create `tests/test_robot_config.py` for configuration tests
- [x] Create `tests/test_driver_control.py` for drive logic tests
- [x] Create `tests/test_autonomous.py` for autonomous routine tests
- [x] Add `make test` target to Makefile
- [x] Verify all 48 tests pass

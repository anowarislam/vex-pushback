# Parent's Guide to VEX V5 Robotics

> A comprehensive guide to understanding your child's robotics journey and asking the right questions.

---

## Part 1: Quick Overview

### What Your Child Will Learn

Your child is embarking on a hands-on journey into robotics, programming, and competitive strategy through the **VEX V5 Push Back** competition (2025-2026 season). This curriculum is designed for 8th-grade students with zero prior coding experience and takes approximately **5 hours** across multiple sessions.

By the end, your child will be able to:
- Write Python code that controls a physical robot
- Understand the physics behind robot movement (forces, gears, friction)
- Design autonomous routines that run without human control
- Develop strategic thinking for competitive matches
- Work as part of an alliance team under time pressure

### The Competition: VEX V5 Push Back

**The basics:** Two alliances (2 robots each) compete on a 12' × 12' field. The goal is to push colored blocks into scoring goals while defending your zones.

**Match structure:**
| Phase | Duration | What Happens |
|-------|----------|--------------|
| Autonomous | 15 seconds | Robot runs pre-programmed code (no human control) |
| Driver Control | 1 min 45 sec | Human driver controls the robot |

**Why it matters:** Your child learns that robotics isn't just about building—it's about strategy, timing, coding, and teamwork.

### Learning Roadmap

| Module | Time | What They Learn |
|--------|------|-----------------|
| 0. Welcome | 15 min | Code structure, development setup |
| 1. Physics Foundations | 45 min | Forces, gears, friction—why robots move |
| 2. Robot Anatomy | 30 min | Brain, motors, sensors—what's inside |
| 3. Python Basics | 45 min | Variables, functions, loops—how to code |
| 4. Drive Control | 30 min | Tank/arcade drive, driver skills |
| 5. Autonomous | 45 min | Pre-programmed movements, timing |
| 6. Competition Strategy | 30 min | Scoring, alliance coordination |
| 7. Advanced Topics | 60 min | PID control, sensors (optional) |

### Milestones to Celebrate

These are moments worth acknowledging:

1. **First successful code run** - The robot responds to their code
2. **Understanding motor reversal** - They can explain why right motors spin "backward"
3. **Tank vs. arcade explanation** - They know the trade-offs of each control scheme
4. **First autonomous routine** - Robot moves on its own following their code
5. **Strategic thinking** - They discuss parking vs. scoring decisions
6. **Debugging success** - They fix a problem without help

---

## Part 2: Questions to Ask Your Child

Use these questions to spark conversation and check understanding. Each includes a brief answer hint so you can follow along.

### Module 1: Physics Foundations

**1. Why does a heavier robot push other robots more easily, but also move slower?**
*(Newton's 2nd Law: Force = Mass × Acceleration. More mass means more pushing force, but the same motor power results in less acceleration.)*

**2. What happens if your robot's wheels spin but it doesn't move?**
*(The wheels have overcome friction—they're slipping. This means traction is lost, possibly because the robot is too light or the floor is slippery.)*

**3. Why would you choose a red motor cartridge over a blue one?**
*(Red gives high torque (pushing power) but low speed. Blue gives high speed but low torque. It's a trade-off based on what the robot needs to do.)*

**4. If two robots are pushing each other and neither moves, what's happening?**
*(The forces are balanced—Newton's 3rd Law. Each robot pushes equally on the other.)*

**5. Why do some wheels have rollers on them?**
*(Omni wheels have rollers that allow sideways sliding, making turning easier. Traction wheels grip in all directions but make turns harder.)*

### Module 2: Robot Anatomy

**1. Why does the robot need to know which port each motor is connected to?**
*(The code sends commands to specific port numbers. If a motor is on port 1, the code must reference port 1 to control it.)*

**2. Why are the right-side motors "reversed" in the code?**
*(Motors on opposite sides face opposite directions. Without reversing, telling both sides to spin "forward" would make the robot turn instead of drive straight.)*

**3. What's the difference between the Brain and the Controller?**
*(The Brain is the robot's computer—it runs the code. The Controller is what the driver holds—it sends joystick and button inputs to the Brain wirelessly.)*

**4. What can sensors tell the robot that the driver can't see?**
*(Exact heading angle, precise distance to objects, whether it's the right color block. Humans estimate; sensors measure precisely.)*

**5. Why does the robot need to "calibrate" before using certain sensors?**
*(The inertial sensor needs to establish a reference point for "straight." If it calibrates while moving, all readings will be off.)*

### Module 3: Python Basics

**1. Why do programmers create functions instead of writing the same code multiple times?**
*(Functions are reusable. Write once, use anywhere. If you need to fix something, you fix it in one place.)*

**2. What's the difference between a variable that stores a number vs. one that stores True/False?**
*(Numbers (int/float) are for calculations like speed. Booleans (True/False) are for decisions like "is the intake running?")*

**3. Why would the robot do something forever using a loop?**
*(Driver control needs to continuously read joystick inputs. Without a loop, it would read once and stop listening.)*

**4. What happens if the code says "turn 90 degrees" but doesn't wait for it to finish?**
*(The next command might run immediately, overlapping with the turn. The robot could try to drive forward while still turning.)*

**5. Why would you draw a flowchart before writing code?**
*(Flowcharts show the logic without worrying about syntax. It's easier to spot problems in a diagram than in code.)*

### Module 4: Drive Control

**1. When would tank drive be better than arcade drive?**
*(Tank drive gives independent control of each side, making pivot turns and defensive pushing easier. Arcade is smoother for curves but less precise.)*

**2. Why does the code ignore small joystick movements (deadband)?**
*(Real joysticks aren't perfectly centered—they drift slightly. Without deadband, the robot would creep even when nobody touches the controller.)*

**3. What's the advantage of using a control "curve" that makes small movements even smaller?**
*(Precision. When pushing blocks into a goal, you need tiny adjustments. A curve lets you have fine control at low speeds and full power at high speeds.)*

**4. Why practice driving in squares and figure-8s?**
*(These patterns develop muscle memory for common movements—straight lines, turns, and smooth curves. Competition drivers need these instinctively.)*

**5. What should the driver prioritize in the last 10 seconds of a match?**
*(Parking. Two robots parked = 30 points, which often outweighs any blocks they could score in that time.)*

### Module 5: Autonomous Programming

**1. Why is the 15-second autonomous period so important?**
*(It can earn a 10-point bonus and score blocks before the opponent. A good autonomous can determine the match outcome.)*

**2. What's the risk of making the robot move too fast during autonomous?**
*(Overshooting. The robot might drive past its target or turn too far, throwing off all subsequent movements.)*

**3. Why do autonomous routines include "wait" commands between movements?**
*(To let the robot stabilize. Momentum continues after a command ends—a brief pause prevents drift.)*

**4. How do you fit multiple scoring actions into just 15 seconds?**
*(Optimize: faster speeds where safe, shorter waits, and overlapping actions like running the intake while driving.)*

**5. What does "blocking vs. non-blocking" mean in robot commands?**
*(Blocking commands wait until finished (drive 500mm, then continue). Non-blocking commands start and return immediately (start intake, keep going). This enables multitasking.)*

### Module 6: Competition Strategy

**1. Why is parking two robots worth so much more than parking one?**
*(8 points for one vs. 30 for both. It's a teamwork incentive—coordinating with your alliance partner is heavily rewarded.)*

**2. How can removing opponent blocks from a goal be worth more than just scoring your own?**
*(Point swing. If they had zone control (10 points to them), removing blocks gives you control (+10 to you). That's a 20-point shift from one action.)*

**3. What should alliance partners decide before a match starts?**
*(Who covers which field area, what autonomous routines to run (avoiding collisions), and who parks first at the end.)*

**4. When would you stop trying to score and focus on defense?**
*(When you're ahead and time is short. Defending a lead by blocking opponents can be more valuable than risking a turnover.)*

**5. What's the difference between a match and a skills challenge?**
*(Match: 2 vs. 2, 2 minutes. Skills: solo robot, 60 seconds, trying to maximize points alone. Skills determines tournament rankings.)*

### Module 7: Advanced Topics

**1. Why does smooth "proportional" control work better than just "on/off" control?**
*(On/off overshoots the target and oscillates. Proportional slows down as you approach, stopping precisely.)*

**2. What does the "I" in PID help solve?**
*(Steady-state error. If friction prevents reaching the exact target, accumulated error builds up and adds extra push to overcome it.)*

**3. Why would a robot use a sensor instead of just timing its movements?**
*(Conditions change. Battery level affects speed, wheels slip, obstacles appear. Sensors let the robot react to what's actually happening.)*

**4. In a 60-second skills run, why is time budgeting critical?**
*(You must reserve time for parking. Spending too long in one area leaves no time for others—or worse, forgetting to park costs 8+ points.)*

**5. What does "closed-loop control" mean?**
*(The robot measures its actual state (via sensors) and adjusts continuously. Open-loop just guesses based on time.)*

---

## Part 3: Deep Dive Appendix

*This section is optional reading for parents who want more detail.*

### Complete Scoring Reference

| Action | Points | Notes |
|--------|--------|-------|
| Block scored | 3 | Each block pushed into any goal |
| Long goal zone control | 10 | Having more blocks than opponent in left or right goal |
| Center goal upper zone | 8 | Majority in upper section of center goal |
| Center goal lower zone | 6 | Majority in lower section of center goal |
| 1 robot parked | 8 | Your robot in alliance park zone at end |
| 2 robots parked | 30 | Both alliance robots parked (same zone or separate) |
| Autonomous bonus | 10 | Win the 15-second autonomous period |

**Autonomous Win Point requirements** (all must be met):
1. Score 7+ blocks of your alliance color
2. Blocks in at least 3 different goals
3. Remove 3+ blocks from loaders
4. Neither robot touching park zone barrier

### Career Connections

This curriculum connects directly to professional fields:

**Mechanical Engineering**
- Physics of motion, forces, torque
- Gear ratios and trade-offs
- Robot design decisions

**Software Engineering**
- Python programming fundamentals
- Control systems (PID)
- Debugging and testing

**Electrical Engineering**
- Sensor integration
- Motor control and power
- Wiring and connections

**Product Management**
- Trade-off analysis (speed vs. torque, scoring vs. parking)
- Prioritization under constraints
- User experience (driver ergonomics)

**Program Management**
- Time budgeting (15-second autonomous, 60-second skills)
- Coordination with partners
- Risk management and fallback plans

**Data Science**
- Sensor data interpretation
- Feedback loops
- Optimization algorithms

### Glossary

| Term | Simple Definition |
|------|-------------------|
| **Autonomous** | The 15-second period where the robot runs pre-written code without human control |
| **Alliance** | Your team of 2 robots working together against the opposing 2 |
| **Deadband** | Ignoring small joystick movements to prevent drift |
| **Drivetrain** | The motors and wheels that move the robot |
| **Encoder** | Sensor inside motors that tracks rotation precisely |
| **Gear ratio** | Relationship between motor speed and wheel speed |
| **IMU (Inertial sensor)** | Sensor that knows which direction the robot faces |
| **Motor cartridge** | Color-coded gear set (blue/green/red) that sets speed/torque |
| **PID** | Control algorithm for precise movements (Proportional-Integral-Derivative) |
| **Port** | Numbered connection point on the Brain (1-21) |
| **Skills challenge** | Solo 60-second run to score maximum points |
| **Tank drive** | Control scheme: left stick = left wheels, right stick = right wheels |
| **Arcade drive** | Control scheme: one stick controls forward/backward and turning |
| **Torque** | Rotational force (twisting power) |

### Frequently Asked Questions

**What if my child gets stuck?**
Encourage them to re-read the tutorial section and try the review questions. Debugging is part of learning—resist solving it for them. If truly stuck, the troubleshooting appendix covers common issues.

**How much should I help?**
Ask questions rather than giving answers. "What did you expect to happen?" and "What actually happened?" are more valuable than fixing the code yourself.

**What equipment is needed?**
- Computer with VS Code installed
- VEX V5 robot kit (provided by school/team)
- The code repository (already set up)

**Can I watch competitions?**
Absolutely! VEX competitions are open to spectators. Watching matches helps you understand what your child is working toward.

**What if my child wants to go deeper?**
Module 7 (Advanced Topics) is optional and covers sophisticated concepts like PID control. Many students also explore custom mechanisms, vision sensors, or more complex autonomous routines.

---

## Navigation

**← Previous:** [Welcome to VEX V5 Robotics](./index.md)

**→ Next:** [Physics Foundations: Forces and Motion](../01-physics-foundations/01-forces-and-motion.md)

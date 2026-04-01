# COMP6009 — Autonomous Robot Navigation
Autonomous mobile robot navigation system built with ROS1, TurtleBot3, and Gazebo. Implements SLAM for real-time mapping and localisation, and A* pathfinding for autonomous navigation in simulated environments.

> University of Kent — COMP6009 Cognitive Robotics | Grade: 95%

---

## Technologies
- ROS1 (Noetic)
- TurtleBot3
- Gazebo / RViz
- SLAM (Karto)
- A* Pathfinding
- Python
- Docker

---

## Project Overview
This project implements shortest-path autonomous navigation for a TurtleBot3 robot in a simulated Gazebo maze environment.

The robot uses Karto SLAM to build a map of its environment in real time, then uses A* pathfinding to plan and execute an optimal route to a target destination. The full navigation stack is visualised in RViz.

Three SLAM methods were evaluated — Hector, RTAB, and Karto. Karto was selected for its accuracy and stability in the simulated environment. Generated map files (`.yaml` and `.pgm`) are saved under `turtlebot3_karto`.

---

## Contributors
- **Nathaniel Kisakye** — Led system design and integration, implemented SLAM (Karto) pipeline, and integrated path planning within the ROS navigation stack

- **Samuel Ametefe** — A* pathfinding contribution

---

## Environment Setup (Docker)

### Step 1 — Ensure Docker is running
Start Docker Desktop before continuing, then open your container terminal.

### Step 2 — Clone and build the workspace
```bash
# 1. Clone the repository
git clone https://github.com/omxln/autonomous-navigation-robot.git

# 2. Enter the workspace
cd autonomous-navigation-robot

# 3. Build the project
catkin_make

# 4. Source the setup file
source devel/setup.bash
```

To auto-source on every session:
```bash
# Optional: auto-source the workspace in every terminal
echo "source ~/autonomous-navigation-robot/devel/setup.bash" >> ~/.bashrc
```

---

## Running the Project

### Launch Gazebo
```bash
source devel/setup.bash
roslaunch custom_gazebo_world custom_world.launch
```

### Launch RViz Navigation
```bash
source devel/setup.bash
roslaunch path_planning turtlebot3_custom_world.launch
```

### Cleaning up Gazebo processes
```bash
rosnode kill /gazebo /gazebo_gui 2>/dev/null || true
killall -9 gzserver gzclient 2>/dev/null || true
source devel/setup.bash
```

---

## Repository Structure
```
autonomous-navigation-robot/
├── src/
│   ├── path_planning/        # A* pathfinding package
│   ├── custom_gazebo_world/  # Custom maze environment
│   └── turtlebot3_karto/     # SLAM map files
├── .gitignore
└── README.md
```
> `build/` and `devel/` are excluded via `.gitignore` — auto-generated after running `catkin_make`

---

## Future Improvements
- Optimise pathfinding efficiency for dynamic obstacle avoidance
- Transition navigation stack to ROS2
- Test on physical TurtleBot3 hardware

# Lab 07: Introduction to ROS 2 – Publishers and Subscribers
**Course**: MXET 400 – Mechatronics II: Industrial Robotic Systems  
**Department**: Multidisciplinary Engineering Technology, Texas A&M University  

---

## 1. Overview & Objectives

In this lab, you will learn the fundamental publish-subscribe communication architecture in ROS 2:
1. **Understand Nodes & Topics**: How independent processes (nodes) communicate asynchronously using strongly typed messages over named buses (topics).
2. **Build a Custom Package**: Compile and link a Python ROS 2 package (`my_first_robot_pkg`) using `colcon`.
3. **Publish & Subscribe Standard Messages**: Implement string publishers and listeners (`std_msgs/msg/String`).
4. **Publish & Subscribe Multi-Dimensional Messages**: Implement custom math nodes that broadcast and process 3D dimension vectors (`geometry_msgs/msg/Vector3`) to compute physical box volume in real time.

---

## 2. Package Structure

```text
lab07/
├── README.md                          # This lab guide & command reference
├── starter_code/                      # Reference snippets from lab handout
│   ├── Talker.txt                     # Bare publisher template
│   └── Listener.txt                   # Bare subscriber template
└── my_first_robot_pkg/                # ROS 2 Python package
    ├── package.xml                    # Package manifest & dependencies
    ├── setup.py                       # Python build configuration & console entry points
    ├── setup.cfg                      # Installation paths
    └── my_first_robot_pkg/
        ├── __init__.py
        ├── talker.py                  # Task 2: String talker node
        ├── listener.py                # Task 2: String listener node
        ├── numbers.py                 # Task 3: Vector3 coordinate publisher
        └── volume.py                  # Task 3: Vector3 volume subscriber & calculator
```

---

## 3. Getting Started & Workspace Build

Ensure you are in the root directory of your ROS 2 workspace before building:

```bash
# 1. Navigate to your workspace root
cd ~/ros2_ws

# 2. Build the lab07 package
colcon build --symlink-install --packages-select my_first_robot_pkg

# 3. Source the workspace setup script
source install/setup.bash
```

> [!TIP]
> **Pro-Tip**: If you added the `sros` alias to your `~/.bashrc` as recommended in class, you can simply type `sros` instead of `source install/setup.bash` every time you open a new terminal.

---

## 4. Lab Tasks & Execution Commands

### Task 1: Package Creation & Structure Review
The package `my_first_robot_pkg` is configured with dependencies on `rclpy`, `std_msgs`, and `geometry_msgs`. Review `package.xml` and `setup.py` to see how console executables are registered under `entry_points`.

---

### Task 2: Basic Publisher and Subscriber (String)

In this task, the **talker** node publishes incremental string messages `"Hello World: X"` to the topic `/topic`, and the **listener** node receives and logs them.

#### Terminal 1 (Run Talker):
```bash
source ~/ros2_ws/install/setup.bash
ros2 run my_first_robot_pkg talker
```

#### Terminal 2 (Run Listener):
```bash
source ~/ros2_ws/install/setup.bash
ros2 run my_first_robot_pkg listener
```

#### Terminal 3 (Inspect Topic):
```bash
# List all active topics
ros2 topic list

# Print message data in real-time
ros2 topic echo /topic

# Check publishing rate (should be ~2.0 Hz / 0.5s period)
ros2 topic hz /topic
```

---

### Task 3: Multi-Variable Publishing & Math Computation (Vector3 & Volume)

In this task, you will modify `numbers.py` and `volume.py` to publish and process 3D dimensions:
* **`numbers.py`**: Publishes a `geometry_msgs/msg/Vector3` containing `x` (length), `y` (width), and `z` (height). On each timer tick (0.5s), the values increment by:
  * $x = x + 1.25$
  * $y = y + 1.50$
  * $z = z + 1.75$
* **`volume.py`**: Subscribes to the dimension topic, computes the 3D volume ($V = x \times y \times z$), and logs both the dimensions and the resulting volume.

#### Terminal 1 (Run Numbers Node):
```bash
source ~/ros2_ws/install/setup.bash
ros2 run my_first_robot_pkg numbers
```

#### Terminal 2 (Run Volume Node):
```bash
source ~/ros2_ws/install/setup.bash
ros2 run my_first_robot_pkg volume
```

#### Expected Terminal Output:
```text
[INFO] [volume]: I heard: "x: 1.25, y: 1.50, z: 1.75" (Volume: 3.28)
[INFO] [volume]: I heard: "x: 2.50, y: 3.00, z: 3.50" (Volume: 26.25)
[INFO] [volume]: I heard: "x: 3.75, y: 4.50, z: 5.25" (Volume: 88.59)
```

---

## 5. Lab Questions & Checkpoint Checklist

Before completing your lab report, verify the following:
* [ ] Talker and Listener communicate successfully over `/topic`.
* [ ] `ros2 topic echo /topic` displays incoming messages.
* [ ] `numbers.py` correctly increments `x`, `y`, `z` by `1.25`, `1.50`, and `1.75`.
* [ ] `volume.py` accurately computes and logs volume as $x \times y \times z$.
* [ ] Capture terminal screenshots of all four running nodes for your lab report.

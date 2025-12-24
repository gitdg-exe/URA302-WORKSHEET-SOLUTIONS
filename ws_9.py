import tkinter as tk

root = tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")

c = tk.Canvas(root, width=500, height=400, bg="white")
c.pack()

c.create_oval(98, 98, 102, 102, fill="black")

path = [(20, 50), (100, 120), (180, 90), (250, 150)]
for i in range(len(path) - 1):
    c.create_line(path[i][0], path[i][1], path[i+1][0], path[i+1][1], fill="blue", width=3)

dot = c.create_oval(10, 200, 20, 210, fill="red")
def move():
    c.move(dot, 5, 0)
    root.after(50, move)
move()

c.create_rectangle(300, 250, 360, 300, fill="gray")
c.create_oval(305, 300, 325, 320, fill="black")
c.create_oval(335, 300, 355, 320, fill="black")

robot = c.create_oval(200, 200, 220, 220, fill="green")
def up():
    c.move(robot, 0, -10)
def down():
    c.move(robot, 0, 10)
def left():
    c.move(robot, -10, 0)
def right():
    c.move(robot, 10, 0)

tk.Button(root, text="Up", command=up).place(x=420, y=50)
tk.Button(root, text="Down", command=down).place(x=420, y=80)
tk.Button(root, text="Left", command=left).place(x=380, y=80)
tk.Button(root, text="Right", command=right).place(x=460, y=80)

ball = c.create_oval(200, 150, 230, 180, fill="blue")
dx, dy = 3, 3
def bounce():
    global dx, dy
    c.move(ball, dx, dy)
    x1, y1, x2, y2 = c.coords(ball)
    if x1 <= 0 or x2 >= 500:
        dx = -dx
    if y1 <= 0 or y2 >= 400:
        dy = -dy
    root.after(30, bounce)
bounce()

line_robot = c.create_oval(50, 200, 70, 220, fill="red")
def straight():
    c.move(line_robot, 2, 0)
    root.after(40, straight)
straight()

A = (150, 300)
D = (400, 300)
c.create_line(A[0], A[1], D[0], D[1], width=3)
c.create_line(A[0], A[1], A[0], 270, fill="red")
c.create_line(A[0], 270, 270, 270, fill="green")
c.create_line(270, 270, 270, 300, fill="blue")

path_robot = c.create_oval(100, 100, 120, 120, fill="purple")
trail = []
prev_pos = c.coords(path_robot)

def key(e):
    global prev_pos
    dx, dy = 0, 0
    if e.keysym == "Up":
        dy = -5
    if e.keysym == "Down":
        dy = 5
    if e.keysym == "Left":
        dx = -5
    if e.keysym == "Right":
        dx = 5

    c.move(path_robot, dx, dy)
    new_pos = c.coords(path_robot)

    line = c.create_line(
        (prev_pos[0] + prev_pos[2]) / 2,
        (prev_pos[1] + prev_pos[3]) / 2,
        (new_pos[0] + new_pos[2]) / 2,
        (new_pos[1] + new_pos[3]) / 2,
        fill="black"
    )
    trail.append(line)
    prev_pos = new_pos

def reset():
    for t in trail:
        c.delete(t)
    trail.clear()

tk.Button(root, text="RESET", command=reset).place(x=420, y=120)

root.bind("<Key>", key)
root.focus_set()

root.mainloop()

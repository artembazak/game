import turtle, random





player2 = turtle.Turtle()



player1.color("green")
player1.shape("turtle")
player1.penup()
player1.goto(200, 100)
player1.pendown()
player1.circle(50)
player1.penup()
player1.goto(-200, 150)

player2.color("blue")
player2.shape("turtle")
player2.penup()
player2.goto(200, -150)
player2.pendown()
player2.circle(50)
player2.penup()
player2.goto(-200, -100)

while True:
    die = random.choice([10, 2, 3, 40, 5, 6])
    die2 = random.choice([10, 2, 3, 40, 5, 6])

    x = 0
    if player1.pos() >= (200, 150):
        break

    if player2.pos() >= (245, -145):
        break


    break

    player1.forward(1 * die)
    player2.forward(1 * die2)

    y += 1 * x
    


player1.left(90)
player1.right(90)
player1.left(90)
player1.right(90)
player1.goto(-200, 150)


player2.left(90)
player2.right(90)
player2.left(90)
player2.right(90)
player2.goto(-200, -100)

turtle.getscreen()._root.mainloop()



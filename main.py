import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
data["state"] = data["state"].str.lower()
print(len(data["state"]))

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
count = 0
guessed = []
while count<len(data["state"]):
    ans = screen.textinput(title=f"{count}/50 state's correct", prompt="What's another state's name? ").lower()
    if ans == "exit":
        break
    if ans in data["state"].tolist():
        if ans not in guessed:
            row = data[data["state"] == ans]
            x = int(row["x"])
            y = int(row["y"])
            writer.goto(x,y)
            guessed.append(ans)
            text = ans.title()
            writer.write(text,align="center",font=("Arial",10,"normal"))
            count+=1
            
state_dict = {"states":[]}
state_dict["states"] = [state for state in data["state"].tolist() if state not in guessed]
state_df = pd.DataFrame(state_dict)
state_df.to_csv("Missed_states.csv")

screen.exitonclick()







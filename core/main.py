from fastapi import FastAPI
import random


app = FastAPI()

manage_list = []


@app.post("/expends")
def Create_New_Expense(description: str ,amount: float):
    while True:
        id = random.randint(1,100)
        uniq = True
        for item in manage_list:
            if item["id"] == id:
                uniq = False
        if uniq == True:
            break

    item = {"id" : id, "description" : description, "amount" : amount}
    manage_list.append(item)
    return item
                

@app.get("/expends")
def Get_All_Expenses():
    return manage_list
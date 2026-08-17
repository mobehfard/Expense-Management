from fastapi import FastAPI,status, HTTPException
import random
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("Application startup")
    
    yield  

   
    print("Application shutdown")
   


app = FastAPI(lifespan=lifespan)

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
    raise HTTPException(status.HTTP_200_OK, detail= item)
                

@app.get("/expends")
def Get_All_Expenses():
    
    raise HTTPException(status.HTTP_200_OK, detail = manage_list)


@app.get("/expends/{id}")
def get_expend(id: int):
    for item in manage_list:
        if item["id"] == id:
            raise HTTPException(status.HTTP_200_OK, detail= item)

    raise HTTPException(status.HTTP_404_NOT_FOUND , detail="object not found")

@app.put("/expends/{id}")
def update_expend(id: int, description: str, amount: float):
    for item in manage_list:
        if item["id"] == id:
            item["description"] = description
            item["amount"] = amount
            raise HTTPException(status.HTTP_202_ACCEPTED, detail=item)
            

    raise HTTPException(status.HTTP_404_NOT_FOUND , detail="object not found")

@app.delete("/expend/{id}")
def del_expend(id: int):
    for item in manage_list:
        if item["id"] == id:
            manage_list.remove(item)
            raise HTTPException(status.HTTP_204_NO_CONTENT, detail="object removed")
                
    
    raise HTTPException(status.HTTP_404_NOT_FOUND , detail="object not found")
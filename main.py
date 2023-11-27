from fastapi import FastAPI
import mysql.connector as con

app = FastAPI()


mydb = con.connect(
    host="localhost",
    user="root",
    password="86888S#i6",
    database="krishna3"
)

cur = mydb.cursor()

@app.get("/cars")
def get_cars():
    cur.execute("SELECT * FROM cars")
    myresult = cur.fetchall()
    return {"cars": myresult}

@app.get("/cars/{id}")
def get_car(id: int):
    cur.execute(f"SELECT * FROM cars WHERE id = {id}")
    myresult = cur.fetchall()
    return {"car": myresult}

@app.post("/cars")
def create_car(manufacturer: str, modelName: str, cc:int, onRoadPrice:int, seatingCapacity:int, gearBox:int, fuelType:str):
    sql = f"INSERT INTO cars (manufacturer, modelName, cc, onRoadPrice, seatingCapacity, gearBox, fuelType) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (manufacturer, modelName, cc, onRoadPrice, seatingCapacity, gearBox, fuelType)
    cur.execute(sql, val)
    mydb.commit()
    return {"message": "Car created Successfully"}

@app.put("/cars/{id}")
def update_car(id: int, manufacturer: str, modelName: str, cc:int, onRoadPrice:int, seatingCapacity:int, gearBox:int, fuelType:str):
    sql = f"UPDATE cars SET manufacturer = %s, modelName = %s, cc = %s, onRoadPrice = %s, seatingCapacity = %s, gearBox = %s, fuelType = %s WHERE id = {id}"
    val = (manufacturer, modelName, cc, onRoadPrice, seatingCapacity, gearBox, fuelType)
    cur.execute(sql, val)
    mydb.commit()
    return {"message": "Car updated Successfully"}

@app.delete("/cars/{id}")
def delete_car(id: int):
    sql = f"DELETE FROM cars WHERE id = {id}"
    cur.execute(sql)
    mydb.commit()
    return {"message": "Car deleted Successfully"}
![](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

# Agile-APIs-Getting-Started-with-PyMongo

## Introduction

Welcome back, Trainers! Now that you've successfully built your Pokémon API, it's time to push it even further. The Pokémon world is vast, and there's still so much more to explore! In this set of exercises, you’ll be extending your existing Pokémon API, adding new features like assigning Pokémon to your team, evolving them, managing battles, and more.

You'll also implement new validation rules and error handling to ensure your API is robust and user-friendly. Get ready to level up your coding skills!


<div align="center"> <img src="https://github.com/user-attachments/assets/c8ec83d3-97e2-4d80-8c3b-7f1ad58e8569" height="450" width="800"> </div>


## Requirements

- Ensure your existing Pokémon API is up and running.
  
- [Learn how to fork this repo](https://guides.github.com/activities/forking/)

- Clone this repo into your code/labs folder

- Use Postman to test and interact with the API endpoints.



## PokeIteration 0: Structuring the Project with the Model-View-Controller (MVC) Pattern

Before diving into coding, it's essential to ensure your project is structured following the MVC pattern to maintain scalability and organization.

1. Create the directory structure for your project following the Model-View-Controller (MVC) architecture.

```bash
/pokemon_api
├── /app
│   ├── /models        # Database models
│   ├── /controllers   # Business logic
│   ├── /routes        # API endpoints
│   ├── /schemas       # Pydantic schemas for data validation
│   ├── /connection    # connection with database
│   └── main.py        # Application entry point
└── README.md          # Project documentation
```

- Models: These define the structure of the data stored in the database. For example, your Pokémon, Trainers, Moves, and Abilities are all models.
  
- Views: In this context, the "views" are the routes that handle incoming HTTP requests (like GET, POST).
  
- Controllers: These contain the business logic that connects the models and routes. They handle operations like adding Pokémon to a team or battling.
  
- Schemas: Using Pydantic, these schemas ensure that incoming and outgoing data conforms to the correct type and format, matching the structure of the database. This guarantees that only valid data is processed by the API.

> ⚠️ **WARNING:** The use of Pydantic schemas is crucial to ensure that all data sent to the API is correctly validated. The schemas match the structure of the data stored in the database, ensuring typographical security and consistency.Any enpoint that requires a schema and does not have one will not be counted as valid. 

### Example TrainerSchema

```python
class TrainerSchema(BaseModel):
    trainer_id: int
    name: str
    team: List[int]  # List of Pokémon IDs in the team
    storage: List[int]  # List of Pokémon IDs in storage

    class Config:
        orm_mode = True
```
<div align="center"> <img src="https://github.com/user-attachments/assets/0ac8b4b1-0a4c-472a-af4d-24277331c0d9" height="300" width="600"> </div>


## **PokeIteration 1: Create Trainers for Battles**

In this exercise, you will create Trainers that will be used for Pokémon battles. We will implement an endpoint to **create a Trainers** for either the player.

### **Tasks:**
- Create an endpoint to **create a new Trainers**.

### **Example Postman Request:**
- `POST /Trainers/create`

### **Response:**
- `"Team 'Ash's' has been successfully created."`

## PokeIteration 2: Add Pokémon to a Team

<img src="https://github.com/user-attachments/assets/cf153b5c-045f-48a0-9b92-3c13b8138377" height="600" width="400" align="right">

Now that you've created a Trainers for the trainer, you need to **add Pokémon** to that team.

### **Tasks:**

- Create an endpoint to **add a Pokémon to an existing team**.
- The Pokémon must come from the existing Pokémon collection in the database.
- Each team should only allow a maximum of 6 Pokémon.

### **Validations:**
- Ensure no duplicates: a Pokémon can’t be added twice to the same team.
- Validate that the team does not exceed 6 Pokémon. If it does, return an error.

### **Error Handling:**
- If the team is full, return a **400 Bad Request** error with the message: `"Your team is already full with 6 Pokémon!"`.
- If the Pokémon is already in the team, return a **409 Conflict** error with the message: `"This Pokémon is already in your team!"`.

### **Example Postman Request:**
- `POST /team/{team_id}/add-pokemon`
  
```json
{
  "id": ObjectId("671622cc16572cf5a1b13926")
}
```

### **Response:**
- `"Pikachu has been successfully added to the 'Ash's Team'."`


## PokeIteration 3: **Release a Pokémon from the Team**

In this exercise, you will create an endpoint that allows you to either release a Pokémon from your team. Releasing means letting go of the Pokémon

### Validation:
- Ensure that the team has a Pokémon before attempting to release it.
  
- Validate that the specified Pokémon ID belongs to the trainer’s team.

  
### Error Handling:
- If you try to release a Pokémon when the team is empty, return an error: "The team is currently empty. You cannot release any Pokémon."
  
- Invalid Pokémon ID: If the Pokémon ID does not exist in the team, return a 404 Not Found: "Pokémon with ID {pokemon_id} not found in your team."

### Endpoint Structure:

- DELETE /team/{pokemon_id}/release: Release the Pokémon, permanently deleting it.

<div align="center"> <img src="https://github.com/user-attachments/assets/bd8aa548-8294-4ff9-80a2-596f412a7628" height="300" width="600"> </div>

## PokeIteration 4: Filter and Sort Pokémons

### **Tasks:**

Create an endpoint that allows trainers to filter pokemon by initial letter, group them by type, and sort them by their base_stats_hp using  aggregate pipelines.

You’ll use multiple stages like $match, $group, $sort, and $project to build this pipeline and manipulate the data.


## PokeIteration 5: View Pokémon Team with Moves and Type

It's time to bring all the data together! In this exercise, you will create an endpoint that retrieves a Pokémon's to your team full details, including its abilities, moves, and types.

### Tasks:

- Create an endpoint to view a specific Pokémon with all its relevant details: 
Abilities (retrieved from the abilities collection).
Moves (retrieved from the moves collection).
Type (retrieved from the pokemon_types collection).

### Validations:
- Ensure the Pokémon exists in the Team.
- Return a 404 Not Found if the Pokémon doesn’t exist.
  
### Error Handling:
- If the Pokémon does not exist, return an error message: "Pokémon not found!".
  
### Example Postman Request:
GET /pokemon/{pokemon_id}/details

<div align="center"> <img src="https://github.com/user-attachments/assets/35406ace-c625-40ed-9c02-b011b5b9f218" height="300" width="600"> </div>

## PokeIteration 6: **Deploy the Pokémon API with Uvicorn**



---


## IABonus : Explore and Implement a Hugging Face Model with FastAPI

In this exercise, you’ll explore Hugging Face’s Model Hub to select and implement a different NLP model in a FastAPI application. The goal is to integrate a model that performs a specific task, such as text translation, summarization, or sentiment analysis.

- Visit Hugging Face Model Hub.
- Filter for NLP models and choose one that interests you (e.g., for translation, text summarization, sentiment analysis).
- Review the model documentation to understand how it works and the data it processes.

<div align="center"> <img src="https://github.com/user-attachments/assets/8833c6b7-f055-4ccb-b1db-76cab8fccda1" height="300" width="650"> </div>

## PokeBonus 1: Battle a Random Wild Pokémon

In this exercise, you'll create an endpoint that selects a Pokémon from a specific trainer's team based on its position in the team, and makes it battle a random wild Pokémon encountered in the tall grass.


### Steps

The endpoint will receive:

- The trainer's ID.
- The position of the Pokémon in the trainer’s team (0-indexed).

Battle logic:

The battle will follow a simple structure based on the Pokémon's stats:

- The Pokémon with the higher speed will attack first.
- The damage will be calculated based on the attacker's attack stat and the defender's defense stat.
- The Pokémon that reaches 0 HP first loses.

Response format:

The response should include the details of the battle result:

- The trainer's Pokémon (name, stats).
- The wild Pokémon (name, stats).
- The winner of the battle.

### Validations

- Ensure the trainer exists and has a Pokémon in the specified position.
- If the position is invalid (i.e., no Pokémon in that position), return an error.
  
### Error Handling

- If the trainer does not exist, return a 404 Not Found error: "Trainer not found.".
- If the position is invalid, return a 400 Bad Request: "Invalid Pokémon position.".
- If there are no Pokémon in the wild database, return a 500 Internal Server Error.

### Response :
```json
{
  "trainer_pokemon": {
    "name": "Pikachu",
    "hp": 35,
    "attack": 55,
    "defense": 40,
    "speed": 90
  },
  "wild_pokemon": {
    "name": "Zubat",
    "hp": 40,
    "attack": 45,
    "defense": 35,
    "speed": 55
  },
  "battle_result": {
    "winner": "trainer_pokemon",
    "loser": "wild_pokemon",
    "details": "Pikachu attacked first with higher speed, dealt 15 damage, and won the battle."
  }
}
```



## PokeBonus2: Level Up

Now that your Pokémon has won a battle, it’s time to take the next step—evolve your Pokémon! In this exercise, you'll extend the functionality from the previous exercise to evolve the winning Pokémon (if it meets the criteria) and update the trainer's team with the evolved form.

Steps:
1. Check the Pokémon evolve:
   
- After a successful battle, check if the Pokémon has an evolution available by looking up the evolves_to field.

  
2. Retrieve the evolved Pokémon:
- Use the evolves_to field from the current Pokémon to find its next evolutionary form.
- Fetch the new Pokémon data from the pokemon collection based on its ID (evolves_to).

3. Update the team:
- Use the previously implemented endpoint to remove the old Pokémon from the team.
- Then, add the evolved Pokémon to the team, replacing the old form.
  
4. Response format:
   
The response should confirm the successful evolution, showing both the old Pokémon and the new evolved form.


```json
{
  "trainer_pokemon": {
    "name": "Bulbasaur",
    "hp": 45,
    "attack": 49,
    "defense": 49,
    "speed": 45,
    "special_attack": 65,
    "special_defense": 65
  },
  "evolved_pokemon": {
    "name": "Ivysaur",
    "hp": 60,
    "attack": 62,
    "defense": 63,
    "speed": 60,
    "special_attack": 80,
    "special_defense": 80
  },
  "message": "Bulbasaur has evolved into Ivysaur and replaced in the team."
}
```
<div align="center"> <img src="https://github.com/user-attachments/assets/94dd3642-d435-4f36-a0c9-6d29737fd992" height="300" width="600"> </div>

## Submission

Upon completion, run the following commands:
```
$ git add .
$ git commit -m "done"
$ git push origin main
```

Then create a Pull Request!!

![happy_coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)

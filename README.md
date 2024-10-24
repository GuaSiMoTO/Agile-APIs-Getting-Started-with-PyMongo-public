# Agile-APIs-Getting-Started-with-PyMongo

# Extending the Pokémon API

## Introduction

Welcome back, Trainers! Now that you've successfully built your Pokémon API, it's time to push it even further. The Pokémon world is vast, and there's still so much more to explore! In this set of exercises, you’ll be extending your existing Pokémon API, adding new features like assigning Pokémon to your team, evolving them, managing battles, and more.

You'll also implement new validation rules and error handling to ensure your API is robust and user-friendly. Get ready to level up your coding skills!

Requirements

- Ensure your existing Pokémon API is up and running.

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
│   └── main.py        # Application entry point
└── README.md          # Project documentation
```

- Models: These define the structure of the data stored in the database. For example, your Pokémon, Trainers, Moves, and Abilities are all models.
  
- Views: In this context, the "views" are the routes that handle incoming HTTP requests (like GET, POST).
  
- Controllers: These contain the business logic that connects the models and routes. They handle operations like adding Pokémon to a team or battling.


## **PokeIteration 1: Create Teams for Battles**

In this exercise, you will create teams that will be used for Pokémon battles. We will implement an endpoint to **create a team** for either the player or the enemy.

### **Tasks:**
- Create an endpoint to **create a new team**.
- Each team can either be for the player or for the enemy.
- Ensure that each trainer (player or enemy) can only have one active team at a time.

### **Validations:**
- Ensure that a team can only be created if the trainer (player or enemy) does not already have an active team.

### **Error Handling:**
- If the trainer already has an active team, return a **409 Conflict** error with the message: `"Trainer {trainer_id} already has an active team!"`.

### **Example Postman Request:**
- `POST /team/create`

### **Response:**
- `"Team 'Ash's Team' has been successfully created."`



## **Exercise 2: Add Pokémon to a Team**

Now that you've created a team for the trainer, you need to **add Pokémon** to that team.

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



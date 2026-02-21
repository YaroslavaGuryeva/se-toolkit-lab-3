# Questionnaire — API Exploration

Fill in each answer below. Replace `___` with the correct value.

## Items endpoints

### GET /items

1. HTTP method: GET
2. Path: /items
3. Status code (success): 200
4. Response type (array or object): array

### GET /items/{item_id}

1. Status code (item found): 200
2. Status code (item not found): 404

### POST /items

1. HTTP method: POST
2. Status code (created successfully): 201

### PUT /items/{item_id}

1. HTTP method: PUT
2. Status code (updated successfully): 200

## Authentication

1. What happens when you call an endpoint without the API key? (status code): 401
2. Where do you set the API key value for Docker Compose? (file name): .env.docker.secret

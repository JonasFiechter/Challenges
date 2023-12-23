'''
Challenge: Task Management API

Imagine you're building a task management API that allows users to create, 
retrieve, update, and delete tasks. Each task should have the following 
attributes:

    Task ID (auto-generated)
    Title
    Description
    Due Date
    Status (e.g., "To Do," "In Progress," "Done")

Your goal is to implement a RESTful API with the following endpoints:

    Create a Task:
        Method: POST
        Endpoint: /tasks
        Request Body: JSON with title, description, and due date.
        Response: JSON with the created task, including the auto-generated 
        task ID.

    Get All Tasks:
        Method: GET
        Endpoint: /tasks
        Response: JSON array containing all tasks.

    Get a Task by ID:
        Method: GET
        Endpoint: /tasks/{task_id}
        Response: JSON with the task details.

    Update a Task:
        Method: PUT
        Endpoint: /tasks/{task_id}
        Request Body: JSON with the updated title, description, due date, and 
        status.
        Response: JSON with the updated task details.

    Delete a Task:
        Method: DELETE
        Endpoint: /tasks/{task_id}
        Response: JSON with a message indicating the success of the deletion.

For bonus points:

    Implement validation for input data (e.g., ensure due dates are in the 
    future).
    Add pagination to the endpoint that retrieves all tasks.
    Implement sorting and filtering options for the endpoint that retrieves all 
    tasks.

You can implement this challenge using any web framework you're comfortable with 
(e.g., Flask, Django, FastAPI). Additionally, consider how you would handle data 
storage. You could use an in-memory data structure, a relational database, or 
any other suitable storage solution.

This challenge allows you to showcase your ability to design a RESTful API, 
handle CRUD operations, perform input validation, and consider additional 
features for a real-world task management system.
'''

def main():
    ...
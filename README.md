# Hexagonal-Architecture

tscheduler is a simple app to demonstrate how to implement Hexagonal Architecture in Python.

The app allow user to:
- Create a Task
- Read a Task
- Execute a Task

This code was created for demonstration purpose when creating [this article in Workflows Guru](https://www.workflows.guru/resources/hexagonal-architecture-implemented-in-python).

## Run the application

You can run the Hexa application from the configurator or you can set up a FastApi application.

If you want to test using Fastapi, please install dependencies using this command:
```
python -m venv venv

fastapi[standard]
```

and run the application using 

```
fastapi dev
```

This will expose the openapi doc in http://127.0.0.1:8000/docs

## Adapters

Adapters are external components, they communicates with our app via the ports

## Domain

Contain the app business logic

## Ports

The ports contains the interfaces (A contract that we should implement)


## Tests

To run the tests just run:

```
pytest
```

When we push to main branch two github workflows will be executed, one to test the task creation and one to test
if we correctly implemented the Hexagonal Architecture using fitness functions.

### Unit Tests: test_create_task

Contains a test example to show how easy to test an Hexagonal Application. You only need an
implementation of your ports to be able to run the tests. The core business logic is independent of external dependencies.

### Fitness Functions: test_check_architecture

Contains some example of fitness functions that should verify that we don't break our Architecture. 
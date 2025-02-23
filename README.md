# Hexagonal-Architecture

tscheduler is a simple app to show how we implement Hexagonal Architecture in Python.
The app allow to:
- Create a Task
- Read a Task
- Execute a Task

This code was created for demonstration purpose when creating [this article in Workflows Guru](workflows.guru/resources/hexagonal-architecture-implemented-in-python).

## Adapters

Adapters are external components, they communicates with our app via the ports

## Domain

Contain the app business logic

## Ports

The ports contains the interfaces (A contract that we should implement)


## Tests


### Unit Tests: test_create_task

Contains a test example to show how easy to test an Hexagonal Application. You only need an
implementation of your ports to be able to run the tests. The core business logic is independent of external dependencies.

### Fitness Functions: test_check_architecture

Contains some example of fitness functions that should verify that we don't break our Architecture. 
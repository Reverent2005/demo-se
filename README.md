# To-Do List CLI Application

This is a simple command-line interface (CLI) application that allows users to manage their tasks effectively. Users can add, remove, and list tasks in a straightforward manner.

## Features

- **Add Task**: Allows users to add a new task to their to-do list.
- **Remove Task**: Enables users to remove a task from their list.
- **List Tasks**: Displays all the tasks currently in the to-do list.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the `demo-se` directory:
   ```
   cd demo-se
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/todo.py
```

Follow the on-screen instructions to manage your tasks.

## Testing

To run the tests for the To-Do List application, navigate to the `tests` directory and execute:
```
pytest test_todo.py
```

## Docker

To build the Docker image for this application, use the following command:
```
docker build -t <your-dockerhub-username>/demo-se .
```

To run the Docker container:
```
docker run -it <your-dockerhub-username>/demo-se
```

## License

This project is licensed under the MIT License.
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';


function App() {
  const [tasks, setTasks] = useState([]);
  const [newTaskTitle, setNewTaskTitle] = useState('');
  const [newTaskDueDate, setNewTaskDueDate] = useState('');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/tasks');
      setTasks(response.data.tasks);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  const addTask = async () => {
    try {
      await axios.post('http://127.0.0.1:5000/tasks', {
        title: newTaskTitle,
        due_date: newTaskDueDate,
      });
      fetchTasks(); // Refresh the task list after adding a task
      setNewTaskTitle('');
      setNewTaskDueDate('');
    } catch (error) {
      console.error('Error adding task:', error);
    }
  };

  return (
    <div className="App" style={{ padding: '20px' }}>
      <h1>Task App</h1>
      <section>
        <h2>Add New Task</h2>
        <div>
          <label htmlFor="newTaskTitle">Task Title:</label>
          <input
            type="text"
            id="newTaskTitle"
            value={newTaskTitle}
            onChange={(e) => setNewTaskTitle(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="newTaskDueDate">Due Date:</label>
          <input
            type="date"
            id="newTaskDueDate"
            value={newTaskDueDate}
            onChange={(e) => setNewTaskDueDate(e.target.value)}
          />
        </div>
        <div>
          <button onClick={addTask}>Add Task</button>
        </div>
      </section>

      <section>
        <h2>Task List</h2>
        <div>
          {tasks.map((task) => (
            <div key={task.id} style={{ marginBottom: '10px' }}>
              <p>
                <strong>{task.title}</strong>
              </p>
              <p>Due Date: {task.due_date || 'Not specified'}</p>
              <p>Status: {task.completed ? 'Completed' : 'Incomplete'}</p>
              <hr />
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default App;

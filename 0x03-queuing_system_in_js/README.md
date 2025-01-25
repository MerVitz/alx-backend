# **Queuing System in JavaScript**  

Welcome to the **Queuing System in JavaScript** project! This project provides a comprehensive exploration of queue processing using **Kue**, data persistence with **Redis**, and web API development with **Express.js**. The goal is to build a scalable, efficient system for handling background jobs such as notifications, stock management, and seat reservations.  

## **Table of Contents**  

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Project Structure](#project-structure)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Testing](#testing)  
- [Best Practices](#best-practices)  
- [Contributing](#contributing)  
- [License](#license)  

---

## **Project Overview**  

This project simulates a queue management system by integrating **Kue** for job scheduling, **Redis** for fast in-memory storage, and **Express.js** for serving web APIs. The system is designed to handle multiple operations such as:  

- Sending push notifications asynchronously.  
- Managing product stock availability and reservations.  
- Implementing seat reservation logic for events.  

The queuing system ensures **high performance**, **scalability**, and **asynchronous processing**, making it ideal for large-scale applications.  

---

## **Features**  

1. **Job Queueing System:**  
   - Efficiently queue and process background tasks with Kue.  
   - Handle job creation, completion, failures, and progress tracking.  

2. **Stock Management:**  
   - Keep track of product inventory using Redis.  
   - Provide API endpoints to check and reserve products.  

3. **Seat Reservation System:**  
   - Real-time seat tracking with reservation limits.  
   - Automatic seat availability updates with Redis.  

4. **Robust API Design:**  
   - RESTful API design principles implemented using Express.js.  
   - JSON responses for easy client-side consumption.  

5. **Asynchronous Operations:**  
   - Ensure non-blocking operations with async/await and Redis Promises.  

6. **Unit Testing:**  
   - Comprehensive test coverage using Mocha and Chai.  
   - Mocking Kue queue processing for isolated testing.  

---

## **Technologies Used**  

- **JavaScript (ES6+):** Core programming language for implementation.  
- **Node.js:** Runtime environment for executing JavaScript server-side.  
- **Express.js:** Web framework for building API endpoints.  
- **Kue:** Job queue management library for processing tasks asynchronously.  
- **Redis:** In-memory data store for fast access and persistence.  
- **Mocha & Chai:** Testing framework for unit tests.  
- **Babel:** Transpiler for using modern JavaScript features.  
- **Nodemon:** Automatically restarting the server during development.  

---

## **Installation**  

Follow these steps to set up the project locally:  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/alx-backend.git
   cd alx-backend/0x03-queuing_system_in_js
   ```

2. **Install dependencies:**  
   ```bash
   npm install
   ```

3. **Start Redis server (ensure Redis is installed):**  
   ```bash
   redis-server
   ```

4. **Run the development server:**  
   ```bash
   npm run dev 9-stock.js
   ```

---

## **Project Structure**  

```
0x03-queuing_system_in_js/
│-- 8-job.js             # Job creation function  
│-- 8-job.test.js        # Unit tests for job creation  
│-- 9-stock.js           # Stock management system  
│-- 100-seat.js          # Seat reservation system  
│-- package.json         # Dependencies and scripts  
│-- README.md            # Project documentation  
│-- __tests__/           # Test cases  
│-- node_modules/        # Installed dependencies  
└-- .babelrc             # Babel configuration  
```

---

## **Usage**  

### **1. Push Notification Jobs**  
To create notification jobs in the queue:  

```javascript
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const jobs = [{ phoneNumber: '1234567890', message: 'Welcome to our service!' }];

createPushNotificationsJobs(jobs, queue);
```

---

### **2. Stock Management API**  

Start the stock management server:  

```bash
npm run dev 9-stock.js
```

Available endpoints:  

- **GET /list_products** – Returns all products.  
- **GET /list_products/:itemId** – Returns a specific product.  
- **GET /reserve_product/:itemId** – Reserves an item if available.  

Example:  
```bash
curl localhost:1245/list_products
```

---

### **3. Seat Reservation System**  

Start the seat reservation server:  

```bash
npm run dev 100-seat.js
```

Available endpoints:  

- **GET /available_seats** – Returns available seats.  
- **GET /reserve_seat** – Reserves a seat if available.  
- **GET /process** – Processes seat reservations from the queue.  

Example:  
```bash
curl localhost:1245/reserve_seat
```

---

## **API Endpoints**  

| Method | Endpoint               | Description                           | Example                           |
|--------|------------------------|---------------------------------------|-----------------------------------|
| GET    | /list_products           | Get list of all products              | `curl localhost:1245/list_products` |
| GET    | /list_products/:itemId    | Get details of a specific product     | `curl localhost:1245/list_products/1` |
| GET    | /reserve_product/:itemId  | Reserve a product                     | `curl localhost:1245/reserve_product/2` |
| GET    | /available_seats          | Get the number of available seats     | `curl localhost:1245/available_seats` |
| GET    | /reserve_seat             | Reserve a seat                        | `curl localhost:1245/reserve_seat` |
| GET    | /process                  | Process seat reservations             | `curl localhost:1245/process` |

---

## **Testing**  

Run unit tests to ensure functionality:  

```bash
npm test
```

Example output:  
```
  createPushNotificationsJobs
    ✓ display an error message if jobs is not an array
    ✓ create two new jobs to the queue

  2 passing (50ms)
```

---

## **Best Practices**  

- Follow **RESTful API design** for clean and intuitive endpoints.  
- Use **async/await** with Redis operations to handle asynchronous flows efficiently.  
- Implement **graceful error handling** for better debugging and user experience.  
- Optimize job queue processing to prevent bottlenecks.  
- Write comprehensive unit tests to ensure reliability and prevent regressions.  

---

## **Contributing**  

Contributions are welcome! Follow these steps to contribute:  

1. Fork the repository.  
2. Create a new feature branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Commit changes and push to your fork.  
4. Open a pull request for review.  

---

## **License**  

This project is licensed under the **MIT License** – you are free to modify and distribute it as per the terms of the license.  

---

🎉 **Thank you for checking out this project! Happy coding!** 🎉  

---

Let me know if you need any changes or additions to the README!

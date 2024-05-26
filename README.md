# Community Exchange Platform

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Video Demo 🎥

[![Watch the video](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

Community Exchange Platform is a console-based application designed to facilitate the exchange of items, services, and skills within a community. Members can publish offers, search for offers, and communicate with each other to arrange exchanges. The platform supports different roles including User, Admin, Contributor, and Partner, each with specific functionalities. The application uses SQLite3 for persistent data storage. 🗄️

## Object-Oriented Programming (OOP) Principles 🧱

This project makes extensive use of `Object-Oriented Programming (OOP)` principles, especially `inheritance`, to promote a clean and maintainable codebase. Here’s how:

### Inheritance 📚

- **`Person` Class**: Serves as the base class for all person types involved in the platform, encapsulating common attributes and methods such as name, username, and password management.
- **Derived Classes**: Classes like `User`, `Admin`, `Contributor`, and `Partner` inherit from the `Person` class. Each subclass extends the base functionality to include role-specific features:
  - **`User`**: Methods for publishing and viewing offers, and managing exchange requests.
  - **`Admin`**: Capabilities to manage users and offers, including deletion and moderation.
  - **`Contributor` and `Partner`**: Specialized functions that enhance community engagement and support.

This approach not only ensures that common functionalities are centralized, reducing redundancy and increasing efficiency, but also simplifies the addition of new features and maintenance of existing ones.

## Features 🌟

### User Role 👤

- **Publish Offers** : Users can create and publish offers for items, services, or skills they want to exchange.
- **View Offers** : Users can browse offers published by other members of the community.
- **Send Exchange Requests** : Users can send requests to exchange items, services, or skills with other users.
- **Accept Exchange Requests** : Users can accept incoming requests from other users.

### Admin Role 👮

- **View Users** : Admins can view all registered users along with their roles.
- **Delete Users** : Admins can delete users from the platform.
- **View Offers** : Admins can view all offers published by users.
- **Delete Offers** : Admins can delete offers that do not comply with community guidelines.

### Contributor Role 📝

- **Publish Materials** : Contributors can publish interesting and helpful materials related to exchanging items, services, or skills.
- **Comment on Offers** : Contributors can comment on offers published by users.
- **Rate Offers** : Contributors can rate offers to help other users make informed decisions.

### Partner Role 🤝

- **Provide Support** : Partners can offer discounts or bonuses to new community members to encourage participation.

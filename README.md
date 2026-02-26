# SavoryShare – Recipe Sharing Platform

SavoryShare is a Django-based recipe sharing web application that allows users to share, discover, favorite, and purchase premium recipes. The system includes an admin approval workflow to ensure high-quality content and a secure payment system for locked recipes.


## Features
- User Registration & Login  
- Recipe Submission & Approval  
- Search Functionality  
- Favorites System  
- Premium Locked Recipes  
- Secure Payment System  
- Admin Dashboard  
- Image Upload  
- Profile Management  

---

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite (development)
- **Version Control:** Git & GitHub

---

## Graphical User Interface (GUI)

The graphical user interface of SavoryShare is designed to be clean, modern, and user-friendly. It allows smooth navigation for both users and administrators.

---

## Home Page

- Sign Up button for new users
- Login button for existing users
- Simple and welcoming layout

---

## Sign Up Page

Users can register securely by providing:
- Email
- Username
- Password

Features:
- Secure authentication
- Email verification support

---

##  Login Page

- Secure login using email and password
- Redirects to dashboard after successful login

---

## Categories / Dashboard Page

After login, users can:

- Browse recipes by category (Dessert, Dinner, etc.)
- Use the search bar to find recipes
- Add a new recipe
- View collection (Approved, Pending, Rejected)
- Access Favorites section

---

## 🍽 Recipes Page

- Displays recipe image, title, and description
- Shows premium lock icon for paid recipes
- Heart icon to favorite recipes

Premium recipes:
- Require payment to unlock
- Show confirmation message after payment
- “Go to Recipe” button appears after successful payment

---

## Favorites Page

- Users can save recipes by clicking the heart icon
- Saved recipes appear in Favorites section
- Makes it easy to access loved recipes later

---

##  Add Recipe Page

Users can submit recipes including:
- Title
- Ingredients
- Instructions
- Servings
- Cook time
- Category
- Image upload
- Option to mark recipe as Premium (Locked)

After submission:
- Recipe status becomes Pending
- Admin reviews and approves or rejects

Rejected recipes:
- Display rejection reason
- Can be edited and resubmitted

---

## Edit Recipe Page

Users can:
- Update recipe details
- Modify ingredients or instructions
- Re-upload images
- Resubmit for approval

---

## Admin Dashboard

Admin can:
- Approve or reject recipes
- Provide rejection reasons
- Manage users
- Manage categories
- Monitor platform activity

---

##  Premium Recipe Workflow

1. User selects locked recipe
2. Payment page appears
3. User enters payment details
4. Confirmation message appears
5. Recipe unlocks successfully

---

##  Database Entities

The system includes:

- Users
- Admin
- Recipe
- Comment
- Favorite
- Payment
- Collection

All tables are linked using primary and foreign keys.

---

##  Technologies Used

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: MySQL / SQLite
- Authentication: Django Auth System
- Payment Integration
- Cloud Hosting Support (AWS / Azure)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Mawela-Mpho-Precious/Recipe-Sharing-Platform.git
cd Recipe-Sharing-Platform

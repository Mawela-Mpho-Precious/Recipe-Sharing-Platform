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
![Home Page](static/images/home.png)
---

## Sign Up Page

Users can register securely by providing:
- Email
- Username
- Password

Features:
- Secure authentication
- Email verification support
![Sign Up](static/images/signup.png)
---

##  Login Page

- Secure login using email and password
- Redirects to dashboard after successful login
![Log In](static/images/login.png)

---

## Categories / Dashboard Page

After login, users can:

- Browse recipes by category (Dessert, Dinner, etc.). After clicking a category a page shows up of the recipes that fall under that category.
- Use the search bar to find recipes
- Add a new recipe
- View collection (Approved, Pending, Rejected)
- Access Favorites section
![Category](static/images/category1.png)
![Category](static/images/category2.png)

---

## Recipes Page

- Displays recipe image, title, and description
- Shows premium lock icon for paid recipes
- Heart icon to favorite recipes
![Recipe](static/images/recipe1.png)
![Recipe](static/images/recipe2.png)

Premium recipes:
- Require payment to unlock
- Show confirmation message after payment
- “Go to Recipe” button appears after successful payment
![Lock](static/images/lock1.png)
![Lock](static/images/lock2.png)
![Lock](static/images/lock3.png)

---

## Favorites Page

- Users can save recipes by clicking the heart icon
- Saved recipes appear in Favorites section
- Makes it easy to access loved recipes later
![Fav](static/images/fav.png)


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
![add](static/images/add.png)
![add](static/images/add2.png)
## Edit Recipe Page

Users can:
- Update recipe details
- Modify ingredients or instructions
- Re-upload images
- Resubmit for approval

---
## Collection
-users are able to see their submmitted recipes, rejected recipes, and pending approval recipes.
![collection](static/images/collection.png)
![collection](static/images/collection2.png)

## Admin Dashboard

Admin can:
- Approve or reject recipes
- Provide rejection reasons
- Manage users
- Manage categories
- Monitor platform activity
-Download a spreadsheet of recipes
![admin](static/images/admin1.png)
![admin](static/images/admin2.png)
![admin](static/images/admin3.png)
![admin](static/images/admin4.png)
![admin](static/images/admin5.png)
![admin](static/images/admin6.png)

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

# Watu

Watu is a minimalist establishment review app designed to help neurodivergent individuals discover inclusive, sensory-friendly spaces. Developed as a full-stack project, it highlights key features such as place search, user reviews, and community ratings using modern web technologies.

---

## Target Audience

Watu is built for the neurodiversity community. It empowers users to easily find museums, grocery stores, restaurants, and other public spaces that offer low-stimulus environments or inclusive accessibility practices.

---

## Site Goals

To deliver a fully functional, database-backed full-stack application that:

- Demonstrates complete CRUD operations across multiple models
- Integrates with external APIs (Google Places)
- Implements robust authentication, authorization, and user-specific interactions
- Prioritizes accessibility, intuitive UX design, and responsive front-end layouts

---

## Requirements Overview

Below is a summary of the development roadmap using Agile epics, user stories, and tasks.

### Epic 1: Establishment Discovery and Browsing
**Goal**: Enable users to search and explore a catalog of local establishments using the Google Places API.

**User Stories**
- Search for places by name, category, or location (TBD)
- View establishment details
- View community reviews on place pages
- Prompt login for any interactions

### Epic 2: User Authentication and Permissions
**Goal**: Provide account registration, login/logout functionality, and restrict interactive actions to authenticated users.

**User Stories**
- Register an account
- Log in and log out securely
- Restrict reviewing and rating to logged-in users

### Epic 3: Reviews and Ratings
**Goal**: Allow users to leave one review per establishment, including a rating and description.

**User Stories**
- Rate a place based on sensory criteria (e.g. noise, lighting)
- Leave a review with optional accessibility comments
- Edit or delete one’s own review
- Display average rating per place


### Epic 4: Accessibility Features
**Goal**: Ensure the application is usable for individuals with diverse needs.

**User Stories**
- Implement keyboard navigation throughout the app
- Provide text alternatives for all images and non-text content
- Ensure color contrast meets accessibility standards
- Use ARIA roles and properties to enhance screen reader support

### Epic 5: Admin Panel
**Goal**: Create an admin interface for managing users, reviews, and establishments.

**User Stories**
- View all user accounts and their activity

### Epic 6: User Dashboard (Strech Goal)
**Goal**: Provide a personal dashboard showing all reviews and ratings left by the user.

**User Stories**
- View all personal reviews in one place
- Edit or remove reviews from the dashboard

---

### Project Board
For detailed task management, please refer to the [GitHub Project Board](https://github.com/users/larevolucia/projects/14/views/1).

## Models Overview

The application consists of three main models: `User`, `Place`, and `Review`. Below is a summary of their relationships:

| Model  | Relationship                      |
| ------ | --------------------------------- |
| User   | One-to-many with `Review`         |
| Place  | One-to-many with `Review`         |
| Review | Belongs to one `User` and `Place` |

### User Model

Uses Django’s built-in User model for authentication.

- Linked to user-generated reviews.

### Place Model

Represents a real-world establishment sourced from the Google Places API.

**Fields**:

- `id` (`AutoField`, primary key)
- `place_id` (`CharField`): Unique identifier from Google
- `name` (`CharField`)
- `address` (`CharField`)
- `latitude` (`FloatField`)
- `longitude` (`FloatField`)
- `type` (`CharField`): Category (e.g. restaurant, museum)
- `created_at` (`DateTimeField`, auto)
- `updated_at` (`DateTimeField`, auto)

**Notes:**

- Stores only essential data locally for performance, cost efficiency, and caching.
- Populated dynamically upon first interaction or search.

### 3. Review Model
Represents a user’s review of a specific place.

**Fields:**

- `user` (`ForeignKey` to `User`)
- `place` (`ForeignKey` to `Place`)
- `text` (`TextField`)
- `rating` (`IntegerField`): 1–5 scale
- `sensory_notes` (`TextField`, optional): e.g. noise, lighting
- `is_edited` (`BooleanField`, default `False`)
- `created_at` (`DateTimeField`, auto)
- `updated_at` (`DateTimeField`, auto)

**Constraints**:

- One review per user per place (`unique_together` on `user` + `place`)



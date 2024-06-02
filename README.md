# Django Kitchen Management System

A Django-based web application for managing kitchen operations, including cooks, dish types, and dishes.

## Features

- Manage dish types
- Manage cooks and their years of experience
- Manage dishes, including details and pricing
- Assign cooks to dishes
- User authentication for secure access

## Models

### DishType

Represents different types of dishes.

- `name`: CharField

### Cook

Custom user model inheriting from Django's `AbstractUser`.

- `years_of_experience`: IntegerField

### Dish

Represents a dish in the kitchen.

- `name`: CharField
- `description`: TextField
- `price`: DecimalField
- `dish_type`: ForeignKey to `DishType`
- `cooks`: ManyToManyField with `Cook`

## Views

### Function-based Views

- `index`: Home page view showing statistics about cooks, dishes, and dish types.

### Class-based Views

#### DishType

- `DishTypeListView`: Lists all dish types
- `DishTypeCreateView`: Create a new dish type
- `DishTypeUpdateView`: Update an existing dish type
- `DishTypeDeleteView`: Delete an existing dish type

#### Dish

- `DishListView`: Lists all dishes with search functionality
- `DishDetailView`: Shows details of a specific dish
- `DishCreateView`: Create a new dish
- `DishUpdateView`: Update an existing dish
- `DishDeleteView`: Delete an existing dish

#### Cook

- `CookListView`: Lists all cooks
- `CookDetailView`: Shows details of a specific cook
- `CookCreateView`: Create a new cook
- `CookExperienceUpdateView`: Update a cook's experience
- `CookDeleteView`: Delete an existing cook

- `toggle_assign_to_dish`: Toggle assignment of a cook to a dish

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KwintDimon/restaurant-kitchen-service.git
    cd restaurant-kitchen-service
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables. Create a `.env` file in the root of your project directory with the following content:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

5. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Log in with your superuser credentials.
- Manage dish types, cooks, and dishes through the admin interface or the application views.
- Assign and unassign cooks to dishes through the dish detail view.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.


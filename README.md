# Taskson - Person Management Web Application

**Taskson** is a web application built with Django for managing a list of persons. It provides a user-friendly interface for adding, viewing, editing, and deleting person records. This project demonstrates a common use case of creating a CRUD application using Django, and it includes various components such as models, forms, views, templates, and JavaScript interactions.

## Features

- **Add Person**: Users can add a new person to the system by providing their name, address, age, and date of birth.

- **View Persons**: The application displays a table listing all the persons in the system, showing their name, address, age, and date.

- **Edit Person**: Users can edit the details of a person by clicking the "Edit" button. This opens a modal where they can update the person's information.

- **Delete Person**: To remove a person from the system, users can click the "Delete" button, which triggers a confirmation modal.

## Project Components

- **Models**: The project defines a Django model named `Person` to represent person records. The model includes fields for name, address, age, and date of birth.

- **Forms**: There are two forms in the project. The `PersonForm` is used for adding and editing persons, and the `DateForm` captures date information. These forms handle data validation and submission.

- **Views**: The project includes Django views for creating, updating, and deleting person records. There's also a view for rendering the HTML template.

- **HTML Templates**: The HTML template, 'person/person.html,' provides the frontend interface for the application. It includes forms for adding persons, a table for listing persons, and modals for editing and deleting.

- **JavaScript**: JavaScript functions are used to handle interactions with persons, such as adding, updating, and deleting. These functions use AJAX to communicate with the server for dynamic updates.

## Getting Started

1. Clone the repository to your local machine.
2. Create a virtual environment and install the required dependencies using `pip install -r requirements.txt`.
3. Run the Django development server with `python manage.py runserver`.
4. Access the application in your web browser at `http://localhost:8000`.

## Usage

- To add a new person, fill in the details in the "Add Person" section and click the "SUBMIT" button.
- To edit a person, click the "Edit" button next to their details, make the necessary changes in the modal, and click "Save changes."
- To delete a person, click the "Delete" button, and confirm the action in the delete confirmation modal.

## Contributions

Contributions to this project are welcome. If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is a demonstration of basic Django CRUD functionality. It uses Django, Bootstrap, and JavaScript to provide a user-friendly interface for managing person records.

---

Feel free to customize this README file further to include specific instructions for running the project in your development environment. Additionally, you can add information about project contributors, acknowledgments, or any other relevant details.

### Credit
[StudyGyaan](https://studygyaan.com/django/how-to-execute-crud-using-django-ajax-and-json) where you can find the original tutorial I modified and built this project from.
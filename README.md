# Library-Management-System
Library Management System Using Basic Python and MySQL Server


---

## Library Management System

The Library Management System is a simple and efficient solution for managing library operations using Python and MySQL. This system enables librarians to manage book inventories, track book issues, and handle book returns seamlessly. It is designed to support basic library functions, ensuring a smooth workflow for both librarians and library users.

### Key Features:

1. **Add Book**:
   - Functionality to add new books to the library's inventory.
   - Store details such as book title, author, ISBN, genre, and total number of copies.
   - Ensure unique ISBN for each book entry to prevent duplicates.

2. **Issue Book**:
   - Allow users to borrow books from the library.
   - Update the book status and reduce the total number of available copies.
   - Track which user has borrowed which book, along with the issue date.

3. **Submit Book**:
   - Manage the return of borrowed books.
   - Update the book status and increase the total number of available copies.
   - Track the return date and ensure the book is marked as available for future borrowing.

4. **Delete Book**:
   - Remove books from the library's inventory.
   - Ensure that books currently issued cannot be deleted.
   - Maintain an accurate record of available books.

5. **Display Book**:
   - List all books available in the library.
   - Display details such as title, author, ISBN, genre, and availability status.
   - Provide search functionality to find specific books quickly.

6. **Update Total Number of Books**:
   - Adjust the total number of copies for a specific book.
   - Manage inventory changes due to new purchases, donations, or lost/damaged books.
   - Ensure the inventory reflects the accurate count of each book.

### Technical Details:

- **Backend**: 
  - MySQL database to store book details, issue/return records, and user information.
  - Tables for Books, Users, and Transactions to manage library operations.

- **Frontend**:
  - Basic Python scripts for CRUD (Create, Read, Update, Delete) operations.
  - Command-line interface for interacting with the system.
  - User prompts for input and confirmation for various operations.

### Workflow:

1. **Adding Books**: Librarian inputs book details -> System stores details in the MySQL database.
2. **Issuing Books**: Librarian/user inputs book ID and user ID -> System checks availability -> If available, updates status and records issue details.
3. **Submitting Books**: User returns the book -> Librarian inputs book ID -> System updates status and records return details.
4. **Deleting Books**: Librarian inputs book ID -> System checks if the book is issued -> If not, deletes book from the database.
5. **Displaying Books**: User inputs search criteria (optional) -> System retrieves and displays matching book records.
6. **Updating Book Count**: Librarian inputs book ID and new count -> System updates the total number of copies in the database.

This Library Management System provides a fundamental yet effective way to manage a library's inventory and transactions, ensuring a streamlined process for both librarians and users.

---

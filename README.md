# Cricket Match Ticket Booking System

## Overview

The Cricket Match Ticket Booking System is a GUI application built using Python's `tkinter` library. This application allows users to book tickets for a cricket match by selecting different seating blocks and calculates the total cost including taxes. The system also provides a receipt with booking details and options to interact with a separate `Cafe` module.

## Features

- **Seating Blocks**: Users can select tickets from various blocks, each with different pricing.
- **Dynamic Pricing**: The application calculates the total cost based on selected blocks and number of tickets, including state tax.
- **Receipt Generation**: Displays a receipt with booking details such as block, number of tickets, state tax, subtotal, and total price.
- **Integration with Cafe Module**: A button that opens a separate `Cafe` window for additional services.
- **Reset and Exit Options**: Provides functionality to reset the form and exit the application.

## Installation

### Prerequisites

- Python 3.x
- `tkinter` (usually included with Python standard library)


Here's a sample README.md file for your Cricket Match Ticket Booking System project. This file provides an overview of the project, instructions for setting it up, and basic usage information.

markdown
Copy code
# Cricket Match Ticket Booking System

## Overview

The Cricket Match Ticket Booking System is a GUI application built using Python's `tkinter` library. This application allows users to book tickets for a cricket match by selecting different seating blocks and calculates the total cost including taxes. The system also provides a receipt with booking details and options to interact with a separate `Cafe` module.

## Features

- **Seating Blocks**: Users can select tickets from various blocks, each with different pricing.
- **Dynamic Pricing**: The application calculates the total cost based on selected blocks and number of tickets, including state tax.
- **Receipt Generation**: Displays a receipt with booking details such as block, number of tickets, state tax, subtotal, and total price.
- **Integration with Cafe Module**: A button that opens a separate `Cafe` window for additional services.
- **Reset and Exit Options**: Provides functionality to reset the form and exit the application.

## Installation

### Prerequisites

- Python 3.x
- `tkinter` (usually included with Python standard library)

### Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/cricket-match-ticket-booking-system.git
Navigate to the Project Directory

bash
Copy code
cd cricket-match-ticket-booking-system
Run the Application

Make sure you have Python installed on your machine. To run the application, use the following command:

bash
Copy code
python main.py
Usage
Select a Block: Check the checkboxes for the desired seating blocks.
Enter Number of Tickets: Input the number of tickets for each selected block.
Calculate Total: Click the "Total" button to calculate the total cost, which includes state tax and other charges.
View Receipt: The receipt will display the block, number of tickets, state tax, subtotal, and total price.
Cafe Module: Click the "Cafe" button to open the Cafe module (if available).
Reset Form: Use the "Reset" button to clear all selections and inputs.
Exit Application: Click the "Exit" button to close the application.
File Structure
main.py: Contains the main application code for the Cricket Match Ticket Booking System.
Cafe.py: Contains the code for the additional Cafe module window.
README.md: This file.
Contributing
Feel free to submit issues or pull requests. Contributions are welcome to improve the functionality and features of the system.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
tkinter for the GUI framework.
Inspiration from various ticket booking systems.

# cricket-cafe-tk

1. Purpose:
The Cricket Match Ticket Booking System allows users to book tickets for cricket matches. It provides a user-friendly interface to select seating blocks, calculate costs, and generate a booking receipt.

2. Features:
   Booking Interface:
        Seating Blocks:
         Users can select seats from different blocks, each with varying ticket prices (e.g., ₹200, ₹400, ₹500, ₹700, ₹800, ₹1000).
         Each block has its own checkbox and entry field for the number of tickets.
        Receipt Generation:
         Once the user selects seats and clicks "Total," the system calculates the total cost, state tax, sub-total, and generates a reference number.
         The receipt displays details including the selected block, number of tickets, state tax, sub-total, total price, reference number, date, and time.
        Buttons:
          Total: Calculates and displays the total cost based on selected seats.
          Cafe: Opens a separate Tkinter window (from the Cafe module) which might be used for additional services or features related to the café.
          Reset: Clears all selections and inputs, resetting the booking interface.
          Exit: Exits the application after confirming the user's intention.

3. Components:
  MainFrame:
    The main container frame with two primary sections: one for the booking interface and one for the receipt and buttons.
  TopFrame1:
      Contains the title of the application.
  TopFrame2:
      Divided into two sections:
        f1: Contains frames for seating blocks.
        f2: Contains frames for the receipt and buttons.
   Seating Blocks Frames (topLeft1, topLeft2, topLeft3, topLeft4, topLeft5, topLeft6):
      Display checkboxes and entry fields for selecting and inputting the number of tickets for each block.
    Receipt Frame (frametopRight):
      Displays booking details and generated receipt.
    Buttons Frame (frameBottomRight):
      Contains buttons for calculating total cost, accessing the café, resetting the form, and exiting the application.

4. Additional Features:
The project utilizes random number generation to create unique reference numbers for each booking.
Uses Tkinter widgets like Label, Checkbutton, Entry, and Button to create an interactive and responsive user interface.
Integrates date and time functionality to include current date and time in the receipt.

5. Dependencies:
Tkinter: For creating the graphical user interface.
Cafe Module: This module is referenced but not provided here. It should contain another Tkinter window related to café services or features.

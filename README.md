# Pomodoro Timer Application

A Python-based Pomodoro timer application that helps you manage your work and break times effectively using the Pomodoro Technique.

## Features

- 🍅 Work sessions (25 minutes)
- ⏸️ Short breaks (5 minutes)
- 🎯 Long breaks (20 minutes)
- ⏯️ Pause/Resume functionality
- 🔄 Reset option
- ✅ Progress tracking with checkmarks
- 🎨 Clean and intuitive interface

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

## Installation

1. Clone or download this repository
2. Make sure you have Python installed on your system
3. Place the `tomato.png` image file in the same directory as `main.py`

## How to Use

1. Run the application by executing `main.py`
2. Click the "Start" button to begin your first work session
3. The timer will automatically:
   - Run for 25 minutes (work session)
   - Take a 5-minute break after each work session
   - Take a 20-minute break after completing 4 work sessions
4. Use the controls:
   - Start: Begin the timer
   - Pause: Temporarily stop the timer
   - Reset: Stop and reset the timer to initial state
5. Checkmarks will appear below the timer to track completed work sessions

## Pomodoro Technique

The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This application follows the standard pattern:

1. Work for 25 minutes
2. Take a 5-minute break
3. Repeat steps 1-2 three more times
4. Take a longer 20-minute break
5. Start the cycle again

## Color Coding

- 🟢 Green: Work session
- 🟡 Pink: Short break
- 🔴 Red: Long break

## Troubleshooting

If you encounter any issues:
1. Make sure the `tomato.png` file is in the same directory as `main.py`
2. Ensure you have Python and tkinter installed
3. Check that all required files are present

## License

This project is open source and available for personal and educational use.

## Credits

Created as part of the 100 Days of Code Python Pro Bootcamp.

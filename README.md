# DREAMTEAM_task
Pytest/unit testing tasks


# Bug Hunt Training Program  

Welcome Detective!  
This repository is your training ground to master **pytest** and learn the art of finding bugs through testing.  

---

## Level 1: Assert Academy Training  

**Hey Detective!**  
Before you can join the elite **Bug Hunt Squad**, you must first pass your **Assert Academy Training**.  

Your mission is to explore and master different types of assertions by writing small test cases.  
This will prepare you for the real investigation in **Level 2**.  

### Training Steps (Rookie):  

1️**Install pytest**  
[Pytest Installation Guide](https://docs.pytest.org/en/stable/getting-started.html)  

2️**Learn your toolkit**  
[Pytest Assertions Documentation](https://docs.pytest.org/en/stable/how-to/assert.html)  

3️**Your Tasks**  
Write pytest test cases for these functions:  
- A function to add two numbers.  
- A function to check if a number is even or odd.  
- A function to print the first element of a list.  
- A function to divide two numbers.  
- A function with two parameters (`text` and `keyword`) that checks if the keyword exists in the text.  

Use different assertions like `assert`, `assertEqual`, `assertIsNone`, `assertGreater`, `assertLess`, etc. to test:  
- Normal cases  
- Error cases  
- Edge cases  

---
**OK Rookie,**  
Now you’ve completed your Academy Training and mastered the art of pytest assertions.  

Here is a test **assignment** for you.  
The Chief suspects that someone has slipped buggy logic into our mystery program. 
The code may or may not contain logical errors. 

###  Your Mission  
- You will be given a **buggy program**:  
  [schoolBounty.py](https://github.com/akdswordguy/DREAMTEAM_task/blob/main/TASKS/schoolBounty.py)   
- Your job is to **catch every bug** by writing proper pytest tests.  
- Document your findings.
- Remember to check:  
  - Normal cases (average/expected inputs)  
  - Lower limit cases  
  - Upper limit cases  
  - Error cases (invalid input, empty values, etc.)  

---

#  Level 2: The Secret Agency Assignment  

This is your next task [whereAmI.py](https://github.com/akdswordguy/DREAMTEAM_task/blob/main/TASKS/whereAmI.py)

---

This device can:  

- Fetch the user’s **current location** using their IP address.  
- Plot the location on a live **interactive map**.  

But beware — while the gadget is **powerful**, the Agency suspects it is also **bug-prone**.  

Your mission: hunt down the flaws by writing **pytest tests** and ensuring the gadget can’t be exploited. Then, improve the device based on your test findings that is you can make changes based on the test results to the code to make it better.

---

## Setup Instructions  

Clone this repository and set up your environment:  

```bash
# Create virtual environment
python3 -m venv venv

# Activate venv (Linux)
source venv/bin/activate

# Install dependencies
pip install requests
pip install folium
```
# Level 3 : The Governor Wants to Know the Weather 
Nice work Detective!!  
One last task — but this time you need to **build the software yourself**.  

The **Governor of our city** is asking for a tool that will give **live weather updates** of the place he wants.  

Your mission is to **build a Weather Application in Python** and then **test it like a pro**.  

---

## Requirements  

- Build a **command-line (terminal) application** (UI is **not required**).  
- The program should:  

1. **Ask the user for their current city** (where they are from).  
   - Fetch and display the weather for that city.  

2. **Ask the user for the destination city** (the place they want to visit).  
   - Fetch and display the weather for that city.  

3. After displaying both, ask:  
   `Do you want to check the weather of another place? (yes/no)`  

   - If the user types **yes**, repeat step 2.  
   - If the user types **no**, exit the program.  

4. **Test the code that you wrote.**

---

## Weather Details to Display  

- City Name  
- Country  
- Temperature (°C)  
- Humidity (%)  
- Weather Description (e.g., "clear sky", "rainy")  

---

## Example Run  

```bash
Enter your city: Delhi  
Weather in Delhi, IN:  
Temperature: 30°C  
Humidity: 40%  
Condition: clear sky  

Enter the city you want to visit: London  
Weather in London, GB:  
Temperature: 18°C  
Humidity: 70%  
Condition: light rain  

Do you want to check the weather of another place? (yes/no): yes  

Enter the city: Paris  
Weather in Paris, FR:  
Temperature: 20°C  
Humidity: 60%  
Condition: cloudy  

Do you want to check the weather of another place? (yes/no): no  
Exiting the program...
```

## Resources 

[Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
[Unit test mock](https://docs.python.org/3/library/unittest.mock.html)
[Pytest mock](https://pytest-mock.readthedocs.io/en/latest/)

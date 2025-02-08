# **Odd Number Doubling Script**  

## 📌 Overview  
This Python script takes an **odd starting number**, **doubles it a set number of times**, and stops when the result is **equal to, 1 above, or 1 below** the target number. It then displays the sequence in reverse order and indicates whether the final number is a match.  

## 🚀 Features  
✅ **User input for:**  
- An **odd starting number**  
- A **target number**  
- The **number of times to double**  

✅ **Stops automatically** when reaching a valid match.  
✅ **Displays the steps in reverse order** (as per requirements).  
✅ **Validates input** to ensure the starting number is odd.  

## 🔧 Usage  
### **1️⃣ Run the script**  
```sh
python OddMatch.py
```
or provide command-line arguments:  
```sh
python OddMatch.py <odd_start_number> <target_number>
```

### **2️⃣ Example Runs**  
#### **Run 1 (With Arguments)**  
```sh
python OddMatch.py 3 35
```
**Output:**  
```
24
12
6
24 (no match)
```

#### **Run 2 (With User Input)**  
```sh
python OddMatch.py
```
**Input & Output:**  
```
Enter an odd starting number: 3
Enter the target number: 35
Enter the number of times to double: 5
96
48
24
12
6
3
96 (no match)
```

#### **Run 3 (Matching 1 Above)**  
```sh
python OddMatch.py
```
**Input & Output:**  
```
Enter an odd starting number: 9
Enter the target number: 35
Enter the number of times to double: 20
36
18
9
36 match (1 above)
```

#### **Run 4 (Another Case of Matching 1 Above)**  
```sh
python OddMatch.py
```
**Input & Output:**  
```
Enter an odd starting number: 9
Enter the target number: 35
Enter the number of times to double: 5
36
18
9
36 match (1 above)
```

#### **Run 5 (No Match Found)**  
```sh
python OddMatch.py
```
**Input & Output:**  
```
Enter an odd starting number: 5
Enter the target number: 35
Enter the number of times to double: 4
80
40
20
10
5
```

## 🛠️ How It Works  
1. The script **doubles the starting number** a set number of times.  
2. It **stops early** if the number **equals the target** or is **1 above/below**.  
3. The **sequence is printed in reverse order**.  
4. The script **indicates if the final number is a match**.  

## 📂 File Structure  
```
OddMatch.py  # Main script
README.md  # Documentation
```

## ⚡ Future Improvements  
🔹 **Enhance input validation** to handle edge cases.  
🔹 **Convert to a function-based script** for easier module integration.  
🔹 **Build a GUI version** using Tkinter or PyQt.  

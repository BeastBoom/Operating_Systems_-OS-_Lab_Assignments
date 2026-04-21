# 🖥️ Operating Systems Lab Assignments  
  
## 📌 Overview  
This repository contains implementations of core Operating System algorithms developed as part of the OS Lab coursework.  
  
It includes:  
- CPU Scheduling Algorithms (FCFS & SJF)  
- Banker's Algorithm for Deadlock Avoidance  
- Page Replacement Algorithms (FIFO, LRU, Optimal, MRU, Second Chance)  
- Disk Scheduling Algorithms (FCFS, SSTF, SCAN, C-SCAN)  
  
All implementations are written in Python with proper structure, outputs, and analysis.  
  
---  
  
# 🚀 Navigation  
  
<p align="center">  
  <a href="#-assignment-1-cpu-scheduling"><button>Assignment 1</button></a> | <a href="https://github.com/BeastBoom/Operating_Systems_-OS-_Lab_Assignments/tree/main/Assignment-1"><button>Folder</button></a> </br>
  <a href="#-assignment-2-bankers-algorithm"><button>Assignment 2</button></a> | <a href="https://github.com/BeastBoom/Operating_Systems_-OS-_Lab_Assignments/tree/main/Assignment-2"><button>Folder</button></a> </br>
  <a href="#-assignment-3-page-replacement-algorithms"><button>Assignment 3</button></a> | <a href="https://github.com/BeastBoom/Operating_Systems_-OS-_Lab_Assignments/tree/main/Assignment-3"><button>Folder</button></a> </br>
  <a href="#-assignment-4-disk-scheduling-algorithms"><button>Assignment 4</button></a> | <a href="https://github.com/BeastBoom/Operating_Systems_-OS-_Lab_Assignments/tree/main/Assignment-4"><button>Folder</button></a> </br>
  <a href="#-features"><button>Features</button></a>  </br>
  <a href="#-project-structure"><button>Structure</button></a>    </br>
  <a href="#-outputs"><button>Outputs</button></a>  </br>
</p>  
  
---  
  
# 📘 Assignment 1: CPU Scheduling  
  
## 🔹 Algorithms Implemented  
- First Come First Serve (FCFS)  
- Shortest Job First (SJF - Non Preemptive)  
  
## ⚙️ Functionality  
- Process creation with PID, Arrival Time, Burst Time  
- Calculation of:  
  - Completion Time (CT)  
  - Turnaround Time (TAT)  
  - Waiting Time (WT)  
- Gantt Chart visualization  
- Average WT & TAT calculation  
- Comparison between FCFS and SJF  
  
## 📊 Key Insight  
SJF performs better than FCFS in minimizing waiting time by prioritizing shorter processes.  
  
---  
  
# 📘 Assignment 2: Banker's Algorithm  
  
## 🔹 Concept  
Banker's Algorithm is used to avoid deadlock by ensuring the system remains in a **safe state**.  
  
## ⚙️ Functionality  
- Input:  
  - Allocation Matrix  
  - Maximum Matrix  
  - Available Resources  
- Calculation:  
  - Need Matrix = Maximum - Allocation  
- Safety Algorithm:  
  - Checks if system is SAFE or UNSAFE  
  - Generates Safe Sequence  
- Step-by-step execution tracing  
  
## 🔐 Key Insight  
The system avoids deadlock by only allowing execution when resources satisfy:

Need ≤ Available

  
---  
  
# 📘 Assignment 3: Page Replacement Algorithms  
  
## 🔹 Algorithms Implemented  
- First In First Out (FIFO)  
- Least Recently Used (LRU)  
- Optimal Page Replacement  
- Most Recently Used (MRU)  
- Second Chance (Clock Algorithm)  
  
## ⚙️ Functionality  
- Input:  
  - Number of Frames  
  - Page Reference String  
- Simulation of each algorithm with step-by-step frame states  
- Page fault counting for each algorithm  
- Performance comparison across all algorithms  
- Best & Worst algorithm identification  
  
## 📊 Key Insight  
Optimal performs the best theoretically by replacing the page not needed for the longest time, while real-world algorithms like LRU approximate this behavior.  
  
---  
  
# 📘 Assignment 4: Disk Scheduling Algorithms  
  
## 🔹 Algorithms Implemented  
- First Come First Serve (FCFS)  
- Shortest Seek Time First (SSTF)  
- SCAN (Elevator Algorithm)  
- C-SCAN (Circular SCAN)  
  
## ⚙️ Functionality  
- Input:  
  - Number of Disk Requests  
  - Request Sequence  
  - Initial Head Position  
  - Disk Size  
- Step-by-step seek movement tracing  
- Total seek time calculation for each algorithm  
- Performance comparison across all algorithms  
- Best & Worst algorithm identification  
  
## 📊 Key Insight  
SSTF minimizes seek time by servicing the nearest request first, while SCAN and C-SCAN provide more uniform wait times and avoid starvation.  
  
---  
  
# ✨ Features  
  
✔ Clean and modular Python implementation    
✔ Proper matrix representation    
✔ Step-by-step execution output    
✔ Gantt Chart (Assignment 1)    
✔ Safe Sequence detection (Assignment 2)    
✔ Page fault tracking & comparison (Assignment 3)    
✔ Seek time calculation & comparison (Assignment 4)    
✔ Beginner-friendly code with comments    
✔ Accurate calculations and logic    
  
---  
  
# 📁 Project Structure  

OS-Lab/  
│  
├── Assignment-1/  
│ ├── code.ipynb  
│ └── Lab_Report-Assignment-1_Dhruv_Gupta_2401201015.pdf 
│  
├── Assignment-2/  
│ ├── code.ipynb   
│ └── Lab_Report-Assignment-2_Dhruv_Gupta_2401201015.pdf  
│  
├── Assignment-3/  
│ ├── code.py  
│ ├── Outputs/  
│ └── Lab_Report-Assignment-3_Dhruv_Gupta_2401201015.pdf  
│  
├── Assignment-4/  
│ ├── code.py  
│ ├── Outputs/  
│ └── Lab_Report-Assignment-4_Dhruv_Gupta_2401201015.pdf  
│  
└── README.md

---  
  
---  
  
# 📸 Outputs  
  
## 🔹 Assignment 1  
- Input Process Table    
- FCFS Output Table    
- SJF Output Table    
- Gantt Charts    
- Average Time Comparison    
  
## 🔹 Assignment 2  
- Allocation Matrix    
- Maximum Matrix    
- Need Matrix    
- Safe Sequence    
- System State (SAFE / UNSAFE)    
  
## 🔹 Assignment 3  
- Page Reference String    
- Frame States per Algorithm (FIFO, LRU, Optimal, MRU, Second Chance)    
- Page Fault Count per Algorithm    
- Performance Comparison Table    
- Best & Worst Algorithm Analysis    
  
## 🔹 Assignment 4  
- Request Queue & Initial Head Position    
- Seek Movement per Algorithm (FCFS, SSTF, SCAN, C-SCAN)    
- Total Seek Time per Algorithm    
- Performance Comparison Table    
- Best & Worst Algorithm Analysis    
  
---  
  
# 📊 Sample Output Highlights  
  
## CPU Scheduling

FCFS Avg WT: Higher  
SJF Avg WT: Lower

  
## Banker's Algorithm

System is SAFE  
Safe Sequence: P1 -> P3 -> P4 -> P0 -> P2

  
## Page Replacement

Optimal: Least Page Faults  
FIFO/MRU: Higher Page Faults

  
## Disk Scheduling

SSTF Seek Time: Lowest  
FCFS Seek Time: Highest

  
---  
  
# 🎯 Learning Outcomes  
  
- Understanding CPU scheduling techniques    
- Implementing optimization-based scheduling (SJF)    
- Learning deadlock avoidance strategies    
- Working with matrices and system states    
- Understanding page replacement strategies and memory management    
- Analyzing disk scheduling for efficient I/O operations    
- Comparing algorithm performance with quantitative metrics    
- Improving problem-solving and coding logic    
  
---  
  
# 🛠️ Technologies Used  
  
- Python 3.x
- Jupyter Notebook and Ubuntu Command Prompt
- Standard Python Libraries  
- Command Line Interface  
  
---  
  
# 📌 Notes  
  
- All algorithms are implemented from scratch  
- Proper edge cases handled (idle CPU, unsafe state, page faults, disk boundary)  
- Outputs are verified for correctness  
  
---  
  
# 👨‍💻 Author  
  
Dhruv Gupta    
BCA (AI & Data Science) 
Roll No : 2401201015 
  
---  

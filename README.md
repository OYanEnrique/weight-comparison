# ⚖️ Weight Comparison Analyzer

A command-line tool that allows a user to enter the names and weights of multiple people. After data entry is complete, it analyzes the list to find the heaviest and lightest weights and reports which people correspond to them.

## Features

* **Continuous Data Entry**: Users can register as many people as they want in a single session.
* **Real-time Min/Max Tracking**: The script identifies the highest and lowest weights as they are being entered.
* **Handles Ties**: Correctly lists all people who share the highest or lowest weight.
* **Clear Summary**: Provides a final report with the total count of people registered and the names associated with the extreme weights.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `weight_comparison.py`).
3.  Run the script from your terminal:
    ```sh
    python weight_comparison.py
    ```
4.  The program will prompt you for a name and a weight.
5.  After each person, it will ask if you want to continue. Enter `S` for yes or `N` for no.
6.  When you enter `N`, the script will display the final analysis.

### Example Session

```sh
> python weight_comparison.py
---Weight Comparison---
Name: John
Weight: 85
Continue? [S/N]s
Name: Maria
Weight: 60
Continue? [S/N]s
Name: Peter
Weight: 92
Continue? [S/N]s
Name: Anna
Weight: 60
Continue? [S/N]n

Until next time!

In total, you registered 4 people
The greatest weight was 92.0Kg. This weight is from [Peter]
The lower weight was 60.0Kg. This weight is from [Maria]
[Anna]
```

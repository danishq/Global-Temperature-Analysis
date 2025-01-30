# Global Temperature Analysis - Mini Project

## Overview

This project analyzes global temperature anomalies using historical data. It processes monthly temperature anomalies from a JSON dataset, aggregates them into yearly averages, applies a moving average for smoothing, and visualizes the trends using Matplotlib and Dash for interactive exploration.

## Features

- Reads and processes global temperature anomaly data from a JSON file.
- Aggregates monthly data into yearly averages.
- Applies a moving average to smooth temperature anomalies.
- Visualizes trends using Matplotlib.
- Provides an interactive dashboard with Dash and Plotly.

## Requirements

Ensure you have the following installed:

- Python 3.7+
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `dash`
  - `plotly`

## Installation

1. Clone this repository (or download the script):

   ```sh
   git clone https://github.com/your-repo/global-temp-analysis.git
   cd global-temp-analysis
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### 1. Running the Matplotlib Visualization

To generate a static plot using Matplotlib:

```sh
python main.py --plot
```

### 2. Running the Interactive Dashboard

To launch the Dash web app for interactive visualization:

```sh
python main.py --dashboard
```

After running the command, open your browser and go to `http://127.0.0.1:8050/`.

## File Structure

```
📂 global-temp-analysis
 ├── 📄 main.py            # Main script for analysis and visualization
 ├── 📄 requirements.txt   # Required Python packages
 ├── 📄 months.json        # Temperature anomaly dataset (monthly records)
 ├── 📄 README.md          # Project documentation
```

## Data Source

The dataset contains historical monthly temperature anomalies from global climate monitoring sources. It is stored in `months.json` and needs to be loaded into the script for processing.

## Notes

- Ensure that the `months.json` file is in the project directory before running the script.
- The moving average window size is set to 5 years for smoothing.
- The interactive Dash app allows users to filter data by year using a slider.

## License

This project is licensed under the MIT License.

## Contribution

Feel free to contribute by submitting pull requests or reporting issues!

---

**Author:** Danish Qureshi

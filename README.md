# 🌍 World Happiness Dashboard

Welcome to the **World Happiness Dashboard**, an interactive Streamlit application that allows users to explore and analyze global happiness data from 2015 to 2019.

## 📊 The Dashboard

The goal of this dashboard is to provide insights into the World Happiness dataset, enabling users to:
- Visualize happiness scores across countries, regions, and time.
- Filter and explore data by year, region, and country.
- Analyze correlations between happiness score components.
- Gain insights into contributing factors to happiness.

## 🗃️ Dataset

The World Happiness data is  locatedin the `/app/data` folder as individual CSV files for each year (2015–2019). These files contain happiness KPIs and explanatory factors for various countries.

## 🌟 Highlights

### Top 10
- The countries with highest and lowest average happiness scores and per year.
### Trends and comparison
<!-- 2. **Filter by region** or country.
3. **View happiness rankings**:
   - Display the top N happiest countries.
   - Display the bottom N countries.
4. **Plot correlations** between score components and happiness score. -->



## 🛠️ Installation

### 🚀 Quickstart with Python

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/georgi-alexandrov/world-happiness-dashboard
cd world-happiness-dashboard
```
## 🛠️ Installation

### 🚀 Quickstart local with python
```
git clone https://github.com/georgi-alexandrov/world-happiness-dashboard
cd world-happiness-dashboard
```
- with [uv](https://github.com/astral-sh/uv):

```powershell
# prepare the python enviroment
uv sync

# run the app
uv run streamlit run app/main.py
```

 - with pip
```powershell
# Install packages
pip install -r requirements.txt

# Run the app
python -m streamlit run app/main.py
```




# Stock Analysis with K-means Support and Resistance

This project visualizes stock data and overlays it with support and resistance levels determined using the k-means clustering algorithm. The plotted candlestick chart allows users to specify a date range for which the stock data is displayed and the respective support and resistance levels are calculated.

## Features
- Visualization of stock data in a candlestick format.
- Calculation of support and resistance levels using k-means clustering.
- Option to zoom into a specific date range for more detailed analysis.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python libraries: `pandas`, `plotly`, `scikit-learn`, `numpy`

You can install the required packages using `pip`:
```
pip install pandas plotly scikit-learn numpy
```

### Usage

1. Clone this repository:
```
git clone <repository-url>
```
2. Navigate to the directory:
```
cd <repository-directory>
```
3. Replace the placeholders `'YYYY-MM-DD'` for `start_date` and `end_date` with the desired date range in the script.
4. Run the script:
```
python main.py
```
This will display the candlestick chart for the specified date range with overlaid support (green lines) and resistance (red lines) levels.

## Methodology

1. **Data Loading**: The stock data is loaded from a CSV file into a Pandas DataFrame. The data should have columns: `timestamp`, `open`, `high`, `low`, `close`.

2. **K-means Clustering**: For determining the number of clusters, the Elbow method is employed. This method calculates the sum of squared distances for different numbers of clusters and picks an optimal number where the rate of change in distance starts decreasing. The support and resistance levels are then identified as the centers of these clusters.

3. **Visualization**: The data is visualized using Plotly, and the calculated support and resistance levels are overlaid as horizontal lines on the candlestick chart. Green lines represent support levels while red lines represent resistance levels.

## Contributing

Contributions are welcome! Please read the contribution guidelines before making any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- K-means clustering as a technique was introduced by Stuart Lloyd in 1957 and has been widely used in various domains since then.
- Special thanks to Plotly for their intuitive and interactive graphing library.

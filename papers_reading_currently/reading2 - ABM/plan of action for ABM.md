## List of papers which are present on ABM for finance.

1. **Agent-Based Modeling in Economics and Finance: Past, Present, and Future**

   - **Authors**: Robert L. Axtell, J. Doyne Farmer
   - **Publication**: Journal of Economic Literature, Vol. 63, No. 1, March 2025, pp. 197–287
   - **Description**: This paper reviews ABM’s evolution in finance, emphasizing its ability to model heterogeneous agents and complex market dynamics. It covers applications like volatility clustering, market impact, and systemic risk, and proposes future directions for ABM in designing robust financial systems.
2. **New Approaches in Agent-Based Modeling of Complex Financial Systems**

   - **Authors**: T. T. Chen, Bo Zheng, Yan Li, Xiong-Fei Jiang
   - **Publication**: Frontiers of Physics, 2017 (arXiv:1703.06840)
   - **Description**: The paper explores ABM for simulating collective behaviors in financial markets, focusing on empirical data-driven parameter estimation. It highlights how ABM captures temporal and spatial correlations, improving understanding of market fluctuations and dynamics.
3. **An Agent-Based Model for Designing a Financial Market That Works Well**

   - **Author**: Takanobu Mizuta
   - **Publication**: arXiv:1906.06000, June 2019
   - **Description**: This study uses an artificial market model (a type of ABM) to evaluate financial market designs, such as the impact of tick size changes on market stability. It demonstrates ABM’s utility in testing regulatory policies and their effects on market efficiency.
4. **Agent-Based Modeling for Complex Financial Systems**

   - **Authors**: Multiple (includes Michael P. Wellman)
   - **Publication**: 2024 (ResearchGate: October 22, 2024)
   - **Description**: This paper focuses on ensemble ABM techniques for high-frequency financial market simulations. It addresses non-identifiability in ABM by integrating multiple time series data, enhancing forecasting accuracy for complex financial systems.
5. **Exploring Complexity: A Bibliometric Analysis of Agent-Based Modeling in Finance and Banking**

   - **Authors**: Ștefan Ionescu, Camelia Delcea, Ionuț Nica, Gabriel Dumitrescu, Claudiu-Emanuel Simion, Liviu-Adrian Cotfas
   - **Publication**: International Journal of Financial Studies, Vol. 13, No. 2, April 2025
   - **Description**: A bibliometric analysis identifying key ABM research clusters in finance, such as financial economics and econophysics. It examines topics like volatility clustering and market microstructure, highlighting ABM’s role in understanding complex financial behaviors.
6. **Data-Driven Economic Agent-Based Models**

   - **Authors**: Multiple (not explicitly listed)
   - **Publication**: arXiv:2412.14130, December 2024
   - **Description**: This paper discusses data-driven ABMs for financial markets, using techniques like ensemble Kalman filters to calibrate models with real-world data. It emphasizes ABM’s superiority over equilibrium models for policy analysis and market forecasting.
7. **Agent-Based Model of Liquidity and Price Impact in Financial Markets**

   - **Authors**: Alessio Emanuele Biondo, Alessandro Pluchino, Andrea Rapisarda
   - **Publication**: Physica A: Statistical Mechanics and its Applications, Vol. 510, 2018, pp. 633–643
   - **Description**: This ABM simulates liquidity dynamics and price impact in financial markets, modeling heterogeneous agents with different trading strategies. It reproduces stylized facts like fat-tailed return distributions and volatility clustering.
8. **Systemic Risk and Stress Testing in Financial Networks: An Agent-Based Approach**

   - **Authors**: Rama Cont, Michel Bouchaud
   - **Publication**: Journal of Financial Stability, Vol. 49, 2020
   - **Description**: This paper develops an ABM to assess systemic risk in financial networks, simulating interbank lending and contagion effects. It provides insights into stress testing and the impact of network structure on financial stability.

---

### Papers along with their main findings or motives produced in the paper/journal

1. **Agent-Based Modeling in Economics and Finance: Past, Present, and Future**

   - **Primary Goal**: Review ABM’s applications in finance, such as modeling **volatility clustering**, **market impact**, and **systemic risk**, and propose a **roadmap for future ABM** use in designing realistic financial systems.
2. **New Approaches in Agent-Based Modeling of Complex Financial Systems**

   - **Primary Goal**: Develop ABMs that use empirical data to simulate collective behaviors and correlations in financial markets, focusing on accurate parameter estimation for market dynamics.
3. **An Agent-Based Model for Designing a Financial Market That Works Well**

   - **Primary Goal**: Use ABM to evaluate financial market designs (e.g., tick size changes) and their impact on market stability and efficiency, aiding regulatory policy design.
4. **Agent-Based Modeling for Complex Financial Systems**

   - **Primary Goal**: Apply ensemble ABM techniques to improve high-frequency financial market simulations, addressing non-identifiability issues for better forecasting accuracy.
5. **Exploring Complexity: A Bibliometric Analysis of Agent-Based Modeling in Finance and Banking**

   - **Primary Goal**: Analyze ABM research trends in finance, identifying key themes like volatility clustering and market microstructure to guide future research directions.
6. **Data-Driven Economic Agent-Based Models**

   - **Primary Goal**: Develop data-driven ABMs for financial markets, using calibration techniques like ensemble Kalman filters to track empirical data and enhance policy analysis.
7. **Agent-Based Model of Liquidity and Price Impact in Financial Markets**

   - **Primary Goal**: Simulate liquidity dynamics and price impact using ABM, reproducing stylized facts like fat-tailed return distributions and volatility clustering.
8. **Systemic Risk and Stress Testing in Financial Networks: An Agent-Based Approach**

   - **Primary Goal**: Model systemic risk in financial networks through ABM, simulating interbank lending and contagion to assess network stability under stress scenarios.

### How My Plan of Action to Test Papers Using Python Mesa Library

To recreate and validate the results of these papers using the Python Mesa library,i would like to follow this plan.below i am going to outline a general approach applicable to all papers, with specific considerations for their unique goals. The Mesa library is chosen for its flexibility in building ABMs, supporting agent interactions, scheduling, and data collection.

# Plan of Action: Testing ABM Finance Papers with Python Mesa Library

## Objective

Recreate and **validate key findings** from the listed ABM finance papers using the Python Mesa library, focusing on **simulating financial market dynamic**s, **systemic risk, liquidity, and regulatory impacts.**

## Tools and Requirements

- **Python Mesa Library**: For building and running ABM simulations.
- **Additional Libraries**: NumPy (for data handling), **Pandas** (for analysis), **Matplotlib/Seaborn** (for visualization), **SciPy** (for statistical analysis).
- **Data Sources**: Empirical financial data (e.g., **stock prices, order book data**) from open sources like Yahoo Finance or Alpha Vantage, where applicable.

## General Methodology

1. **Paper Analysis**:

   - Read the paper to identify the ABM structure: agents (e.g., traders, banks), behaviors (e.g., trading strategies, lending), interactions (e.g., order book, interbank network), and outputs (e.g., price volatility, systemic risk metrics).
   - Note key parameters, assumptions, and stylized facts (e.g., fat-tailed returns, volatility clustering) to validate.
2. **Model Design in Mesa**:

   - **Agents**: Define agent classes (e.g., `TraderAgent`, `BankAgent`) with attributes (e.g., wealth, risk appetite) and methods (e.g., `trade()`, `lend()`).
   - **Model**: Create a `FinancialMarketModel` class with environment setup (e.g., order book, network graph), agent initialization, and step scheduling.
   - **Scheduling**: Use Mesa’s `RandomActivation` or `SimultaneousActivation` for agent updates, depending on the paper’s time dynamics.
   - **Data Collection**: Implement Mesa’s `DataCollector` to track metrics (e.g., price series, liquidity, network stability).
3. **Implementation Steps**:

   - Map paper’s agent behaviors to Mesa agent methods.
   - Replicate market mechanisms (e.g., limit order book, interbank lending) using Python data structures (e.g., lists, NetworkX for networks).
   - Calibrate parameters using empirical data or paper-specified values.
   - Run simulations for sufficient steps to observe emergent behaviors.
4. **Validation**:

   - Compare simulation outputs to paper’s reported results (e.g., statistical properties like kurtosis for fat tails, autocorrelation for volatility clustering).
   - Use statistical tests (e.g., Kolmogorov-Smirnov test) to verify if simulated distributions match empirical or paper-reported distributions.
   - Visualize results (e.g., price trajectories, network contagion) to confirm qualitative behaviors.
5. **Testing and Debugging**:

   - Test model components incrementally (e.g., agent trading logic, order matching).
   - Use Mesa’s visualization tools (e.g., `ModularServer`) to inspect real-time dynamics.
   - Ensure reproducibility by setting random seeds.

## Paper-Specific Testing Strategies

1. **Agent-Based Modeling in Economics and Finance: Past, Present, and Future**

   - **Goal**: Reproduce volatility clustering and market impact.
   - **Mesa Approach**: Model traders with heterogeneous strategies (e.g., fundamentalist, chartist). Use `DataCollector` to track price volatility. Validate by computing autocorrelation of squared returns.
   - **Validation**: Check for positive autocorrelation in volatility and compare to empirical stock data.
2. **New Approaches in Agent-Based Modeling of Complex Financial Systems**

   - **Goal**: Simulate correlations using empirical data-driven parameters.
   - **Mesa Approach**: Import historical price data to calibrate agent trading rules. Implement a limit order book. Measure cross-correlations between simulated assets.
   - **Validation**: Compare simulated correlation matrices to historical data using Pearson correlation coefficients.
3. **An Agent-Based Model for Designing a Financial Market That Works Well**

   - **Goal**: Test tick size impact on market stability.
   - **Mesa Approach**: Implement an order book with variable tick sizes. Run simulations with different tick sizes and measure bid-ask spread and volatility.
   - **Validation**: Confirm that smaller tick sizes reduce spreads but may increase volatility, as per paper findings.
4. **Agent-Based Modeling for Complex Financial Systems**

   - **Goal**: Enhance high-frequency forecasting with ensemble methods.
   - **Mesa Approach**: Simulate multiple ABM runs with varied parameters (ensemble). Aggregate outputs (e.g., price predictions) and compare to a single-run model.
   - **Validation**: Use mean squared error to assess ensemble forecast accuracy against historical high-frequency data.
5. **Exploring Complexity: A Bibliometric Analysis of Agent-Based Modeling in Finance and Banking**

   - **Goal**: Reproduce volatility clustering and microstructure effects (less simulation-focused, but testable).
   - **Mesa Approach**: Model traders with adaptive strategies affecting order book depth. Track price volatility and order flow.
   - **Validation**: Verify volatility clustering via autocorrelation and fat-tailed returns via kurtosis.
6. **Data-Driven Economic Agent-Based Models**

   - **Goal**: Calibrate ABM with empirical data for policy analysis.
   - **Mesa Approach**: Use historical data to set agent parameters via Kalman filter-inspired updates. Simulate policy scenarios (e.g., tax changes) and measure market responses.
   - **Validation**: Compare simulated policy impacts (e.g., trading volume) to paper’s reported effects.
7. **Agent-Based Model of Liquidity and Price Impact in Financial Markets**

   - **Goal**: Reproduce fat-tailed returns and liquidity dynamics.
   - **Mesa Approach**: Model traders with liquidity-sensitive strategies. Implement an order book to track price impact of large orders.
   - **Validation**: Compute return distribution kurtosis and compare price impact functions to paper’s stylized facts.
8. **Systemic Risk and Stress Testing in Financial Networks: An Agent-Based Approach**

   - **Goal**: Simulate interbank contagion and systemic risk.
   - **Mesa Approach**: Use NetworkX to create an interbank network. Model banks as agents with lending/borrowing behaviors. Introduce shocks (e.g., bank default) and track contagion.
   - **Validation**: Measure network stability metrics (e.g., fraction of failed banks) and compare to paper’s stress test results.

## Sample Mesa Code Skeleton

```python
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import numpy as np

class TraderAgent(Agent):
    def __init__(self, unique_id, model, strategy="fundamentalist"):
        super().__init__(unique_id, model)
        self.wealth = 1000
        self.strategy = strategy
  
    def step(self):
        # Implement trading logic based on strategy
        if self.strategy == "fundamentalist":
            self.trade()
  
    def trade(self):
        # Example: Place buy/sell order
        pass

class FinancialMarketModel(Model):
    def __init__(self, N, tick_size=0.01):
        self.num_agents = N
        self.tick_size = tick_size
        self.schedule = RandomActivation(self)
        self.order_book = []  # Simplified order book
        self.datacollector = DataCollector(
            model_reporters={"Price": lambda m: m.get_current_price()},
            agent_reporters={"Wealth": lambda a: a.wealth}
        )
    
        # Create agents
        for i in range(self.num_agents):
            strategy = np.random.choice(["fundamentalist", "chartist"])
            agent = TraderAgent(i, self, strategy)
            self.schedule.add(agent)
  
    def get_current_price(self):
        # Return latest price from order book
        return 100.0  # Placeholder
  
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

# Run simulation
model = FinancialMarketModel(N=100, tick_size=0.01)
for i in range(1000):
    model.step()

# Analyze results
results = model.datacollector.get_model_vars_dataframe()
print(results)
```

## Execution Plan

1. **Setup Environment**:
   - Install Mesa: `pip install mesa`
   - Install dependencies: `pip install numpy pandas matplotlib seaborn networkx`
2. **Develop Models**:
   - For each paper, adapt the code skeleton to match the paper’s ABM structure.
   - Implement specific features (e.g., order book, network) as needed.
3. **Calibrate and Run**:
   - Use empirical data or paper parameters to initialize models.
   - Run simulations for 1000–10,000 steps, depending on the paper’s time scale.
4. **Validate Results**:
   - Compute metrics (e.g., volatility, kurtosis, contagion spread).
     - **Contagion spread** refers to the process by which financial distress or shocks propagate through interconnected entities in a financial system, such as banks or institutions. When one entity experiences a failure or significant loss, the effects can cascade through the network via lending relationships, shared exposures, or market interactions, potentially leading to widespread instability or systemic crises. Modeling contagion spread helps in understanding the resilience of financial networks and the mechanisms that amplify or mitigate systemic risk.
     - **Kurtosis** is a statistical measure that describes the "tailedness" or extremity of deviations in a probability distribution compared to a normal distribution. In financial markets, high kurtosis indicates that extreme price movements (large gains or losses) occur more frequently than would be expected under a normal distribution, resulting in "fat tails." Measuring kurtosis in simulated return distributions is crucial for validating whether an agent-based model accurately reproduces the empirical characteristics of financial time series.
   - Compare to paper findings using statistical tests and visualizations.
5. **Iterate**:
   - Adjust parameters or logic if results diverge significantly.
   - Document discrepancies and potential causes (e.g., simplified assumptions).

<!-- ## Challenges and Solutions

- **Challenge**: Access to high-frequency data for calibration.
  - **Solution**: Use open datasets (e.g., Yahoo Finance) or synthetic data based on paper descriptions.
- **Challenge**: Replicating complex market mechanisms (e.g., order book).
  - **Solution**: Simplify mechanisms (e.g., use a basic matching algorithm) while preserving key dynamics.
- **Challenge**: Computational cost of large-scale ABMs.
  - **Solution**: Optimize code (e.g., vectorize operations) and limit agent count initially. -->

## Deliverables

- For each paper:
  - A Mesa-based Python script replicating the ABM.
  - A report summarizing simulation results, validation metrics, and comparisons to paper findings.
  - Visualizations of key outputs (e.g., price series, network graphs).

## Timeline

- **Week 1–2**: Analyze papers, design models, and set up environment.
- **Week 3–6**: Implement and test models for each paper (1–2 papers per week).
- **Week 7–8**: Validate results, refine models, and compile reports.

# Indepth deliverables for each of the paper.

## Deliverables for Testing ABM Finance Papers with Python Mesa Library

The following sections detail the deliverables for each of the eight papers, focusing on recreating their ABM simulations using the Python Mesa library and validating their key findings. Each deliverable set includes code, simulation outputs, validation metrics, visualizations, and documentation to ensure comprehensive testing and alignment with the paper’s goals.

## 1. Agent-Based Modeling in Economics and Finance: Past, Present, and Future

**Primary Goal**: Review ABM’s applications in finance, such as modeling volatility clustering, market impact, and systemic risk, and propose a roadmap for future ABM use.

**Deliverables**:

- **Python Mesa Script (volatility_clustering_model.py)**:
  - A Mesa-based ABM simulating a financial market with heterogeneous traders (e.g., fundamentalists, chartists).
  - Agent classes: `TraderAgent` with attributes (wealth, strategy) and methods (trade based on fundamentalist or chartist logic).
  - Model class: `FinancialMarketModel` with a limit order book, random activation scheduler, and parameters for trader proportions and noise levels.
  - DataCollector to track price series, returns, and agent wealth over 5000 steps.
- **Simulation Output Data**:
  - CSV file (`volatility_results.csv`) containing time series of prices, returns, and squared returns for 10 simulation runs with different random seeds.
  - JSON file (`model_params.json`) documenting parameter settings (e.g., 100 traders, 50% fundamentalists, noise variance).
- **Validation Report (validation_report_1.md)**:
  - Statistical analysis of volatility clustering: Compute autocorrelation function (ACF) of squared returns using Pandas and SciPy.
  - Comparison to paper’s stylized facts: Positive ACF for lags 1–20, indicating volatility clustering.
  - Market impact analysis: Measure price changes after large orders and compare to paper’s qualitative descriptions.
  - Statistical tests: Kolmogorov-Smirnov test to compare simulated return distributions to empirical stock data (e.g., S&P 500 daily returns).
- **Visualizations (volatility_plots.pdf)**:
  - Plot 1: Time series of prices and returns for a single run, using Matplotlib.
  - Plot 2: ACF plot of squared returns, showing clustering persistence.
  - Plot 3: Histogram of returns with fitted fat-tail distribution (e.g., Student’s t).
- **Documentation (model_doc_1.md)**:
  - Description of model structure, agent behaviors, and order book mechanics.
  - Instructions for running the script and reproducing results.
  - Discussion of simplifications (e.g., simplified order matching) and their impact on results.
- **Supplementary Notebook (volatility_analysis.ipynb)**:
  - Jupyter Notebook with code for post-processing simulation data, generating plots, and performing statistical tests.

## 2. New Approaches in Agent-Based Modeling of Complex Financial Systems

**Primary Goal**: Develop ABMs that use empirical data to simulate collective behaviors and correlations in financial markets.

**Deliverables**:

- **Python Mesa Script (correlation_model.py)**:
  - Mesa ABM with `TraderAgent` class modeling multiple assets, calibrated using historical price data.
  - Model class: `MultiAssetMarketModel` with a multi-asset order book, random activation, and empirical parameter estimation (e.g., volatility from historical data).
  - DataCollector to track prices and returns for 3–5 assets over 3000 steps.
- **Simulation Output Data**:
  - CSV file (`correlation_results.csv`) with price and return time series for each asset across 10 runs.
  - CSV file (`empirical_params.csv`) with parameters derived from historical data (e.g., daily returns from Yahoo Finance for stocks like AAPL, MSFT).
- **Validation Report (validation_report_2.md)**:
  - Correlation analysis: Compute Pearson correlation coefficients for simulated asset returns using Pandas.
  - Comparison to empirical correlations: Validate against historical correlation matrices from the same stocks.
  - Temporal correlation: Measure ACF of returns to confirm realistic market behavior.
  - Error metrics: Mean absolute error (MAE) between simulated and empirical correlation matrices.
- **Visualizations (correlation_plots.pdf)**:
  - Plot 1: Heatmap of simulated vs. empirical correlation matrices using Seaborn.
  - Plot 2: Time series of prices for multiple assets in a single run.
  - Plot 3: Scatter plot of simulated vs. empirical pairwise returns.
- **Documentation (model_doc_2.md)**:
  - Details on data preprocessing (e.g., downloading historical data via yfinance) and parameter calibration.
  - Explanation of multi-asset order book implementation and agent trading rules.
  - Notes on reproducibility and data source limitations.
- **Supplementary Notebook (correlation_analysis.ipynb)**:
  - Notebook for data calibration, simulation analysis, and visualization generation.

## 3. An Agent-Based Model for Designing a Financial Market That Works Well

**Primary Goal**: Evaluate financial market designs (e.g., tick size changes) and their impact on market stability and efficiency.

**Deliverables**:

- **Python Mesa Script (tick_size_model.py)**:
  - Mesa ABM with `TraderAgent` class implementing buy/sell orders at varying tick sizes.
  - Model class: `MarketDesignModel` with a limit order book, configurable tick sizes (e.g., 0.01, 0.1), and random activation.
  - DataCollector to track bid-ask spread, price volatility, and trading volume over 2000 steps.
- **Simulation Output Data**:
  - CSV file (`tick_size_results.csv`) with metrics (spread, volatility, volume) for tick sizes [0.01, 0.05, 0.1] across 10 runs.
  - JSON file (`tick_params.json`) with simulation parameters (e.g., 100 traders, order size distribution).
- **Validation Report (validation_report_3.md)**:
  - Analysis of tick size effects: Compare average bid-ask spread and volatility across tick sizes.
  - Validation against paper: Confirm smaller tick sizes reduce spreads but increase volatility.
  - Statistical tests: ANOVA to assess significant differences in metrics across tick sizes.
- **Visualizations (tick_size_plots.pdf)**:
  - Plot 1: Boxplot of bid-ask spreads for each tick size using Seaborn.
  - Plot 2: Time series of price volatility for different tick sizes.
  - Plot 3: Bar plot of average trading volume by tick size.
- **Documentation (model_doc_3.md)**:
  - Description of order book mechanics and tick size implementation.
  - Instructions for modifying tick sizes and running simulations.
  - Discussion of model assumptions (e.g., uniform order sizes) and limitations.
- **Supplementary Notebook (tick_size_analysis.ipynb)**:
  - Notebook for analyzing simulation outputs, generating plots, and performing statistical tests.

## 4. Agent-Based Modeling for Complex Financial Systems

**Primary Goal**: Apply ensemble ABM techniques to improve high-frequency financial market simulations.

**Deliverables**:

- **Python Mesa Script (ensemble_model.py)**:
  - Mesa ABM with `TraderAgent` class for high-frequency trading (e.g., second-level updates).
  - Model class: `HighFrequencyMarketModel` with ensemble runs (10 models with varied parameters, e.g., trader aggression).
  - DataCollector to track price predictions and trading activity over 1000 steps.
- **Simulation Output Data**:
  - CSV file (`ensemble_results.csv`) with price time series for each ensemble run and aggregated predictions.
  - CSV file (`single_run_results.csv`) for a single ABM run for comparison.
- **Validation Report (validation_report_4.md)**:
  - Ensemble performance: Compare aggregated price predictions to single-run predictions using mean squared error (MSE).
  - Validation against paper: Confirm ensemble reduces forecasting error.
  - Comparison to empirical data: MSE against high-frequency data (e.g., 1-second stock prices from open datasets).
- **Visualizations (ensemble_plots.pdf)**:
  - Plot 1: Time series of ensemble vs. single-run price predictions.
  - Plot 2: Error distribution histogram for ensemble predictions.
  - Plot 3: Line plot of MSE over time for ensemble vs. single run.
- **Documentation (model_doc_4.md)**:
  - Explanation of ensemble implementation (parallel runs with parameter variation).
  - Instructions for running ensemble simulations and aggregating outputs.
  - Notes on computational considerations (e.g., memory usage).
- **Supplementary Notebook (ensemble_analysis.ipynb)**:
  - Notebook for ensemble aggregation, error analysis, and visualization.

## 5. Exploring Complexity: A Bibliometric Analysis of Agent-Based Modeling in Finance and Banking

**Primary Goal**: Analyze ABM research trends, identifying themes like volatility clustering and market microstructure.

**Deliverables**:

- **Python Mesa Script (microstructure_model.py)**:
  - Mesa ABM with `TraderAgent` class modeling adaptive strategies affecting order book depth.
  - Model class: `MicrostructureModel` with a detailed limit order book and random activation.
  - DataCollector to track price volatility, order flow, and book depth over 3000 steps.
- **Simulation Output Data**:
  - CSV file (`microstructure_results.csv`) with price, volatility, and order book metrics for 10 runs.
  - JSON file (`microstructure_params.json`) with parameters (e.g., 100 traders, order cancellation rates).
- **Validation Report (validation_report_5.md)**:
  - Volatility clustering: Compute ACF of squared returns to confirm clustering.
  - Microstructure effects: Analyze order book depth and its impact on price stability.
  - Validation against paper: Confirm fat-tailed returns (kurtosis > 3) and volatility clustering.
  - Statistical tests: Kurtosis calculation and comparison to empirical data.
- **Visualizations (microstructure_plots.pdf)**:
  - Plot 1: Time series of prices and order book depth.
  - Plot 2: ACF plot of squared returns.
  - Plot 3: Histogram of returns with fitted fat-tail distribution.
- **Documentation (model_doc_5.md)**:
  - Description of order book dynamics and adaptive trader strategies.
  - Instructions for running and analyzing simulations.
  - Discussion of simplifications (e.g., fixed order sizes).
- **Supplementary Notebook (microstructure_analysis.ipynb)**:
  - Notebook for post-processing, statistical analysis, and visualization.

## 6. Data-Driven Economic Agent-Based Models

**Primary Goal**: Calibrate ABMs with empirical data for policy analysis.

**Deliverables**:

- **Python Mesa Script (data_driven_model.py)**:
  - Mesa ABM with `TraderAgent` class using parameters calibrated via empirical data.
  - Model class: `PolicyMarketModel` with a limit order book and policy scenarios (e.g., transaction tax).
  - DataCollector to track trading volume, prices, and agent wealth over 4000 steps.
- **Simulation Output Data**:
  - CSV file (`policy_results.csv`) with metrics for baseline and policy scenarios across 10 runs.
  - CSV file (`calibration_params.csv`) with parameters derived from empirical data (e.g., volatility from stock returns).
- **Validation Report (validation_report_6.md)**:
  - Policy impact: Compare trading volume and volatility under different policy scenarios.
  - Calibration accuracy: Validate parameters against historical data using MAE.
  - Validation against paper: Confirm policy effects (e.g., reduced volume with taxes).
- **Visualizations (policy_plots.pdf)**:
  - Plot 1: Time series of trading volume for baseline vs. policy scenarios.
  - Plot 2: Boxplot of volatility across scenarios.
  - Plot 3: Agent wealth distribution histogram.
- **Documentation (model_doc_6.md)**:
  - Details on calibration process (e.g., Kalman filter-inspired updates).
  - Instructions for applying different policy scenarios.
  - Notes on data sources and calibration challenges.
- **Supplementary Notebook (policy_analysis.ipynb)**:
  - Notebook for calibration, policy simulation, and visualization.

## 7. Agent-Based Model of Liquidity and Price Impact in Financial Markets

**Primary Goal**: Simulate liquidity dynamics and price impact, reproducing stylized facts.

**Deliverables**:

- **Python Mesa Script (liquidity_model.py)**:
  - Mesa ABM with `LiquidityAgent` class implementing liquidity-sensitive trading.
  - Model class: `LiquidityMarketModel` with a limit order book tracking large orders.
  - DataCollector to track price impacts, returns, and liquidity metrics over 5000 steps.
- **Simulation Output Data**:
  - CSV file (`liquidity_results.csv`) with price series, return distributions, and liquidity metrics for 10 runs.
  - JSON file (`liquidity_params.json`) with parameters (e.g., order size distribution, liquidity levels).
- **Validation Report (validation_report_liquidity.md)**:
  - Stylized facts: Compute kurtosis of returns to confirm fat tails (>3) and ACF for volatility clustering.
  - Price impact: Measure price changes after large orders and fit a power-law function.
  - Validation against paper: Compare impact functions and distribution shapes to reported results.
- **Visualizations (liquidity_plots.pdf)**:
  - Plot 1: Time series of prices and liquidity levels.
  - Plot 2: Log-log plot of price impact vs. order size.
  - Plot 3: Return distribution histogram with power-law fit.
- **Documentation (model_doc_liquidity.md)**:
  - Explanation of liquidity modeling and price impact calculation.
  - Instructions for running simulations and analyzing results.
  - Discussion of model assumptions (e.g., constant market depth).
- **Supplementary Notebook (liquidity_analysis.ipynb)**:
  - Notebook for statistical analysis, impact function fitting, and visualization.

## 8. Systemic Risk Modeling and Stress Testing in Financial Networks: An Agent-Based Approach

**Primary Goal**: Model systemic risk in financial networks, simulating interbank lending and contagion.

**Deliverables**:

- **Python Mesa Script (network_model.py)**:
  - Mesa ABM with `BankAgent` class modeling lending/borrowing behaviors.
  - Model class: `InterbankNetworkModel` with a NetworkX graph for interbank connections and shock scenarios (e.g., bank default).
  - DataCollector to track bankruptcy events, network stability, and contagion spread over 100 steps.
- **Simulation Output Data**:
  - CSV file (`network_results.csv`) with metrics (e.g., fraction of failed banks, contagion size) for 10 runs.
  - JSON file (`network_params.json`) with parameters (e.g., network density, shock magnitude).
- **Validation Report (validation_network.md)**:
  - Contagion analysis: Measure fraction of banks affected by initial shocks.
  - Validation against paper: Compare contagion metrics to reported stress test outcomes.
  - Network stability: Analyze degree centrality and clustering coefficients using NetworkX.
- **Visualizations (network_plots.pdf)**:
  - Plot 1: Network graph showing contagion spread at different time steps.
  - Plot 2: Time series of failed banks for different shock scenarios.
  - Plot 3: Histogram of contagion sizes across runs.
- **Documentation (model_doc_network.md)**:
  - Description of network structure and shock propagation rules.
  - Instructions for running simulations and visualizing networks.
  - Notes on simplifications (e.g., static network topology).
- **Supplementary Notebook (network_analysis.ipynb)**:
  - Notebook for network analysis, shock simulation, and visualization.

## General Notes

- **Reproducibility**: All scripts include random seeds and documented parameters to ensure consistent results.
- **Data Sources**: Empirical data (e.g., stock prices) will be sourced from open APIs (Yahoo Finance, Alpha Vantage) or synthetic data if unavailable.
- **Validation Rigor**: Each report uses statistical tests to quantify alignment with paper findings, ensuring objective validation.
- **Scalability**: Models are optimized for 100–200 agents initially, with documentation on scaling to larger systems if needed.

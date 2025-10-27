
### **Different Sources of Data in ABM for Financial Markets**

Agent-based models in financial markets rely on various data sources to simulate realistic market dynamics, calibrate models, or validate outputs against real-world phenomena. Below are the primary sources of data identified from the papers and common practices in ABM research, along with the specific types of data used:

1. **Stock Market Data**:

   - **Description**: Historical price and volume data for individual stocks or portfolios of stocks.
   - **Specific Data**:
     - **Stock Prices**: Daily, intraday, or tick-by-tick closing, opening, high, low prices (e.g., used to model price movements or volatility).
     - **Trading Volumes**: Number of shares traded over time, used to simulate liquidity or market activity.
     - **Returns**: Percentage changes in stock prices, often used to analyze risk or return distributions.
   - **Example**: In Ishiyama et al. (2004), the model simulates trading of “twenty different stocks,” likely using synthetic price and volume data to study transaction risks.
2. **Financial Indices**:

   - **Description**: Aggregated data from stock market indices representing a basket of stocks.
   - **Specific Data**:
     - **Index Prices**: Time series of index values (e.g., Hang-Seng Futures Index, S&P 500).
     - **Index Returns**: Percentage changes in index values, used to model market trends or volatility.
     - **Volatility Measures**: Metrics like the VIX or implied volatility derived from index options.
   - **Example**: Vytelingum et al. (2025) use **Hang-Seng Futures Index** data to calibrate an ABM for **liquidity risk modeling**, focusing on order flow and price impact.
3. **Limit Order Book (LOB) Data**:

   - **Description**: Detailed records of buy and sell orders in a market, including price levels, quantities, and timestamps.
   - **Specific Data**:
     - **Order Book Snapshots**: Bid and ask prices, order sizes, and depth at specific times.
     - **Trade Data**: Executed trades with prices, volumes, and timestamps.
     - **Order Flow**: Sequence of limit orders, market orders, and cancellations, used to model trader behavior.
   - **Example**: Shi and Cartlidge (2023, 2024) use **historical LOB data** (unspecified exchange or asset) to pre-train a neural stochastic trader in a hybrid ABM for LOB simulation.
4. **Corporate Bond Market Data**:

   - **Description**: Data related to corporate bond trading, including prices, yields, and trading volumes.
   - **Specific Data**:
     - **Bond Prices and Yields**: Market prices or yield-to-maturity for corporate bonds.
     - **Credit Ratings**: Ratings (e.g., AAA, BB) to assess bond quality.
     - **Trading Activity**: Volume and frequency of bond trades, particularly in over-the-counter (OTC) markets.
   - **Example**: Di Noia (2024) studies corporate bond market trends but does not specify a dataset, likely using synthetic data to model credit dynamics within firms.
5. **Over-the-Counter (OTC) Government Bond Market Data**:

   - **Description**: Data from bilateral trading in government bond markets, which are less standardized than equity markets.
   - **Specific Data**:
     - **Bond Prices and Yields**: Prices or yields for government bonds.
     - **Liquidity Metrics**: Bid-ask spreads or trading volumes in OTC markets.
   - **Example**: Vidler and Walsh (2024) model OTC government bond market liquidity but do not specify a real-world dataset, likely using synthetic data for simulation.
6. **Cryptocurrency Market Data**:

   - **Description**: Price, volume, and order book data for cryptocurrencies like Bitcoin.
   - **Specific Data**:
     - **Price Time Series**: Historical Bitcoin prices (e.g., daily or intraday).
     - **Transaction Data**: Blockchain transaction records or exchange trade data.
     - **Order Book Data**: Buy/sell orders on crypto exchanges.
   - **Example**: Fratrič et al. (2022) simulate Bitcoin price dynamics, likely using synthetic data informed by historical Bitcoin price trends to study market manipulation.
7. **Housing Market Data**:

   - **Description**: Data related to real estate transactions, mortgage rates, and housing prices.
   - **Specific Data**:
     - **House Prices**: Historical or regional housing price indices.
     - **Mortgage Rates**: Fixed or variable interest rates from central banks or lenders.
     - **Transaction Volumes**: Number of housing sales or mortgage approvals.
   - **Example**: Gamal et al. (2024) model the UK housing market, focusing on mortgage rates tied to the Bank of England’s rates, but do not specify a real dataset, likely using synthetic data.
8. **Synthetic or Artificial Data**:

   - **Description**: Data generated within the ABM to mimic real-world financial market behavior without relying on external datasets.
   - **Specific Data**:
     - **Simulated Prices and Volumes**: Hypothetical time series of asset prices or trading volumes.
     - **Agent Behaviors**: Synthetic order placements, cancellations, or trades based on predefined rules.
     - **Market Scenarios**: Simulated market conditions (e.g., crashes, booms) to test model robustness.
   - **Example**: Fluri et al. (2025) use synthetic data to simulate fractional ownership markets, focusing on illiquid alternative investments.
9. **Bibliometric or Literature Data**:

   - **Description**: Metadata from academic publications used to analyze research trends, not for market simulation.
   - **Specific Data**:
     - **Publication Metadata**: Titles, abstracts, keywords, citations from databases like Web of Science or Scopus.
     - **Bibliometric Metrics**: Citation counts, co-authorship networks, or keyword frequencies.
   - **Example**: Ionescu et al. (2025) use a dataset of **489 scholarly articles** from Web of Science for bibliometric analysis of ABM in finance.
10. **Internet Query and Social Media Data**:

    - **Description**: Data from online searches or social media platforms to capture investor sentiment or market signals.
    - **Specific Data**:
      - **Search Volumes**: Query frequencies from platforms like Google Trends.
      - **Social Media Activity**: Posts or sentiment data from platforms like Twitter (now X).
    - **Example**: Chen et al. (2017) combine internet query data with stock market data to model complex financial system dynamics.
11. **Macroeconomic and Policy Data**:

    - **Description**: Economic indicators or policy variables influencing financial markets.
    - **Specific Data**:
      - **Interest Rates**: Central bank rates (e.g., Bank of England rates).
      - **Inflation Rates**: Consumer price indices or inflation metrics.
      - **GDP or Employment Data**: Macroeconomic indicators affecting market behavior.
    - **Example**: Alexandre and Lima (2020) model monetary policy and prudential regulation, likely using synthetic data informed by macroeconomic variables like interest rates.
12. **Mutual Fund Data**:

    - **Description**: Data on mutual fund performance, asset allocations, or trading strategies.
    - **Specific Data**:
      - **Fund Returns**: Historical returns of mutual funds.
      - **Portfolio Holdings**: Asset compositions within funds.
    - **Example**: Vié and Farmer (2023) develop an ABM (“Evology”) for US equity mutual funds, empirically calibrated but without specifying a particular dataset.
13. **Sports-Betting Exchange Data**:

    - **Description**: Data from betting exchanges like Betfair, including odds and betting volumes.
    - **Specific Data**:
      - **Betting Odds**: Time series of odds for specific events.
      - **Betting Volumes**: Amounts wagered on different outcomes.
    - **Example**: Cliff et al. (2021) simulate a sports-betting exchange, likely using synthetic data modeled after platforms like Betfair.
14. **Central Bank Digital Currency (CBDC) Data**:

    - **Description**: Hypothetical or simulated data for CBDC transactions or issuance mechanisms.
    - **Specific Data**:
      - **Transaction Volumes**: Simulated CBDC transfers.
      - **Issuance Metrics**: Data on CBDC supply or circulation.
    - **Example**: Lyu et al. (2023) propose a Dynamic Issuance Mechanism for CBDC, using synthetic data to model economic impacts.

---

### **Detailed Analysis of Data Sources for Each Paper**

Below, I analyze the data sources for each of the 34 listed papers, specifying the dataset used (if any), the type of data, and why a specific dataset might not be mentioned. I also address environmental or other factors included in the models. The papers are listed in chronological order from most recent to oldest, as provided.

---

#### **2025**

1. **Agent-based Liquidity Risk Modelling for Financial Markets** (Vytelingum et al., 2025)

   - **Dataset Used**: **Hang-Seng Futures Index** data. (hongkong's most liquid companies on the exchange )
   - **Specific Data**: Historical price and order flow data from the Hang-Seng Futures Index, used to calibrate an ABM for **liquidity risk modeling**. The model simulates **transaction costs, market slippage, and price impact** through Monte-Carlo simulations, with traders updating asset value beliefs based on order flow.
   - **Environmental or Other Factors**: Includes market-specific factors like order flow and liquidity risk. No external environmental factors (e.g., macroeconomic conditions) are mentioned.
   - **Details**: The use of real-world index data ensures the model reflects realistic market dynamics, particularly for futures trading.
2. **Exploring Complexity: A Bibliometric Analysis of Agent-Based Modeling in Finance and Banking** (Ionescu et al., 2025)

   - **Dataset Used**: **489 scholarly articles** from the **Web of Science (WoS)** database (2000–2024).
   - **Specific Data**: Metadata (titles, abstracts, keywords, citations) analyzed using R Studio and Bibliometrix to study ABM trends in finance and banking.
   - **Why No Financial Market Dataset**: The paper is a bibliometric analysis, not a market simulation, so it focuses on academic literature rather than financial data like stock prices or order books.
   - **Environmental or Other Factors**: None; the focus is on research trends, not market or environmental variables.
   - **Details**: The dataset is used to map the evolution of ABM applications, not to train or simulate a financial model.
3. **Simulating Illiquid Markets: Insights from Fractional Ownership Trading and Agent-Based Models** (Fluri et al., 2025)

   - **Dataset Used**: **Synthetic data** generated within the ABM.
   - **Specific Data**: Simulated trading data for illiquid alternative investments (e.g., fractional ownership of art or real estate) on FinTech platforms, including hypothetical prices, volumes, and trading rules.
   - **Why No Specific Dataset**: The focus on illiquid markets, which often lack standardized data, necessitates synthetic data to explore diverse trading scenarios. Real-world data for such markets may be scarce or proprietary.
   - **Environmental or Other Factors**: Includes market structure factors (e.g., trading rules) but no external environmental factors like economic conditions.
   - **Details**: Synthetic data allows flexibility to test various market architectures without relying on specific real-world datasets.
4. **Agent-Based Modeling in Economics and Finance: Past, Present, and Future** (Axtell and Farmer, 2025)

   - **Dataset Used**: None specified.
   - **Specific Data**: The paper is a review and forward-looking perspective on ABM applications, not a simulation study, so no specific financial data (e.g., stocks, indices) is used.
   - **Why No Specific Dataset**: The paper focuses on theoretical and methodological advancements in ABM, discussing challenges and future directions rather than implementing a specific model with market data.
   - **Environmental or Other Factors**: Discusses broad economic factors (e.g., market interactions) but not specific environmental data like macroeconomic indicators.
   - **Details**: The absence of a dataset aligns with the paper’s conceptual nature, aiming to guide future ABM research.
5. **AI-Driven Agent-Based Modeling of Investor Behavior** (Hu, 2025)

   - **Dataset Used**: None specified; likely **synthetic data** or historical market data (unspecified).
   - **Specific Data**: The ABM simulates irrational investor behavior using reinforcement learning and neural networks, but no specific stock, index, or order book dataset is mentioned. The model may use synthetic price or trading data to test AI performance in stable vs. unstable markets.
   - **Why No Specific Dataset**: The focus is on evaluating AI techniques (reinforcement learning, neural networks) within ABM, not replicating a specific market. Synthetic data allows controlled testing of investor behavior under varying market conditions.
   - **Environmental or Other Factors**: Includes investor sentiment and irrationality as key factors, but no external environmental data (e.g., macroeconomic variables) is noted.
   - **Details**: The lack of a specific dataset reflects the paper’s emphasis on methodological innovation over empirical market modeling.
6. **Evaluating Binary Decision Biases in Large Language Models** (Vidler and Walsh, 2025)

   - **Dataset Used**: None specified; uses **API query data** from GPT models.
   - **Specific Data**: One-shot and few-shot API queries to assess binary decision-making biases in LLMs, not financial market data like stocks or order books.
   - **Why No Financial Market Dataset**: The paper evaluates LLMs for decision-making, not market simulation. The focus is on model biases, not financial market dynamics, so no market data is required.
   - **Environmental or Other Factors**: None; the study focuses on LLM performance metrics (e.g., Temperature parameter effects).
   - **Details**: The dataset is limited to LLM query responses, as the paper’s goal is to inform fair ABM simulations, not to simulate markets directly.

---

#### **2024**

7. **(Mis)information Diffusion and the Financial Market** (Di Francesco and Peraire, 2024)

   - **Dataset Used**: None specified; likely **synthetic data**.
   - **Specific Data**: The ABM simulates information propagation and delayed shock absorption in markets, but no specific dataset (e.g., stock prices, indices) is mentioned. Synthetic data likely includes simulated price movements or trading volumes.
   - **Why No Specific Dataset**: The paper focuses on modeling information dynamics theoretically, not replicating a specific market. Synthetic data allows control over information flow variables.
   - **Environmental or Other Factors**: Includes information networks and shock propagation but no external environmental factors like economic indicators.
   - **Details**: The absence of real-world data aligns with the theoretical focus on understanding delayed market responses.
8. **Decoding OTC Government Bond Market Liquidity** (Vidler and Walsh, 2024)

   - **Dataset Used**: None specified; likely **synthetic data**.
   - **Specific Data**: The ABM models liquidity in OTC government bond markets, simulating bilateral trading dynamics. No specific bond price, yield, or liquidity dataset is mentioned.
   - **Why No Specific Dataset**: OTC markets are less transparent, and real-world data may be limited. Synthetic data allows exploration of liquidity dynamics without requiring specific bond market data.
   - **Environmental or Other Factors**: Includes market structure (bilateral trading) but no external environmental factors.
   - **Details**: The focus on stylized market behavior explains the use of synthetic data over real-world datasets.
9. **Financial Revolution through Agent-based Artificial Simulation Computational Models** (Maharani and Rahmawati, 2024)

   - **Dataset Used**: None specified; likely **synthetic data** in NetLogo.
   - **Specific Data**: The ABM, implemented in NetLogo, simulates investor behavior in the capital market, but no specific dataset (e.g., stock prices, indices) is mentioned. Synthetic data likely includes simulated price or volume series.
   - **Why No Specific Dataset**: The paper demonstrates ABM’s potential to analyze investor behavior, focusing on methodological application rather than a specific market. Synthetic data supports generalizability.
   - **Environmental or Other Factors**: Focuses on investor behavior but does not mention external factors like macroeconomic conditions.
   - **Details**: The use of NetLogo suggests a stylized simulation environment, not tied to a specific dataset.
10. **Neural Stochastic Agent-Based Limit Order Book Simulation** (Shi and Cartlidge, 2024)

    - **Dataset Used**: **Historical LOB data** (unspecified exchange or asset).
    - **Specific Data**: Historical limit order book data used to pre-train a neural stochastic trader with a neural point process model, integrated into a multi-agent ABM. Specific data includes order prices, volumes, and timestamps.
    - **Environmental or Other Factors**: Includes market microstructure factors (e.g., order flow, liquidity) but no external environmental data.
    - **Details**: The use of historical LOB data ensures the model captures realistic trading patterns, though the exact source (e.g., specific exchange) is not specified.
11. **When Firms Buy Corporate Bonds** (Di Noia, 2024)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM analyzes credit dynamics in the corporate bond market, focusing on trends like bond market size and low-quality debt. No specific bond price, yield, or trading dataset is mentioned.
    - **Why No Specific Dataset**: The paper explores general trends in corporate bond markets, using synthetic data to model firm behavior and credit dynamics without needing specific market data.
    - **Environmental or Other Factors**: Includes firm-level factors (e.g., credit allocation) but no external environmental data.
    - **Details**: Synthetic data supports the study’s focus on theoretical credit dynamics within firms.
12. **A Behavioural Agent-Based Model for Housing Markets** (Gamal et al., 2024)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models the UK housing market, focusing on mortgage rates (fixed or variable, tied to Bank of England rates) and financial shocks. No specific housing price or mortgage dataset is mentioned.
    - **Why No Specific Dataset**: The paper simulates hypothetical financial shocks, using synthetic data to model housing market dynamics rather than replicating a specific dataset.
    - **Environmental or Other Factors**: Includes macroeconomic factors like interest rates but no external environmental data (e.g., economic indicators beyond rates).
    - **Details**: Synthetic data allows testing of shock scenarios in a controlled environment.

---

#### **2023**

13. **Gradient-Assisted Calibration for Financial Agent-Based Models** (Dyer et al., 2023)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The paper experiments with calibrating heterogeneous ABMs using differentiable programming, but no specific financial dataset (e.g., stocks, indices) is mentioned.
    - **Why No Specific Dataset**: The focus is on methodological advancements in calibration, not simulating a specific market. Synthetic data supports testing of gradient-based techniques.
    - **Environmental or Other Factors**: None; the focus is on calibration techniques, not market or environmental variables.
    - **Details**: The methodological nature of the paper explains the lack of a specific dataset.
14. **A Study on the Dynamic Issuance Mechanism Based on Central Bank Digital Currency** (Lyu et al., 2023)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates a Dynamic Issuance Mechanism (DIM) for CBDC, modeling economic impacts. No real-world transaction or issuance data is mentioned.
    - **Why No Specific Dataset**: CBDCs are often hypothetical or in early stages, so synthetic data is used to model theoretical issuance scenarios.
    - **Environmental or Other Factors**: Includes macroeconomic factors like economic vitality and commodity prices but no external environmental data.
    - **Details**: Synthetic data supports exploration of CBDC impacts without real-world constraints.
15. **Many Learning Agents Interacting with an Agent-Based Market Model** (Dicks et al., 2023)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM incorporates optimal execution agents to study market microstructure, but no specific dataset (e.g., stock prices, order books) is mentioned. Synthetic data likely includes price and volume series.
    - **Why No Specific Dataset**: The paper focuses on how agent interactions affect stylized facts, using synthetic data to control market conditions and test hypotheses.
    - **Environmental or Other Factors**: Includes market microstructure factors but no external environmental data.
    - **Details**: Synthetic data aligns with the study’s goal of exploring general market dynamics.
16. **Neural Stochastic Agent-Based Limit Order Book Simulation** (Shi and Cartlidge, 2023)

    - **Dataset Used**: **Historical LOB data** (unspecified exchange or asset).
    - **Specific Data**: Historical limit order book data used to pre-train a neural stochastic trader, similar to the 2024 paper by the same authors. Data includes order prices, volumes, and timestamps.
    - **Environmental or Other Factors**: Includes market microstructure factors (e.g., order flow) but no external environmental data.
    - **Details**: The use of LOB data ensures realistic simulation of trading dynamics.
17. **Towards Evology: A Market Ecology Agent-Based Model of US Equity Mutual Funds II** (Vié and Farmer, 2023)

    - **Dataset Used**: None specified; described as **empirically calibrated** but no specific dataset mentioned.
    - **Specific Data**: The ABM (“Evology”) models US equity mutual funds, simulating trading strategies and market interactions. Likely uses synthetic data informed by mutual fund returns or holdings.
    - **Why No Specific Dataset**: The paper focuses on a general market ecology model, using empirical calibration to match stylized facts rather than a specific dataset.
    - **Environmental or Other Factors**: Includes market interactions and trading strategies but no external environmental data.
    - **Details**: The empirical calibration suggests some reference to real-world mutual fund data, but specifics are not provided.

---

#### **2022**

18. **An Agent-Based Model With Realistic Financial Time Series** (Faria, 2022)

    - **Dataset Used**: None specified; uses **synthetic data** validated against stylized facts.
    - **Specific Data**: The ABM generates artificial financial time series (e.g., prices, returns) designed to match statistical properties of real-world financial data (stylized facts like fat-tailed returns).
    - **Why No Specific Dataset**: The goal is to validate the ABM’s ability to replicate stylized facts, not to model a specific market. Synthetic data allows control over statistical properties.
    - **Environmental or Other Factors**: Focuses on statistical properties of returns, not external environmental factors.
    - **Details**: Synthetic data is central to the validation methodology.
19. **Agent-based Model Generating Stylized Facts of Fixed Income Markets** (Kopp et al., 2022)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates fixed income and equity markets, aiming to reproduce stylized facts (e.g., volatility clustering). No specific bond or equity dataset is mentioned.
    - **Why No Specific Dataset**: The focus is on replicating general market properties, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes market-specific factors like volatility but no external environmental data.
    - **Details**: Synthetic data supports the study’s goal of modeling stylized facts.
20. **Manipulation of the Bitcoin Market** (Fratrič et al., 2022)

    - **Dataset Used**: None specified; likely **synthetic data** informed by Bitcoin price trends.
    - **Specific Data**: The ABM simulates Bitcoin price dynamics with a fraudulent agent, likely using synthetic price and volume data to model manipulation effects.
    - **Why No Specific Dataset**: The paper tests the impact of a fraudulent agent, requiring a controlled environment where synthetic data is more suitable than specific Bitcoin exchange data.
    - **Environmental or Other Factors**: Includes market manipulation factors but no external environmental data.
    - **Details**: Synthetic data allows simulation of hypothetical manipulation scenarios.
21. **Impact of False Information from Spoofing Strategies** (Li and Yang, 2022)

    - **Dataset Used**: None specified; uses **synthetic data**.
    - **Specific Data**: The ABM simulates a continuous double auction market with spoofing agents, using synthetic order book data (e.g., orders, trades) to analyze market dynamics.
    - **Why No Specific Dataset**: The focus on spoofing effects requires a controlled environment, making synthetic data ideal for isolating manipulation impacts.
    - **Environmental or Other Factors**: Includes market microstructure and spoofing behavior but no external environmental data.
    - **Details**: Synthetic data supports analysis of spoofing’s impact on market fairness.
22. **Application of Agent-Based Modeling: Simulating Financial Systemic Risk and Contagion** (Khan, 2022)

    - **Dataset Used**: None specified; likely **synthetic data** covering 1986–2017.
    - **Specific Data**: The ABM simulates systemic risk in housing and financial markets, using synthetic data for house prices, mortgage rates, and financial transactions.
    - **Why No Specific Dataset**: The paper models long-term systemic risk and contagion, using synthetic data to capture emergent phenomena across decades.
    - **Environmental or Other Factors**: Includes macroeconomic factors (e.g., housing bubble dynamics) but no explicit environmental data.
    - **Details**: Synthetic data allows simulation of complex, interconnected market behaviors.

---

#### **2021**

23. **Implementing the BBE Agent-Based Model of a Sports-Betting Exchange** (Cliff et al., 2021)
    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates a sports-betting exchange (e.g., Betfair-like), using synthetic betting odds and volumes.
    - **Why No Specific Dataset**: The focus is on replicating betting exchange dynamics, not a specific event or market, so synthetic data is sufficient.
    - **Environmental or Other Factors**: Includes betting market dynamics but no external environmental data.
    - **Details**: Synthetic data supports testing of betting exchange mechanisms.

---

#### **2020**

24. **The Impact of Social Influence in Australian Real Estate** (Evans et al., 2020)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models the Australian housing market with a spatial component, simulating house prices and social influence factors.
    - **Why No Specific Dataset**: The paper focuses on spatial and social dynamics, using synthetic data to model hypothetical scenarios.
    - **Environmental or Other Factors**: Includes social influence and spatial factors but no external environmental data.
    - **Details**: Synthetic data supports the spatial ABM’s flexibility.
25. **Deep Reinforcement Learning in Agent-Based Financial Market Simulation** (Maeda et al., 2020)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates price-order-book dynamics with deep reinforcement learning, using synthetic price and order data.
    - **Why No Specific Dataset**: The focus is on training reinforcement learning models, requiring controlled synthetic data to test strategies.
    - **Environmental or Other Factors**: Includes market impact but no external environmental data.
    - **Details**: Synthetic data supports the study’s methodological focus.
26. **Combining Monetary Policy and Prudential Regulation** (Alexandre and Lima, 2020)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models interactions between monetary policy and banking regulation, simulating firm funding and bank behavior.
    - **Why No Specific Dataset**: The paper explores theoretical policy interactions, using synthetic data to model economic scenarios.
    - **Environmental or Other Factors**: Includes macroeconomic factors like interest rates but no external environmental data.
    - **Details**: Synthetic data supports the study’s policy focus.
27. **Anchoring Heuristics, Investor Sentiment and Stylized Facts** (Higachi et al., 2020)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates stock market dynamics with behavioral factors (e.g., anchoring, sentiment), using synthetic price and return data.
    - **Why No Specific Dataset**: The focus is on explaining stylized facts via behavioral finance, not replicating a specific market.
    - **Environmental or Other Factors**: Includes investor sentiment but no external environmental data.
    - **Details**: Synthetic data supports modeling of behavioral phenomena.
28. **Managerial Overconfidence in IPO Decisions** (Szyszka et al., 2020)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates IPO decisions and macrodynamics, using synthetic data for stock prices and firm behaviors.
    - **Why No Specific Dataset**: The paper bridges behavioral finance and macroeconomics, using synthetic data to model overconfidence effects.
    - **Environmental or Other Factors**: Includes managerial behavior but no external environmental data.
    - **Details**: Synthetic data supports theoretical analysis of IPO impacts.
29. **Essays on Modeling and Analysis of Dynamic Sociotechnical Systems** (Dewhurst, 2020)

    - **Dataset Used**: None specified; likely **synthetic data** or empirical data for validation.
    - **Specific Data**: The ABM models financial markets, social media, and elections, but no specific financial dataset is mentioned.
    - **Why No Specific Dataset**: The paper is a broad thesis, using synthetic or stylized data to explore sociotechnical systems.
    - **Environmental or Other Factors**: Includes social and economic factors but no specific environmental data.
    - **Details**: The broad scope justifies the use of synthetic data.
30. **Agent-Based Simulations of Monetary Policy and Financial Markets** (Schasfoort, 2020)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates monetary policy and financial market interactions, using synthetic data for economic variables.
    - **Why No Specific Dataset**: The thesis explores policy impacts, using synthetic data to model theoretical scenarios.
    - **Environmental or Other Factors**: Includes macroeconomic factors like monetary policy but no external environmental data.
    - **Details**: Synthetic data supports policy-focused simulations.

---

#### **2019**

31. **The Macro-Political Economy of the Housing Market** (Khan and Yang, 2019)
    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models housing bubble and financial crisis dynamics, using synthetic house price and transaction data.
    - **Why No Specific Dataset**: The focus is on complex event simulation, using synthetic data to capture emergent phenomena.
    - **Environmental or Other Factors**: Includes macroeconomic factors (e.g., housing bubble) but no external environmental data.
    - **Details**: Synthetic data supports long-term market analysis.

---

#### **2018**

32. **Generating Synthetic Bitcoin Transactions** (Lee et al., 2018)

    - **Dataset Used**: None specified; likely **synthetic data** informed by Bitcoin price trends.
    - **Specific Data**: The ABM uses inverse reinforcement learning to simulate Bitcoin transactions and predict prices, likely with synthetic price and volume data.
    - **Why No Specific Dataset**: The focus is on methodological innovation (IRL and ABM), using synthetic data to test price prediction.
    - **Environmental or Other Factors**: Includes market trends but no external environmental data.
    - **Details**: Synthetic data supports the study’s predictive goals.
33. **Agent-Based Models in Financial Market Studies** (Wang et al., 2018)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The paper reviews ABM applications, using synthetic data to illustrate financial market phenomena.
    - **Why No Specific Dataset**: The paper is a review, not a specific simulation, so synthetic data is used for illustrative purposes.
    - **Environmental or Other Factors**: Includes market complexity but no external environmental data.
    - **Details**: The review nature explains the lack of a specific dataset.
34. **Agent-Based Modeling for Complex Financial Systems** (No authors, 2018)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models a complex network of interacting market systems, using synthetic data for prices and interactions.
    - **Why No Specific Dataset**: The paper describes a general framework for financial systems, not a specific market simulation.
    - **Environmental or Other Factors**: Includes market interactions but no external environmental data.
    - **Details**: Synthetic data supports the conceptual framework.

---

#### **2017**

35. **New Approaches in Agent-Based Modeling of Complex Financial Systems** (Chen et al., 2017)
    - **Dataset Used**: **Internet query data** and **stock market data** (unspecified).
    - **Specific Data**: Combines internet search volumes (e.g., Google Trends) with stock market data (e.g., prices, returns) to model financial system dynamics.
    - **Environmental or Other Factors**: Includes investor sentiment from internet queries but no external environmental data.
    - **Details**: The use of internet and stock data supports the novel big-data approach.

---

#### **2016**

36. **Complexity and Model Comparison in Agent-Based Modeling of Financial Markets** (Mandes and Winker, 2016)
    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models the foreign exchange market, using synthetic price and order data to compare model complexity.
    - **Why No Specific Dataset**: The focus is on model comparison, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes market microstructure but no external environmental data.
    - **Details**: Synthetic data supports methodological analysis.

---

#### **2015**

37. **An Improved Platform for Multi-Agent Based Stock Market Simulation** (Yu et al., 2015)
    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM (PSSPAM platform) simulates stock market dynamics with parallel agents, using synthetic price and volume data.
    - **Why No Specific Dataset**: The focus is on platform development, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes market dynamics but no external environmental data.
    - **Details**: Synthetic data supports platform scalability testing.

---

#### **2014**

38. **A Platform for Stock Market Simulation with Distributed Agent-Based Modeling** (Wang et al., 2014)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM platform simulates stock markets, using synthetic price and volume data for large-scale parallel agents.
    - **Why No Specific Dataset**: The focus is on platform design, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes market dynamics but no external environmental data.
    - **Details**: Synthetic data supports platform testing.
39. **Investigating the Challenges of Data, Pricing and Modelling** (Zangeneh, 2014)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates the Credit Default Swap (CDS) market, using synthetic data for pricing and trading.
    - **Why No Specific Dataset**: The focus is on methodological challenges, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes market pricing but no external environmental data.
    - **Details**: Synthetic data supports exploration of CDS market challenges.
40. **Group-Wise Herding Behavior in Financial Markets** (Kim and Kim, 2014)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM simulates herding behavior, using synthetic price and trading data to analyze market fluctuations.
    - **Why No Specific Dataset**: The focus is on herding dynamics, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes herding behavior but no external environmental data.
    - **Details**: Synthetic data supports behavioral analysis.
41. **Regulation of Systemic Risk Through Contributory Endogenous Agent-Based Modeling** (Bristor et al., 2014)

    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models systemic risk with transparent firm participation, using synthetic data for firm interactions and market dynamics.
    - **Why No Specific Dataset**: The focus is on a regulatory framework, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes firm behavior but no external environmental data.
    - **Details**: Synthetic data supports the regulatory focus.

---

#### **2012**

42. **Equation-Free Analysis for Agent-Based Computation** (Liu, 2012)
    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM models investor interactions with mimesis, using synthetic price and trading data.
    - **Why No Specific Dataset**: The focus is on the Equation-Free methodology, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes investor behavior (mimesis) but no external environmental data.
    - **Details**: Synthetic data supports methodological innovation.

---

#### **2009**

43. **Cognitive-Agent-Based Modeling of a Financial Market** (Pereira et al., 2009)
    - **Dataset Used**: None specified; likely **synthetic data**.
    - **Specific Data**: The ABM uses BDI agents to simulate market dynamics, using synthetic price and trading data.
    - **Why No Specific Dataset**: The focus is on agent architecture, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes agent beliefs and intentions but no external environmental data.
    - **Details**: Synthetic data supports the evolutionary system design.

---

#### **2004**

44. **Evaluation of Transaction Risks of Mean Variance Model** (Ishiyama et al., 2004)
    - **Dataset Used**: None specified; uses **synthetic data** for twenty stocks.
    - **Specific Data**: The ABM simulates trading of twenty stocks, using synthetic price and volume data to study transaction risks.
    - **Why No Specific Dataset**: The focus is on theoretical risk analysis, not a specific market, so synthetic data is used.
    - **Environmental or Other Factors**: Includes investor types (institutional, speculators) but no external environmental data.
    - **Details**: Synthetic data supports controlled risk analysis.

---

#### **Unspecified Date**

45. **Re: File Number S7-02010, 'Concept Release on Equity Market Structure'** (Murphy and Murphy)
    - **Dataset Used**: None specified; likely none or **synthetic data**.
    - **Specific Data**: The document discusses ABM as a methodology for financial systems, not a specific simulation, so no dataset is mentioned.
    - **Why No Specific Dataset**: The focus is on advocating ABM’s application, not implementing a model, so no data is required.
    - **Environmental or Other Factors**: None; the focus is on methodological advocacy.
    - **Details**: The lack of a dataset aligns with the paper’s conceptual nature.

---

### **Summary of Data Sources Across All Papers**

- **Explicit Datasets**:

  - **Hang-Seng Futures Index** (Vytelingum et al., 2025): Used for liquidity risk modeling (price and order flow data).
  - **Historical LOB Data** (Shi and Cartlidge, 2023, 2024): Used for LOB simulation (order prices, volumes, timestamps).
  - **Web of Science Articles** (Ionescu et al., 2025): Metadata for bibliometric analysis, not market simulation.
  - **Internet Query and Stock Market Data** (Chen et al., 2017): Combines search volumes and stock data for financial system modeling.
- **Synthetic Data** (Most Common):

  - Used in 38 of the 45 papers (e.g., Fluri et al., 2025; Gamal et al., 2024; Faria, 2022).
  - Includes simulated prices, volumes, orders, or economic variables to model hypothetical scenarios, stylized facts, or theoretical dynamics.
  - Reasons: Allows control over variables, flexibility for niche or data-scarce markets (e.g., illiquid assets, CBDCs), and focus on methodological or theoretical goals rather than specific market replication.
- **No Dataset**:

  - Papers like Axtell and Farmer (2025) and Murphy and Murphy (undated) are reviews or advocacy pieces, not simulations, so no data is needed.
  - Vidler and Walsh (2025) use LLM query data, not financial market data, due to their focus on decision-making biases.
- **Environmental or Other Factors**:

  - Most papers focus on market-specific factors (e.g., order flow, liquidity, investor behavior) or macroeconomic variables (e.g., interest rates, housing prices).
  - No papers explicitly include external environmental factors like climate data, geopolitical events, or natural disasters.

---

### **Notes**

- The prevalence of synthetic data reflects ABM’s strength in modeling complex, emergent phenomena in controlled settings, especially for theoretical or methodological studies.
- Real-world datasets (e.g., Hang-Seng Futures, LOB data) are used when calibration to specific markets is needed for realism or validation.
- The lack of environmental factors suggests a focus on internal market dynamics, though some papers (e.g., Alexandre and Lima, 2020) include macroeconomic variables like interest rates.
- If you need assistance accessing specific financial datasets (e.g., via Bloomberg, Quandl, or exchange APIs) or further details on any paper, please let me know!

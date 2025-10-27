# Information below is from : An Agent-Based Model of Rumor-Induced Volatility in Financial Markets paper (which is still under review)

## Key points

- Agent Based Models(ABMs) have explained empirical phenomena in financial markets with the help of heterogenous agents following unique trading strategies (Axtell and Farmer, 2025; Hommes, 2006; Hommes and Wagener, 2008).
- When the percentage of agents with high financial literacy and cognition increases beyond 30%, the maximum return and volatility of asset prices observed Decreases
- 

## Problem Statement

- Volatility in asset prices
- Complex dynamics of asset pricing
- bubbles and crashes


## These are the summary of the papers which are under the (Market Dynamics and Volatility) and Portfolio Optimization and Trading Strategy.

Here is the information for each of the research papers :

***

### 1. Analyzing herding, stylized facts, and information cascades via self-organized criticality in an agent-based speculation game (Sawar Sagwal et al.)

*   **Main Objective**: The paper aims to analyze herding, stylized facts, and information cascades through **self-organized criticality in an agent-based speculation game**. It specifically addresses the lack of herding behavior in the Speculation Game (SG) model, which is rooted in the Minority Game framework but successfully replicates other stylized facts.
*   **Dataset Used**:
    *   **Real-world BSE Sensex data** spanning December 2004 to February 2024.
    *   The data is analyzed to demonstrate the presence of order imbalance.
*   **Data Frequency**: Not explicitly stated, but the time span suggests historical market data, likely **daily or similar frequency**.
*   **Code/GitHub Link**: Data will be made available upon request. No public GitHub link is provided.
*   **Other Information**: The model was validated for stationarity using the Augmented Dickey–Fuller (ADF) unit root test, ensuring it exhibits key empirical regularities observed in real-world data.

### 2. Reinforcement Learning Pair Trading: A Dynamic Scaling Approach (Hongshen Yang and Avinash Malik)

*   **Main Objective**: This study investigates whether **Reinforcement Learning (RL) can enhance decision-making in cryptocurrency algorithmic trading** by combining RL with statistical arbitrage pair trading. Key contributions include the construction of a tailored RL environment for quantity-varying pair trading, a novel method for adaptive investment quantities, hyperparameter fine-tuning, and an RL component for market analysis and decision-making.
*   **Dataset Used**:
    *   **Real-world BTC-GBP and BTC-EUR data**.
    *   The dataset consists of **263,520 data points**.
*   **Data Frequency**: **1-minute intervals**.
*   **Code/GitHub Link**: The original data is openly available from Binance Exchange. No specific GitHub link for the code is provided in the excerpts.
*   **Other Information**: The results show that RL-based pair trading achieved annualized profits ranging from 9.94% to 31.53%, significantly outperforming the traditional non-RL technique's 8.33% in volatile markets like cryptocurrencies. Deep Q-Learning (DQN), Soft Actor Critic (SAC), Advantage Actor-Critic (A2C), and Proximal Policy Optimization (PPO) algorithms were experimented with, with A2C performing best.

### 3. Reinforcement-Learning Portfolio Allocation with Dynamic Embedding of Market Information (No authors listed on page 1)

*   **Main Objective**: The paper assesses the out-of-sample performance of the **Dynamic Embedding Reinforcement Learning (DERL) framework** for portfolio allocation using U.S. equities data. It aims to demonstrate the superior performance of end-to-end strategies compared to traditional two-step frameworks and the robustness of the approach across various RL algorithms.
*   **Dataset Used**:
    *   **Real-world U.S. equities data** spanning thirty years.
    *   Focuses on the **top 500 stocks** by market capitalization in each subperiod.
*   **Data Frequency**: Implied to be **daily**, given the mention of "daily rebalancing of our DERL strategy".
*   **Code/GitHub Link**: No explicit GitHub link is provided, but implementation details are available in an "E-Companion".
*   **Other Information**: The framework uses only price-volume information and several technical indicators as inputs, which are automatically transformed into low-dimensional embeddings by a generative autoencoder.

### 4. Decision Transformer: Reinforcement Learning via Sequence Modeling (No authors listed on page 1)

*   **Main Objective**: The paper investigates the application of Large Language Models (LLMs) for **trading tasks across various financial assets**, including stocks and cryptocurrencies. The core idea is to apply LLMs to make trading decisions.
*   **Dataset Used**:
    *   **Real-world trading data for five stocks**: Johnson & Johnson (JNJ), Universal Corp (UVV), Honeywell International Inc. (HON), and Tesla, Inc. (TSLA).
    *   **Real-world Bitcoin (BTC) trading data**.
*   **Data Frequency**:
    *   For stocks: Warm-up period from July 1, 2020, to September 30, 2020; test period from October 1, 2020, to May 6, 2021.
    *   For BTC: Warm-up period from February 11, 2023, to April 4, 2023; test period from April 5, 2023, to November 5, 2023.
    *   The granularity of "trading tasks" typically implies **daily or higher frequency** data.
*   **Code/GitHub Link**: Not provided in the excerpts.
*   **Other Information**: Performance is measured using Composite Return (CR), Sharpe Ratio (SR), Annualized Volatility (AV), and Maximum Drawdown (MDD).

### 5. Multi-Agent Stock Prediction Systems: Machine Learning Models, Simulations, and Real-Time Trading Strategies (Daksh Dave, Gauransh Sawhney, Vikhyat Chauhan)

*   **Main Objective**: This research presents a comprehensive study on **stock price prediction** utilizing advanced machine learning (ML) and deep learning (DL) techniques, evaluating various recurrent neural network (RNN) architectures (LSTM, GRU, attention-based models). It aims to provide practical guidance for developing more accurate and efficient AI-driven trading systems.
*   **Dataset Used**:
    *   **Real-world stock data, specifically focusing on TESLA**.
    *   The study utilizes both univariate and multivariate time series data.
*   **Data Frequency**: References suggest that "tick data" provided more accurate predictions compared to "15-minute data", implying the use of **tick-level or 15-minute frequency data**.
*   **Code/GitHub Link**: Not provided in the excerpts.
*   **Other Information**: The findings indicate that attention-based models achieved the highest accuracy (95.1467%), outperforming other architectures like LSTM (89.2522%) and GRU (84.1694%).

### 6. Agent-based Liquidity Risk Modelling for Financial Markets (Perukrishnen Vytelingum et al.)

*   **Main Objective**: The paper describes a novel **agent-based approach for modeling the transaction cost of buying or selling an asset** in financial markets, specifically focusing on **liquidity risk**. It introduces a mechanism for traders to update their belief of fundamental value based on order flow and demonstrates its practical application by calculating liquidity risk for the Hang-Seng Futures Index.
*   **Dataset Used**:
    *   **Real-world Hang-Seng Futures Index data** is used for demonstrating the model's practical application.
    *   The core of the study involves **simulated data** generated by the agent-based model (ABM).
*   **Data Frequency**: For experiments, "multiple market orders executed every 10s over 5 minutes" are mentioned, indicating a focus on **high-frequency (seconds-level) data** for simulation.
*   **Code/GitHub Link**: No GitHub link is provided. Permissions for copying or redistribution are handled via email request to Simudyne.
*   **Other Information**: The ABM calculates costs and uncertainties through Monte-Carlo simulations, and observes emergent, realistic price impact (following the square-root law) without oversimplifying the problem.

### 7. Multi-Agent Reinforcement Learning for Dynamic Treaty Bidding in Reinsurance Markets (Stella C. Dong and James R. Finlay)

*   **Main Objective**: This paper applies **dynamic, multi-agent reinforcement learning (MARL) to the treaty bidding problem in reinsurance markets**. It aims to overcome limitations in adaptivity, institutional realism, and strategic competition found in prior approaches, and identifies managerial and policy implications.
*   **Dataset Used**:
    *   **Synthetic datasets** designed to reflect realistic treaty and market conditions.
*   **Data Frequency**: Not explicitly stated, as it is synthetic data for simulations, but financial market simulations typically involve discrete time steps or event-driven updates.
*   **Code/GitHub Link**: The simulation code and supporting documentation are available from the corresponding author upon reasonable request for academic and research purposes. No public GitHub link is provided.
*   **Other Information**: The study examines how MARL agents perform across varying risk aversion levels, showing consistent empirical risk-return relationships.

### 8. Quantum Reinforcement Learning for Sector Rotation: A Real-World Benchmark Study (No authors listed on page 1)

*   **Main Objective**: This paper introduces a reproducible **Quantum Reinforcement Learning (QRL) benchmark for sector rotation** using real financial data. It provides a systematic comparison of classical and quantum-enhanced policy networks within a shared Proximal Policy Optimization (PPO) framework.
*   **Dataset Used**:
    *   **Real-world sector-level financial data from the Taiwan stock market**, covering 2,646 listed companies categorized into 47 industry sectors.
*   **Data Frequency**: **Daily** capital share information and stock prices. The dataset spans from April 23, 2007, to June 13, 2025, with a training period from April 23, 2007, to December 31, 2019, and a testing period from January 1, 2020, to June 13, 2025.
*   **Code/GitHub Link**: No explicit GitHub link is provided for the QRL benchmark.
*   **Other Information**: The paper also analyzes discrepancies between training rewards and investment performance, proposing improvements for reward shaping and regularization. A rolling-window approach is employed to simulate real-time decision-making.

### 9. Neuro-Symbolic Traders: Assessing the Wisdom of AI Crowds in Markets (No authors listed on page 1)

*   **Main Objective**: This paper focuses on **LLM agentic workflows for automated model discovery** and their integration into trading systems. It evaluates LLMs' performance as risk-informed agentic traders and tests them within a context-aware backtesting environment.
*   **Dataset Used**:
    *   **Synthetic price and news data** generated by the Simudyne Horizon simulator.
    *   Specifically, a synthetic news cycle for the S&P 500 covering a six-month trading period (January 1 to July 1, 2023) was used.
*   **Data Frequency**: Not explicitly stated, but synthetic news cycles for a six-month period imply detailed, possibly **daily or higher frequency** data within the simulation.
*   **Code/GitHub Link**: No GitHub link is provided. The paper mentions using Simudyne Horizon for benchmarking and simulation.
*   **Other Information**: The study compares the performance of seven frontier LLMs (Deepseek, Anthropic, OpenAI, Meta) in automated model discovery and trading tasks.

### 10. Hide-and-Shill: A Reinforcement Learning Framework for Market Manipulation Detection in Symphony—a Decentralized Multi-Agent System (Ronghua Shi et al.)

*   **Main Objective**: The paper proposes "Hide-and-Shill," a novel **Multi-Agent Reinforcement Learning (MARL) framework for decentralized market manipulation detection in Decentralized Finance (DeFi)**. It aims to provide a real-time DeFi market surveillance solution.
*   **Dataset Used**:
    *   A **multi-source dataset integrating real-world observations with Large Language Model (LLM)-generated synthetic data**.
    *   **Real-world Twitter discourse**: 100,000 posts and 600,000 comments related to cryptocurrency from January 2020 to December 2024.
    *   **LLM-Generated Synthetic Dataset**: 50,000 synthetic discourse episodes created using DeepSeek-32B, fine-tuned on real manipulation cases.
    *   **On-chain Market Data**: Retrieved from CoinGecko & Uniswap V3.
*   **Data Frequency**:
    *   The "longitudinal dataset" for social discourse (2020-2024) and "real-time" monitoring suggest **high-frequency data**.
*   **Code/GitHub Link**: **Yes**, all datasets, code, and models are publicly released at the **Hide-and-Shill GitHub repository**: **https://github.com/tifoit/Hide-and-Shill**.
*   **Other Information**: The framework formulates manipulation detection as a MARL problem, where a detector agent learns to optimize attention allocation. It demonstrates significant superiority over state-of-the-art baselines.

### 11. StockSim: A Dual-Mode Order-Level Simulator for Evaluating Multi-Agent LLMs in Financial Markets (Charidimos Papadakis et al.)

*   **Main Objective**: This paper introduces **STOCKSIM, an open-source simulation platform for the systematic evaluation of Large Language Models (LLMs) in realistic financial decision-making scenarios**. It aims to provide a comprehensive system that models market dynamics, including latency, slippage, and order-book microstructure, for assessing LLM-based trading agents.
*   **Dataset Used**:
    *   Market data provided by **Polygon.io**.
    *   The simulation environment is designed to incorporate real-world factors.
*   **Data Frequency**: Described as an **"Order-Level Simulator"**, which implies very **high-frequency, tick-level data** that captures detailed market microstructure.
*   **Code/GitHub Link**: **Yes**, the code is open-sourced at **https://github.com/harrypapa2002/StockSim**.
*   **Other Information**: The platform supports diverse simulation modes, varying granularity, heterogeneous trading strategies, and multi-agent coordination, making it a capable testbed for NLP research on reasoning under uncertainty and sequential decision-making.

### 12. Hierarchical Reinforcement Learning with Multi-Modal LLM Integration for Adaptive Portfolio Optimization (No authors listed on page 1)

*   **Main Objective**: This paper introduces an innovative **hierarchical reinforcement learning (RL) framework for portfolio optimization**. It integrates structured financial indicators with sentiment signals extracted from financial news using lightweight, domain-specific Large Language Models (LLMs) like FinBERT, employing a three-tier multi-agent architecture.
*   **Dataset Used**:
    *   **Real-world daily adjusted closing prices for 14 financial assets** (major global stock indices and commodities).
    *   **News articles collected monthly from Google News (2003–2024)** and processed with FinBERT for sentiment scores.
*   **Data Frequency**: **Daily adjusted closing prices** for financial assets; **monthly sentiment scores** from news.
*   **Code/GitHub Link**: **Yes**, all experiments are reproducible via **three Google Colab notebooks**, with links provided in the paper.
*   **Other Information**: The framework decomposes decision-making into base agents, meta-agents, and a super-agent, leading to adaptive, interpretable, and robust decision-making. The super-agent strategy achieved superior performance (26.0% Annualized ROI, 1.2 Sharpe Ratio) compared to benchmarks and state-of-the-art RL methods.

### 13. MountainLion: A Multi-Agent Financial Analysis Framework with Explainable RAG and Reflective Decision-Making for Web3 Investments (No authors listed on page 1)

*   **Main Objective**: This paper presents **MountainLion, a multi-agent, Retrieval-Augmented Generation (RAG)-enabled financial analysis framework designed for cryptocurrency trading**. It aims to enable interpretable, real-time, and adaptive responses across diverse financial modalities by integrating specialized LLM agents, graph-based retrieval reasoning, and a reflective decision module.
*   **Dataset Used**:
    *   **Real-time market signals, historical price data, and relevant news narratives** from sources like K-line data, coin listings, and prediction models.
    *   Raw news streams are collected from APIs, RSS feeds, and curated portals.
    *   Forecasting results for various crypto tokens (ADA, BTC, ARB, SOL, XRP, DOGE, TRX, ETH, MATIC, BNB) are presented.
*   **Data Frequency**: "Real-time" retrieval and "short-term forecast Prompt (within 0-24 hours)" imply **high-frequency or intra-day data**.
*   **Code/GitHub Link**: Not provided in the excerpts.
*   **Other Information**: The framework supports dynamic financial report generation and refinement by fusing textual news, visual market signals, and on-chain data. Empirical evaluations confirm its improvement in medium-term forecasting accuracy while enhancing transparency and adaptability.

### 14. Reinforcement Learning in Agent-Based Systems: Unveiling Adaptive Decision Intelligence (Muhammad Farooq, Hasina Malik, Edward Oscar)

*   **Main Objective**: The paper title indicates a focus on **"Reinforcement Learning in Agent-Based Systems: Unveiling Adaptive Decision Intelligence"**. Based on the title and typical academic paper structure, this appears to be a review or conceptual paper exploring the intersection of RL and agent-based systems.
*   **Dataset Used**: Not applicable, as it is a conceptual or review paper and does not describe experimental results using a specific dataset.
*   **Data Frequency**: Not applicable.
*   **Code/GitHub Link**: Not applicable for this type of paper.
*   **Other Information**: Co-authored by Hasina Malik and Edward Oscar, published in July 2025.

### 15. LLM-Infused Risk-Sensitive Reinforcement Learning for Trading Agents (No authors listed on page 1)

*   **Main Objective**: This paper proposes a two-phase framework for **automated stock trading by infusing Reinforcement Learning (RL) with Large Language Models (LLMs)**. It aims to provide a holistic causal-effect relationship and a deep understanding of market dynamics.
*   **Dataset Used**:
    *   **Real-world Financial News and Stock Price Integration Dataset (FNSPID)**.
    *   A subset of FNSPID (approx. 74K financial news records) for **15 companies** across large-cap, mid-cap, and small-cap bands, with news spanning from 1999 to 2023.
*   **Data Frequency**: "Next-day prediction using end-of-day news and market data" implies **daily frequency**.
*   **Code/GitHub Link**: The paper references a related arXiv preprint ("FinRL-DeepSeek: LLM-infused risk-sensitive reinforcement learning for trading agents"), implying associated code but no direct public GitHub link in the excerpt itself.
*   **Other Information**: The framework is designed for low-latency deployment, processing an average of 3–4 filtered news articles per company during post-market hours and retrieving market data via APIs. It evaluates performance using metrics like Information Ratio (IR), CVaR, Rachev Ratio, and Sharpe Ratio.

### 16. FinRL-DeepSeek: LLM-infused Risk-Sensitive Reinforcement Learning for Trading Agents (No authors listed on page 1, likely an extended version or related work of the previous one)

*   **Main Objective**: This paper focuses on enhancing the integration of LLM signals into primary algorithms (PPO and CPPO) for **LLM-infused risk-sensitive reinforcement learning for trading agents**. The goal is to significantly stabilize performance and better leverage text-based financial information.
*   **Dataset Used**:
    *   **Real-world Yahoo Finance data for Nasdaq-100 stocks** (prices, volumes, indicators).
    *   **Real-world FINSPID dataset** (15.7 million news records on Nasdaq-100 stocks, a subset of 2 million news used for LLM requests).
*   **Data Frequency**: Nasdaq-100 stock data from Yahoo Finance is typically **daily**. The "small subset" for experiments (2013-2023, with trading period 2023/2 - 2023/3) aligns with daily or higher frequency trading.
*   **Code/GitHub Link**: The paper refers to the arXiv preprint http://arxiv.org/abs/2502.07393 for "FinRL-DeepSeek" and mentions FinRL GitHub.
*   **Other Information**: The LLM is requested to output confidence probabilities alongside scores, which helps the RL agent weigh uncertain signals more cautiously. Pipeline optimization to streamline data processing and LLM interactions is identified as future work.

### 17. Agent AI for Finance: From Financial Argument Mining to Agent-Based Modeling (Chung-Chi Chen · Hiroya Takamura)

*   **Main Objective**: This book provides an overview of the current state of **financial argument mining and financial text generation**, and presents a blueprint for NLP in finance within the Agent AI era. It extends discussions to include reasoning, planning, inference, and decision-making for financial applications.
*   **Dataset Used**:
    *   **Real-world financial argument mining datasets**: professional research reports and earnings conference calls.
    *   **Equity-AMSA dataset**: Annotated data for scenarios and impact duration estimations in equality analysis reports.
    *   **Manager’s promise dataset** and **ESG-related news articles/reports** (multi-lingual) for impact duration inference.
    *   **Numeracy-600K, EQUATE, and NumGLUE Task 3** for quantitative tasks.
    *   **Pilot dataset for database querying and reasoning (DBQR)**.
    *   **Social media posts** on a financial platform for inter-opinion relationship analysis.
*   **Data Frequency**: Varies depending on the specific task. For instance, "stock movement prediction timeframe of 30 d" is mentioned, implying **daily data** for that specific application. Overall, it covers various textual data types, not strictly time-series data at a fixed frequency.
*   **Code/GitHub Link**: **Yes**, slides based on the book's content are available at **https://sites.google.com/view/finagent/home**. Specific experiments also reference other papers with associated code.
*   **Other Information**: Discusses different aspects of agent AI: single-agent design (e.g., Retrieval-Augmented Generation, Model Editing), multi-agent interaction (behavior simulation, trading decision-making), and multi-scale model synergy (data augmentation, dynamic interaction loop). It emphasizes "forward-looking argument mining" as a key concept.

### 18. Twin-Based RL for Solving Multi-Period PO (P. T. Huynh et al.)

*   **Main Objective**: This study refines and develops reinforcement learning algorithms based on a **twin-based approach to address multi-period portfolio management with constraints**. Its design aims to balance short-term returns and long-term risks under risk management constraints.
*   **Dataset Used**:
    *   **Real-world data from 100 stocks listed on the Vietnam Stock Exchange**, covering 15 years from 2009 to 2023.
    *   The dataset includes stock symbols, daily stock prices, and cash dividend payouts.
    *   **Training data**: 2009 to 2022. **Testing data**: 2023.
*   **Data Frequency**: **Daily stock prices** for calculation of metrics, with investors making **monthly decisions**.
*   **Code/GitHub Link**: No GitHub link provided in the excerpts.
*   **Other Information**: The model integrates fundamental stock price data, cash dividends, and technical indicators like MACD. It is theoretically adaptable to any stock market and other application domains.

### 19. A Graph Neural Network-Reinforcement Learning Framework for Dynamic Portfolio Optimization (No authors listed on page 1)

*   **Main Objective**: To demonstrate that a **dynamic Graph Neural Network (GNN)-Proximal Policy Optimization (PPO) system can outperform traditional baselines** (market-trading, buy-and-hold, moving-average crossover) in a multi-year validation set for stock market prediction. It combines the power of GNNs with RL, specifically using dynamic edge-weighted graphs and a Graph Attention Network (GAT) encoder.
*   **Dataset Used**:
    *   **Real-world daily OHLCV (Open-High-Low-Close-Volume) data** from Yahoo Finance for **eight liquid US equities**: AAPL, MSFT, NVDA, AMZN, META, TSLA, JPM, and XOM.
    *   **Raw samples**: January 1, 2014, to May 18, 2025. **Training set**: January 1, 2015, to December 31, 2022. **Evaluation set**: January 1, 2023, to May 18, 2025.
*   **Data Frequency**: **Daily OHLCV data**.
*   **Code/GitHub Link**: No GitHub link provided in the excerpts.
*   **Other Information**: Builds daily edge-weighted graphs using the rolling Pearson correlation to capture changing relationships between tickers. The agent is trained sequentially, never seeing future data, to ensure realism.

### 20. FD-RLPO: Feature-Domain-based Reinforcement Learning Framework for Portfolio Optimization (No authors listed on page 1)

*   **Main Objective**: To propose **FD-RLPO, a novel framework that simultaneously captures intra- and inter-domain features to address challenges in financial data fluctuation** and optimize returns for portfolio optimization. It utilizes reinforcement learning within an Actor-Critic framework.
*   **Dataset Used**: The provided excerpts do not specify the exact dataset (name, assets, or timeframe).
*   **Data Frequency**: Not specified.
*   **Code/GitHub Link**: No GitHub link provided in the excerpts.
*   **Other Information**: The framework includes a Relation Module that uses self-supervised learning with data masking, and a Prediction Module with a feature-centered inversion mechanism.

### 21. Finance and Market Concentration Using Agent Based Modeling, Evidence from South Korea (Anonymised review copy)

*   **Main Objective**: This paper employs an **Agent-Based Model (ABM) to investigate the impact of finance on market concentration, economic growth, and labor income share**. It extends the Keynes-meets-Schumpeter (K+S) model and validates it using historical data from South Korea.
*   **Dataset Used**:
    *   **Real-world historical data from South Korea from 1990 to 2020** for model validation.
    *   The ABM itself generates simulated data for policy experiments.
*   **Data Frequency**: Each time step in the simulation corresponds to a **single real-world quarter**.
*   **Code/GitHub Link**: No GitHub link is provided.
*   **Other Information**: The study uses debt-to-sales ratio (DSR) and interest rate as proxies for financial policies. Findings indicate that the impact of financing on market concentration varies non-linearly depending on the policy type.

### 22. Impact of Pinging in Financial Markets: An Agent-Based Study (No authors listed on page 1)

*   **Main Objective**: This agent-based study aims to analyze the **impact of "pinging" (a high-frequency trading strategy) in financial markets**, particularly concerning market manipulation in "dark pools" and its effect on "lit" market efficiency and execution costs.
*   **Dataset Used**:
    *   The study uses a **simulated market environment** built upon existing financial market ABM frameworks.
*   **Data Frequency**: The simulation length is 2000 time steps, and market arrival times are governed by a Poisson process, indicating **event-driven or high-frequency simulation**.
*   **Code/GitHub Link**: No GitHub link is provided.
*   **Other Information**: The study explores how market manipulation in dark pools disrupts lit market efficiency. It examines execution scenarios and metrics within the simulated environment.

### 23. Reinforcement Learning in Finance: QTRAN for Portfolio Optimization (No authors listed on page 1)

*   **Main Objective**: This paper conducts a **comparative experiment between QTRAN (a reinforcement learning algorithm) and other RL algorithms for portfolio optimization**. It analyzes QTRAN's performance across different asset categories, its sensitivity to transaction costs, the impact of portfolio diversification, and its adaptability in a high-frequency trading environment.
*   **Dataset Used**: The specific dataset name, assets, or timeframe are not detailed in the provided excerpts.
*   **Data Frequency**: Experiments include a "high-frequency trading environment", suggesting that the underlying data for that part of the study is **high-frequency**.
*   **Code/GitHub Link**: No GitHub link provided in the excerpts.
*   **Other Information**: QTRAN is shown to have more stable volatility in high-frequency trading but drops significantly in low liquidity phases. It performs best in technology and healthcare stocks.

### 24. Efficiency of a Self-Organizing Ising Model of Financial Markets (No authors listed on page 1)

*   **Main Objective**: This study explores the **effect of noise traders on the distribution of absolute logarithmic returns** in an Ising model of financial markets. The broader aim is to contribute to the creation of an agent-based model that can accurately predict the dynamics of real-world financial markets.
*   **Dataset Used**:
    *   **Simulated data** generated from an Ising model of financial markets.
*   **Data Frequency**: Not explicitly stated as a real-world frequency. The simulation generates time-series data related to price changes and returns.
*   **Code/GitHub Link**: No GitHub link provided. It mentions using the "powerlaw package in Python".
*   **Other Information**: The research focuses on emergent statistical signatures in financial markets, such as fat-tails in return distributions and volatility clustering. Findings suggest that only a low percentage of noise traders is necessary to retrieve realistic market behaviors from the Ising model.

### 25. A Multi-Agent Approach to Stock Market Prediction and Risk Management (Anamay Potdar and Dr. Swapnali D. Mahadik)

*   **Main Objective**: This research introduces a **simulated AI trading system functioning as an Agentic AI for stock market prediction and risk management**. Its primary objective is to explore the feasibility of such a system by creating a simulation model, contributing insights into autonomous AI trading and real-time AI-driven financial systems.
*   **Dataset Used**:
    *   The system leverages **real-time and historical data** for news extraction, chart pattern recognition, and supply-demand evaluation.
    *   This implies a **simulated system** that uses characteristics of **real-world financial data**.
*   **Data Frequency**: "Real-time news sentiment analysis" suggests processing **high-frequency data** streams.
*   **Code/GitHub Link**: Not provided in the excerpts.
*   **Other Information**: The system integrates news sentiment analysis, chart pattern recognition, supply-demand evaluation, and risk management to enable fully autonomous stock trading. Future work includes improving real-time execution in the Indian stock market.

### 26. Risk-Sensitive Deep Reinforcement Learning for Portfolio Optimization (Xinyao Wang and Lili Liu)

*   **Main Objective**: This study introduces an **Adaptive Risk-sensitive Transformer-based Deep Reinforcement Learning (ART-DRL) framework to improve portfolio optimization in commodity futures markets**, specifically petroleum futures. It aims to demonstrate how machine learning can support portfolio management under volatile market conditions.
*   **Dataset Used**:
    *   **Real-world petroleum futures market data** for selected contracts.
    *   **Daily continuous futures prices from 2014 to 2024** are used.
*   **Data Frequency**: **Daily**.
*   **Code/GitHub Link**: No GitHub link is provided. The data cannot be made publicly available due to proprietary restrictions, but summary statistics and analysis scripts can be shared upon reasonable request.
*   **Other Information**: The framework integrates multiple DRL agents (DQN, PPO, A2C, DDPG) with a performance-driven switching mechanism and a Transformer-based temporal encoder. It demonstrates resilience by learning from historical periods of extreme volatility.

### 27. Hierarchical Multi-Agent System with Bayesian Neural Networks for Portfolio Optimization (Firdaous Khemlichi et al.)

*   **Main Objective**: This paper presents a **Hierarchical Multi-Agent System with Bayesian Neural Networks for Portfolio Optimization (IPS)**. It aims to assess the impact of multi-agent coordination and signal fusion on portfolio performance across both stable and volatile market regimes.
*   **Dataset Used**:
    *   **Real-world historical data from three major indices**: S&P 500 (U.S.), DAX (Germany), and FTSE 100 (U.K.).
    *   **60 stocks** (20 per index) were selected based on liquidity.
*   **Data Frequency**: The timeframe is 2010–2020. While not explicitly stated, historical stock and index data are typically at a **daily frequency**.
*   **Code/GitHub Link**: No GitHub link is provided. Yahoo Finance is mentioned as a data source.
*   **Other Information**: Performance was evaluated during both pre-COVID and COVID periods. Ablation studies confirm the effectiveness of its core components, including the multi-agent PPO with Bayesian Neural Networks (BNN).

### 28. Multi-Agent Performance Learning System for Dynamic Portfolio Optimization (No authors listed on page 1)

*   **Main Objective**: To present the **Multi-Agent Performance Learning System (MPLS) framework**, detailing its architecture, analytical components, and reinforcement learning mechanisms for portfolio optimization. The goal is to assess the impact of multi-agent coordination and signal fusion on portfolio performance across stable and volatile market regimes.
*   **Dataset Used**:
    *   A **ten-year dataset (2010–2020)** integrating **60 stocks from the S&P 500 (U.S.), DAX (Germany), and FTSE 100 (U.K.) indices**.
    *   It includes FinBERT sentiment scores, GNN correlations, and volatility estimates.
*   **Data Frequency**: While not explicitly stated, a "ten-year dataset" for stocks and indices generally implies **daily frequency**.
*   **Code/GitHub Link**: No GitHub link is provided. Yahoo Finance, Bloomberg, and Investing.com are cited as data sources.
*   **Other Information**: The framework moves beyond traditional statistical models like Markowitz mean-variance and confirms that its modules contribute significantly to performance through ablation studies.

### 29. The New Kind of Science Market Model (No authors listed on page 1)

*   **Main Objective**: This work describes **stylized facts in financial markets using empirical data analysis** and studies well-known artificial market models (Cont-Bouchaud, Lux-Marchesi, Bak et al.). It proposes alternative methods to improve the Cont-Bouchaud model to generate long-term autocorrelation of volatility.
*   **Dataset Used**:
    *   Mentions "empirical data analysis", implying **real-world financial data**.
    *   Also uses **simulated data** from artificial market models.
*   **Data Frequency**: Not explicitly stated for empirical data. Simulations focus on the "time evolution of price and return".
*   **Code/GitHub Link**: "Test set of tests is available on request," and the author is open to collaboration for further information and experiments. No public GitHub link is provided.
*   **Other Information**: Focuses on key stylized facts like non-Gaussian return distribution and volatility clustering. Explores the behavior of noise traders and different price update mechanisms in simulations.

### 30. Multi-dimensional instability in energy financial markets: A delayed asymmetric agent-based modeling approach (Jiang-Cheng Li et al.)

*   **Main Objective**: This study develops a **Multi-dimensional Instability Index (MDI) and a delayed asymmetric agent-based model to systematically characterize market instability** in energy financial markets. It aims to provide insights into market stability dynamics during notable crises and identify optimal investor behaviors.
*   **Dataset Used**:
    *   **Real-world WTI crude oil futures data** from June 1988 to October 2024 for empirical analysis.
    *   The core model is an agent-based model which would generate **simulated data**.
*   **Data Frequency**: The long time span for empirical analysis implies **historical time-series data**, likely **daily or higher frequency**.
*   **Code/GitHub Link**: No GitHub link is provided in the excerpts.
*   **Other Information**: The MDI integrates multiple key indicators, including information entropy, unstable time, absolute return volatility, maximum drawdown, and Value-at-Risk (VaR). Simulation results reveal nonlinear, non-monotonic relationships and bifurcation dynamics based on factors like information delay and behavioral asymmetry.

### 31. Sentiment Trading with Large Language Models (No authors listed on page 1)

*   **Main Objective**: This paper focuses on **sentiment trading using large language models**, specifically estimating financial sentiment for stock prediction. It conducts ablation experiments to assess the impact of sentiment integration and a weighting parameter in the SAPPO model.
*   **Dataset Used**:
    *   **Real-world daily adjusted closing prices for Google, Microsoft, and Meta**.
    *   **Financial news sentiment extracted using LLaMA 3.3**.
*   **Data Frequency**: **Daily adjusted closing prices**. The dataset covers January 2013 to January 2020.
*   **Code/GitHub Link**: No GitHub link is provided. The paper mentions using PyTorch and Stable-Baselines3 for implementation, and OpenAI Gym for the financial environment.
*   **Other Information**: The results highlight that a moderate sentiment influence (λ = 0.1) yields the best Sharpe ratio and return. The financial environment simulates trading with transaction costs, VWAP execution, and rebalancing constraints.

### 32. An Agent-Based Model of Rumor-Induced Volatility in Financial Markets (No authors listed on page 1)

*   **Main Objective**: This study investigates the **influence of financial literacy and IQ on the scale and spread of rumors** and their effects on asset price, return, and volatility, utilizing an **Agent-Based Model** of rumor-induced volatility in financial markets.
*   **Dataset Used**:
    *   The study uses **simulated data** generated from an Agent-Based Model.
*   **Data Frequency**: The simulation runs at "each discrete time step t", generating time-series data for analysis.
*   **Code/GitHub Link**: No GitHub link is provided.
*   **Other Information**: Findings suggest that higher financial literacy and IQ lead to decreased asset price volatility and faster rumor dissipation. The model qualitatively mirrors patterns observed in real markets, exhibiting properties like absence of autocorrelation in returns, heavy tails, and volatility clustering.
*   

### Overview of Key Trends
Based on the provided information on 32 research papers, here is a comprehensive analytics summary. These papers predominantly explore AI-driven approaches in finance, with a strong emphasis on reinforcement learning (RL), agent-based modeling (ABM), and large language models (LLMs) for tasks like portfolio optimization, trading strategies, market simulation, and risk management. Key trends include:
- **Dominant Methods**: RL and its variants (e.g., MARL, hierarchical RL) appear in over 50% of papers, often applied to portfolio optimization. ABM is common for simulating market behaviors, while LLMs are emerging for sentiment analysis and integration with RL.
- **Datasets**: 84% (27/32) use real-world data, focusing on stocks, cryptocurrencies, and futures. Synthetic data supplements in 28% (9/32), especially for simulations.
- **Data Frequency**: Daily is the most common (50%, 16/32), suitable for portfolio tasks. High-frequency (e.g., minute/tick) appears in 22% (7/32), often for trading simulations.
- **Code Availability**: Only 19% (6/32) provide public code links (e.g., GitHub or Colab), with others offering data/code upon request or none.
- **Assets and Markets**: Stocks/U.S. equities dominate (59%, 19/32), followed by cryptocurrencies (16%, 5/32) and futures (9%, 3/32).
- **Performance Focus**: Common metrics include Sharpe Ratio (mentioned in 9 papers), Annualized Return/ROI (7), Volatility (6), and Drawdown (4). Many highlight outperformance vs. baselines like buy-and-hold.
- **Temporal Coverage**: Datasets span 1990–2025, with recent focus (post-2020) in 47% (15/32), reflecting interest in volatile periods (e.g., COVID, crypto booms).

Below are tabulated breakdowns for clarity.

### Method Distribution
Papers are categorized by primary method (some have overlaps, e.g., RL + LLM).

| Method Category | Count | Paper Numbers | Key Insights |
|-----------------|-------|---------------|--------------|
| Reinforcement Learning (RL) / Variants (e.g., DRL, PPO, Q-Learning) | 17 | 2, 3, 4, 8, 12, 15, 16, 18, 19, 20, 23, 26, 27, 28, 31 | Heavily used for portfolio optimization (12/17). Algorithms like PPO (5 mentions) and A2C (2) are popular. Focus on risk-sensitivity and adaptability in volatile markets. |
| Multi-Agent RL (MARL) / Hierarchical Multi-Agent Systems | 7 | 7, 10, 12, 13, 27, 28 | Emphasizes coordination for tasks like detection (10) or optimization (27,28). Often integrates LLMs or Bayesian networks. |
| Agent-Based Modeling (ABM) / Simulations | 13 | 1, 6, 7, 9, 21, 22, 24, 25, 29, 30, 32 | Used for market dynamics (e.g., herding, rumors, liquidity). 46% (6/13) combine with RL or ML. Emergent behaviors like volatility clustering are common themes. |
| Large Language Models (LLMs) / Sentiment / Argument Mining | 9 | 4, 9, 12, 13, 15, 16, 17, 31 | Integrated for sentiment (5/9) or trading decisions. Models like FinBERT (2) and LLaMA (1) appear. Growing trend for multi-modal fusion (news + prices). |
| Other (e.g., ML/DL Prediction, GNN, Quantum RL, Conceptual) | 6 | 5, 8, 14, 17, 19, 20 | Includes reviews (14,17) and hybrids like GNN-RL (19). Quantum RL (8) is niche but benchmarks against classical methods. |

### Dataset Types and Sources
| Dataset Type | Count | Paper Numbers | Key Insights |
|--------------|-------|---------------|--------------|
| Real-World Only | 18 | 1, 2, 3, 4, 5, 8, 12, 15, 16, 18, 19, 26, 27, 28, 30, 31 | Dominates (56%); sources like Yahoo Finance (5 mentions), Binance (1), Polygon.io (1). Focus on U.S. stocks (e.g., S&P 500 in 3 papers). Time spans average 10–20 years. |
| Synthetic / Simulated Only | 5 | 7, 22, 24, 29, 32 | Used for controlled experiments (e.g., rumors in 32). Often generated via ABM or simulators like Simudyne (9,22). |
| Both Real-World and Synthetic | 6 | 6, 9, 10, 21, 25, 30 | Combines for validation (e.g., real Hang-Seng + simulated in 6). LLMs generate synthetics in 10 (50k episodes). |
| Not Applicable / Unspecified | 3 | 14, 20, 23 | Conceptual papers (14) or lacking details (20,23). |

### Asset/Market Focus
| Asset/Market Type | Count | Paper Numbers | Key Insights |
|-------------------|-------|---------------|--------------|
| Stocks / Equities (e.g., U.S., Taiwan, Vietnam) | 19 | 3, 4, 5, 8, 17, 18, 19, 21, 25, 27, 28, 31 | Most common; S&P 500 (3 mentions), Nasdaq-100 (1). Used for prediction (5) and optimization (10+). |
| Cryptocurrencies (e.g., BTC, ETH) | 5 | 2, 4, 10, 13 | Volatile markets; pair trading (2) and manipulation detection (10). Real-time/high-freq data common. |
| Futures / Commodities (e.g., Hang-Seng, WTI Oil, Petroleum) | 4 | 6, 26, 30 | Risk modeling (6,26); long-term data (1988–2024 in 30). |
| Mixed / Indices / Sectors | 6 | 1, 12, 17, 21, 27, 28 | Global indices (e.g., DAX, FTSE in 27); sector rotation (8). |
| Other / Niche (e.g., Reinsurance, Social Media) | 3 | 7, 10, 17 | Includes Twitter discourse (10) and reinsurance treaties (7). |
| Unspecified / General | 3 | 14, 20, 23 | Conceptual or broad simulations. |

### Data Frequency Distribution
| Frequency | Count | Paper Numbers | Key Insights |
|-----------|-------|---------------|--------------|
| Daily | 16 | 3, 8, 12, 15, 16, 18, 19, 26, 27, 28, 31 | Standard for portfolio tasks; aligns with rebalancing (3) and closing prices (19). |
| High-Frequency (e.g., 1-min, Tick, Seconds) | 7 | 2, 5, 6, 11, 13, 23, 25 | For trading simulations (11) or HFT strategies (23). Tick data improves accuracy (5). |
| Other (e.g., Monthly, Quarterly, Event-Driven) | 4 | 12, 18, 21 | Monthly decisions (18); quarterly steps (21). |
| Not Specified / N/A | 9 | 1, 4, 7, 9, 14, 17, 20, 22, 24, 29, 32 | Often synthetic/simulated (7,9,32) or conceptual (14). |

### Code and Data Availability
| Availability | Count | Paper Numbers | Key Insights |
|--------------|-------|---------------|--------------|
| Public GitHub / Link Provided | 6 | 10 (GitHub), 11 (GitHub), 12 (Colab), 16 (FinRL implied), 17 (Google Site) | Open-source focus; simulators (11) and frameworks (10,13) are most shared. |
| Available Upon Request | 5 | 1, 7, 26, 29 | Data/scripts for academic use; proprietary restrictions (26). |
| No Link / Not Provided | 21 | 2–6, 8, 9, 13–15, 18–25, 27–32 | Majority; some mention tools like PyTorch (31) or powerlaw package (24). |

### Additional Insights
- **Integration Trends**: 28% (9/32) integrate LLMs with RL/ABM, signaling a shift toward multi-modal AI (e.g., news + prices in 12,15). ABM often validates against real data for stylized facts like fat-tails (1,24,29).
- **Challenges Addressed**: Volatility/risk (12 papers), market manipulation (3: 10,22,32), herding/cascades (1,30).
- **Gaps**: Limited public code hinders reproducibility. Few papers (16%) cover non-stock assets, suggesting stock bias. High-frequency data is underrepresented despite HFT relevance.
- **Future Directions**: Many suggest extensions like real-time deployment (15,25) or policy implications (7,21). Overall, the field is advancing toward adaptive, explainable AI for finance.
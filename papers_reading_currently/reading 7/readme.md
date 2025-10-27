Technical Docs for understanding the paper : https://docs.google.com/document/d/1U6fqyyOQ3KQnJ6L6v-yM-AMTZhJcRCv68-IRPBiIejM/edit?usp=sharing


The appendix of the research paper provides comprehensive supplementary materials, including details on data processing, model implementation, extensive experimental setups, full results tables, ablation studies on core design choices, and sensitivity analyses.

### I. Overview of Appendix Content

The appendix is structured to detail the methodological choices and full experimental outcomes:

1.  **Related Work (Appendix A):** Discusses time series tokenization methods and compares Kronos against general-purpose and financial Time Series Foundation Models (TSFMs).
2.  **Dataset Details (Appendix B):** Describes the data preprocessing and cleaning pipeline applied to the large-scale financial K-line dataset, including handling missing values and filtering low-quality segments.
3.  **Implementation Details (Appendix C):** Provides specifics on input preprocessing (z-score normalization and clipping), model architecture (temporal embeddings, tokenizer configuration, Transformer block architecture), and hyperparameter settings for training and inference.
4.  **Experimental Design and Implementation (Appendix D):** Outlines the five quantitative finance tasks (forecasting, generation, simulation), defines the evaluation metrics, and details the configurations for all 25 baseline models.
5.  **Additional Results (Appendix E):** Contains the sensitivity analysis for inference hyperparameters and an ablation study on the tokenizer architecture.
6.  **Full Experiment Results (Appendix F):** Presents the complete results tables for all forecasting, generation, and investment simulation tasks, including visualizations.
7.  **Forecast Showcases (Appendix G):** Provides visualizations comparing Kronos's forecasts against baselines for key features like Close Price and Volume.
8.  **Discussion (Appendix H):** Addresses critical questions regarding the rationale for using K-line data (Q1), the effectiveness of the tokenizer (Q2), and the analysis of subtoken factorization (Q3).

### II. Ablation Studies Performed

The authors performed several ablation studies to validate the core design choices of Kronos, focusing on the discrete, sequential modeling paradigm, vocabulary size, and tokenizer architecture.

| Ablation Focus | Study Goal | Key Variants Compared |
| :--- | :--- | :--- |
| **Modeling Paradigms** (Q1) | To show the effectiveness of the discrete, sequential approach over continuous modeling and parallel prediction. | **Direct-AR:** Continuous prediction space using Mean Squared Error (MSE) regression. **Prob-AR:** Continuous prediction space using Negative Log-Likelihood (NLL) with a Student-t mixture distribution. **Kronos-Parallel:** Discrete space, but predicts coarse and fine subtokens concurrently instead of sequentially. |
| **Impact of Vocabulary Size** (Q2) | To determine how quantization precision affects reconstruction quality and downstream forecasting accuracy. | Vocabulary sizes ranging from $2^{14}$ to $2^{20}$ were tested [45, Figure 6]. |
| **Tokenizer Architecture** (Appendix E) | To validate the choice of a Transformer-based autoencoder with hierarchical loss. | **Transformer w/ Standard Loss:** Transformer-based tokenizer using a non-hierarchical reconstruction loss. **CNN-based:** A CNN-based autoencoder with comparable parameter count. |
| **Test-Time Scaling** (Appendix D/E) | To show how ensembling predictions from multiple stochastic samples improves accuracy. | Varied the number of inference samples ($N$) from 1 to 20 (log scale) [47, Figure 7]. |
| **Subtoken Factorization** (Q3/Appendix H) | To analyze the trade-off between reducing vocabulary parameters and increasing inference latency by factoring the token into $n$ parts. | Factorization splits $n$ = 1 (No Split), $n$ = 2 (Ours), $n$ = 4, and $n$ = 5 were analyzed based on the Kronosbase architecture. |

### III. Published Results of Ablation Studies

The ablation studies demonstrated the superiority of Kronos's design choices:

*   **Modeling Paradigms:** The discrete-space models significantly **outperformed the continuous alternatives** (Direct-AR and Prob-AR) across forecasting tasks. Furthermore, **Kronossmall** outperformed **Kronos-Parallel**, demonstrating the importance of the sequential coarse-to-fine subtoken prediction mechanism for modeling subtoken dependencies.
*   **Vocabulary Size:** Increasing the vocabulary size consistently **improved both reconstruction quality** (MAE/MSE) **and forecasting accuracy** (IC/RankIC), confirming that finer-grained representation translates to better predictive outcomes [45, Figure 6].
*   **Tokenizer Architecture:** Transformer-based architectures **outperformed the CNN-based model** in reconstruction quality. The proposed hierarchical loss achieved reconstruction quality nearly identical to the standard loss variant, while successfully imposing the desired coarse-to-fine structure beneficial for the autoregressive model.
*   **Test-Time Scaling:** The results showed a **consistent improvement in both IC and RankIC** as the number of inference samples ($N$) increased, confirming that averaging across multiple paths mitigates stochasticity and yields a more stable forecast [47, Figure 7].

### IV. Baselines and Comparison Papers

Kronos was rigorously benchmarked against a comprehensive suite of **25 baseline models** drawn from four distinct paradigms. The full results are detailed in Appendix F, specifically Tables 14-21 and Table 10.

#### 1. Full-shot Time Series Models
These models were trained from scratch on the downstream task:

*   TimeXer (Wang et al. 2024c)
*   TimesNet (Wu et al. 2022)
*   TimeMixer (Wang et al. 2024a)
*   PatchTST (Nie et al. 2022)
*   Non-stationary Transformer (NSTransformer) (Liu et al. 2022)
*   DLinear (Zeng et al. 2023)
*   FEDformer (Zhou et al. 2022)
*   iTransformer (Liu et al. 2023)

#### 2. Zero-shot Time Series Foundation Models
These are large-scale pre-trained models evaluated in a zero-shot setting:

*   TimeMOE (Xiaoming et al. 2025)
*   Moirai (Woo et al. 2024)
*   TimesFM (Das et al. 2024)
*   Moment (Goswami et al. 2024)
*   Chronos (Ansari et al. 2024)

#### 3. Econometric Volatility Models
Included specifically for the volatility forecasting task:

*   **ARCH** (Engle 1982)
*   **GARCH** (Bollerslev 1986)

#### 4. Generative Time Series Models
Compared against for the Synthetic K-line Generation task:

*   **DiffusionTS** (Yuan and Qiao 2024) (Diffusion-based)
*   **TimeVAE** (Desai et al. 2021) (VAE-based)
*   **TimeGAN** (Yoon, Jarrett, and Van der Schaar 2019) (GAN-based)

In the **Investment Simulation** experiment (Appendix F, Table 10), Kronos variants were compared against the largest versions of all full-shot and zero-shot baselines, including $i\text{Transformer}$, TimeXer, $M\text{oirai}_{\text{large}}$, $M\text{oment}_{\text{large}}$, $C\text{hronos}_{\text{large}}$, and $T\text{imesFM}$.
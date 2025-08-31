from SimulationEngine.SimulationEngine import SimulationEngine
from MacroEconSimulation.MacroEconModel import MacroEconModel
import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from sklearn.preprocessing import StandardScaler
from scipy.ndimage import generic_filter

def simulationExecution(objConfiguration, itrNum):
    print('< now in simulation for iteration case #' + str(itrNum) + ' >')

    # Setting model execution parameter
    objConfiguration.addConfiguration("itrNum", itrNum)  # Repeat experiment iteration number
    objConfiguration.addConfiguration("time", 1)  # Simulation time

    objModel = MacroEconModel(objConfiguration)

    engine = SimulationEngine()
    engine.setOutmostModel(objModel)
    engine.run(maxTime=999999, \
               logFileName='log.txt', \
               visualizer=False, \
               logGeneral=False, \
               logActivateState=False, \
               logActivateMessage=False, \
               logActivateTA=False, \
               logStructure=False \
               )
    return

def setStaticParameters(objConfiguration, inputFilename):

    inputFilename = os.path.join('InputData',inputFilename)

    with open(inputFilename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                rawData = np.array(row[1])
                line_count += 1
            else:
                rawData = np.vstack([rawData, row[1]])
                line_count += 1

    objConfiguration.addConfiguration("N_Fk", int(rawData[0]))  # Capital good firm number
    objConfiguration.addConfiguration("N_Fc", int(rawData[1]))  # Consumption good firm number
    objConfiguration.addConfiguration("N_B", int(rawData[2]))  # Bank number
    objConfiguration.addConfiguration("N_H", int(rawData[3]))  # Household(labor) number
    objConfiguration.addConfiguration("T", int(rawData[4]))  # Simulation time
    objConfiguration.addConfiguration("nu", float(rawData[5]))  # R&D investment propensity
    objConfiguration.addConfiguration("xi", float(rawData[6]))  # R&D allocation to innovative search
    objConfiguration.addConfiguration("zeta1", float(rawData[7]))  # Innovation success rate
    objConfiguration.addConfiguration("zeta2", float(rawData[8]))  # Imitation success rate
    objConfiguration.addConfiguration("alpha1",
                                      float(rawData[9]))  # Beta distribution parameter for innovation (alpha1)
    objConfiguration.addConfiguration("beta1", float(rawData[10]))  # Beta distribution parameter for innovation (beta1)
    objConfiguration.addConfiguration("x1_lower",
                                      float(rawData[11]))  # Beta distribution support for innovation (x1_lower)
    objConfiguration.addConfiguration("x1_upper",
                                      float(rawData[12]))  # Beta distribution support for innovation (x1_upper)
    objConfiguration.addConfiguration("b", float(rawData[13]))  # Payback period
    objConfiguration.addConfiguration("mu1", float(rawData[14]))  # Mark-up coefficient (capital)
    objConfiguration.addConfiguration("mu0", float(rawData[15]))  # Mark-up coefficient (consumption)
    objConfiguration.addConfiguration("v", float(rawData[16]))  # Mark-up rule coefficient (rho)
    objConfiguration.addConfiguration("mc", int(rawData[17]))  # Min client
    objConfiguration.addConfiguration("gamma", float(rawData[18]))  # New customer sample parameter
    objConfiguration.addConfiguration("iota", float(rawData[19]))  # Desired inventory level
    objConfiguration.addConfiguration("eta", int(rawData[20]))  # Physical scrapping age
    objConfiguration.addConfiguration("alpha", float(rawData[21]))  # Cobb-douglas alpha
    objConfiguration.addConfiguration("r", float(rawData[22]))  # Interest rate
    objConfiguration.addConfiguration("psi_u", float(rawData[23]))  # Bank mark up coefficient
    objConfiguration.addConfiguration("psi_d", float(rawData[24]))  # Bank mark down coefficient
    objConfiguration.addConfiguration("pr", float(rawData[25]))  # Loan principle repayment rate (maturity)
    objConfiguration.addConfiguration("delta", float(rawData[26]))  # Maximum capital expansion rate
    objConfiguration.addConfiguration("k", float(rawData[27]))  # Credit multiplier
    objConfiguration.addConfiguration("DSR", float(rawData[28]))  # Maximum debt to sale ratio
    objConfiguration.addConfiguration("psi_1", float(rawData[29]))  # Wage setting parameter for labor productivity
    objConfiguration.addConfiguration("psi_2", float(rawData[30]))  # Wage setting parameter for cpi
    objConfiguration.addConfiguration("psi_3", float(rawData[31]))  # Wage setting parameter for unemployment rate
    objConfiguration.addConfiguration("omega_1",
                                      float(rawData[32]))  # Consumption good firm competitiveness weight for price
    objConfiguration.addConfiguration("omega_2", float(
        rawData[33]))  # Consumption good firm competitiveness weight for unfilled demand
    objConfiguration.addConfiguration("tr", float(rawData[34]))  # Tax rate
    objConfiguration.addConfiguration("phi", float(rawData[35]))  # Unemployment subsidy rate
    objConfiguration.addConfiguration("chi", float(rawData[36]))  # Replicator dynamics coefficient
    objConfiguration.addConfiguration("initEmploy", float(rawData[37]))  # Initial consumption employment rate
    objConfiguration.addConfiguration("g", float(rawData[38]))  # Labor growth rate (quarterly)


def extractSimulInfo_ConsumptionGoodFirm(dict_, itrValue, saveDir, startTime, T):

    dict = {}
    dictInfo = {}

    for i in range(0, itrValue):
        filename = os.path.join(saveDir, str(i), 'ConsumptionFirmLog.csv')
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            line_count2 = 0

            cnt = 0

            for row in csv_reader:
                cnt +=1

                if line_count == 0:
                    line_count += 1
                elif (line_count-1) % 200 == 0:
                    raw_1timestep = np.array(row)
                    line_count += 1
                else :
                    raw_1timestep = np.vstack((raw_1timestep, np.array(row)))
                    if line_count % 200 == 0 and line_count2 == 0:
                        for key, value in dict_.items():
                            dict[key] = raw_1timestep[:,value]

                        line_count2 += 1

                    elif line_count % 200 == 0 and line_count2 != 0:

                        for key, value in dict_.items():
                            dict[key] = np.vstack((dict[key], raw_1timestep[:,value]))

                    line_count += 1

            mktShare_ = np.expand_dims(dict['mktShare'].transpose(), axis=0)  # shape : (1, #C-firms, #timestep)
            mktShare_[mktShare_ == None] = 0
            mktShare_ = mktShare_.astype(float)
            order = mktShare_[0, :, startTime].argsort()[::-1]  # ordering among the firms with respect to the market share at startTime(50)

            if i == 0 :

                for key, value in dict.items():
                    dictInfo[key] = np.expand_dims(dict[key].transpose(), axis=0)[:, order,:]  # shape : (1, #C-firms, #timestep)

            else:

                for key, value in dict.items():
                    dictInfo[key] = np.concatenate((dictInfo[key], np.expand_dims(dict[key].transpose(), axis=0)[:, order,:]),axis=0)  # shape : (1, #C-firms, #timestep)

    for key, value in dictInfo.items():

        value = value.astype(float)
        avgValue = np.mean(value, axis=0)[:,startTime:T]  # shape : (#iter, #C-firms, #timestep) ->(#C-firms, #timestep)
        stdValue = np.mean(value, axis=0)[:,startTime:T]
        avgValue_forConvergence = np.mean(value, axis=0)[:,:T]
        dictInfo[key] = [avgValue, stdValue, avgValue_forConvergence]

    return dictInfo

def extractSimulInfo_Household(itrValue, startTime, T, saveDir, mode):

    tempGrowth = []
    tempHHI = []
    tempLaborShare = []

    totalProduction = np.zeros((itrValue, T-startTime))
    totalInvestment = np.zeros((itrValue, T-startTime))
    totalEmploymentRate = np.zeros((itrValue, T-startTime))
    totalWage = np.zeros((itrValue, T-startTime))

    for i in range(0, itrValue):
        filename = os.path.join(saveDir, str(i), 'Household.csv')
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                elif line_count == 1:
                    rawData = np.array(row)
                    line_count += 1
                else:
                    rawData = np.vstack([rawData, row])
                    line_count += 1
        rawData = np.transpose(rawData)

        totalProductionInfo = [float(x) for x in rawData[1]]
        totalInvestmentInfo = [float(x) for x in rawData[6]]
        employmentRateInfo = [float(x) for x in rawData[12]]
        wageInfo = [float(x) for x in rawData[14]]
        HHI_consumptionInfo = [float(x) for x in rawData[16]]
        laborShareInfo = [float(x) for x in rawData[17]]

        if mode == 'validation' or mode == 'firmLevelAnalysis':

            totalProduction[i] = [math.log(100* x/totalProductionInfo[startTime]) for x in totalProductionInfo][startTime:T]
            totalInvestment[i] = totalInvestmentInfo[startTime:T]
            totalEmploymentRate[i] = employmentRateInfo[startTime:T]
            totalWage[i] = wageInfo[startTime:T]

        elif mode == 'policyExperiment' or  mode == 'policyExperiment_joint':

            for t in range(startTime, T):
                tempGrowth.append((totalProductionInfo[t] / totalProductionInfo[t-1]) -1)
                tempHHI.append(HHI_consumptionInfo[t] * 10000)
                tempLaborShare.append(laborShareInfo[t] * 100)

    if mode == 'validation' or mode == 'firmLevelAnalysis':
        return totalProduction, totalInvestment, totalWage, totalEmploymentRate

    elif mode == 'policyExperiment' or mode == 'policyExperiment_joint':
        return tempGrowth, tempHHI, tempLaborShare

def extractRealData(filename, avgTotalInvestment_simul, avgTotalWage_simul):

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 1:
                rawData = np.array(row)
                line_count += 1
            else:
                rawData = np.vstack([rawData, row])
                line_count += 1
    rawData = np.transpose(rawData)

    realGDP = [float(x) for x in rawData[4]]
    investment = [float(x) for x in rawData[7]]
    unemploymentRate = [float(x) for x in rawData[8]]
    hiringRate = [float(x) for x in rawData[9]]
    wage = [float(x) for x in rawData[10]]
    logRealGDP = [math.log(100 * x/realGDP[0]) for x in realGDP]
    investmentDataStart = 37
    realInvestment = [avgTotalInvestment_simul[investmentDataStart - 1] * float(x) / float(investment[investmentDataStart - 1]) for x in
        investment]
    wageDataStart = 77
    realWage = [avgTotalWage_simul[wageDataStart - 1] * float(x) / float(wage[wageDataStart - 1]) for x in wage]

    realEmployment = [(100 - x)/100 for x in unemploymentRate]
    realHiring = [x/100 for x in hiringRate]

    return logRealGDP, realInvestment, realWage, realEmployment, realHiring

def getPolicyOptions(args, policy, numPolicyOptions):
    if args.mode == 'policyExperiment':
        option = []
        if policy == 'DSR':
            for i in range(numPolicyOptions):
                tempOption = np.random.uniform(1, 8, 1)[0]
                option.append(tempOption)

        elif policy == 'r':
            for i in range(numPolicyOptions):
                tempOption = np.random.uniform(0.01, 0.1, 1)[0]
                option.append(tempOption)
    elif args.mode == 'policyExperiment_joint':
        option = []
        if policy == 'DSR':
            for i in range(numPolicyOptions):
                tempOption = np.random.uniform(args.dsrRange[0], args.dsrRange[1], 1)[0]
                option.append(tempOption)

        elif policy == 'r':
            for i in range(numPolicyOptions):
                tempOption = np.random.uniform(args.rRange[0], args.rRange[1], 1)[0]
                option.append(tempOption)

    return option

def getPolicyOptions_joint(numPolicyOptions):
    option = []
    dsr_values = np.linspace(1,8,numPolicyOptions)
    r_values = np.linspace(0.01, 0.1, numPolicyOptions)
    option = [(dsr, r) for dsr in dsr_values for r in r_values]

    return option

def plotValidation(saveDir,target, real1, real2, simulAvg, simulStd, T, startTime):

    plt.plot(simulAvg, label='simulation result')
    plt.fill_between(np.linspace(0, T-startTime-1, T-startTime), simulAvg - 2 * simulStd,
                     simulAvg + 2 * simulStd, color='b', alpha=.1)

    if target == 'Employment Rate':
        plt.plot(real1, label='employment rate(real world)')
        plt.plot(real2, label='hiring rate(real world)')
    else:
        plt.plot(real1, label='validation data')

    plt.xlabel("Time (Quarterly)")
    labels = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']
    plt.xticks(range(0,140,20), labels)
    plt.ylabel(target)
    plt.legend(fontsize='small', loc='best')
    plt.savefig(os.path.join(saveDir, target+".png"), transparent=True, dpi=600)
    plt.clf()

def calcMAPE(itrValue, real1, real2, simul, target):
    lstMAPE = []
    for i in range(itrValue):
        cnt = 0
        percentError = 0
        for t in range(len(simul[i])):
            tempSimulation = simul[i][t]
            tempValidation = real1[t]
            if target == 'employment rate':
                tempValidation = (real1[t] + real2[t])/2
            if not math.isnan(tempSimulation) and not math.isnan(tempValidation):
                cnt += 1
                percentError += 100 * abs(tempValidation - tempSimulation) / tempValidation

        MAPE = percentError / cnt
        lstMAPE.append(MAPE)
        # accuracy : str(100 - np.mean(lstMAPE)) + "% ± " + str(np.std(lstMAPE)) + "%
        strAvgMAPE = "MAPE of target : " + str(np.mean(lstMAPE)) +  "% ± " + str(np.std(lstMAPE)) + "%"
    print(strAvgMAPE)

    return lstMAPE, strAvgMAPE

def plot_log_policyExperiment(saveDir, policy, option,dict_policyExp):

    if policy == 'DSR':
        filename_policyAnalysisLog = 'descriptiveAnalysisLog_DSR'

    elif policy == 'r':
        filename_policyAnalysisLog = 'descriptiveAnalysisLog_IR'

    GrowthRate_avg = dict_policyExp["GDP Growth Rate"]
    HHIResult_avg = dict_policyExp["Herfindal-Hershman Index"]
    laborShareResult_avg = dict_policyExp["Labor Share (%)"]

    # logging
    policyAnalysisLog = open(os.path.join(saveDir,filename_policyAnalysisLog+'.csv'), 'w')
    policyAnalysisLog.write(policy + ',')
    for x in option: policyAnalysisLog.write(str(x) + ',')
    policyAnalysisLog.write("\n")
    policyAnalysisLog.write(str("GDP growth rate") + ',')
    for x in GrowthRate_avg: policyAnalysisLog.write(str(x) + ',')
    policyAnalysisLog.write("\n")
    policyAnalysisLog.write(str("HHI consumption") + ',')
    for x in HHIResult_avg: policyAnalysisLog.write(str(x) + ',')
    policyAnalysisLog.write("\n")
    policyAnalysisLog.write(str("Labor share") + ',')
    for x in laborShareResult_avg: policyAnalysisLog.write(str(x) + ',')
    policyAnalysisLog.write("\n")
    policyAnalysisLog.close()

    runCurveFitting(saveDir,filename_policyAnalysisLog+'.csv', policy)

def recordArgsMAPE(saveDir,args, objConfiguration, numSurvivedKfirm=[0], lstInfoEtc=None):
    log = open(os.path.join(saveDir,'log.txt'), 'w')
    log.write('< Arguments >\n')
    for arg, value in sorted(vars(args).items()):
        log.write(arg + " : "+ str(value)+'\n')
    if lstInfoEtc != None:
        log.write('< MAPE > \n')
        for i in range(len(lstInfoEtc)):
            log.write(lstInfoEtc[i] + '\n')
    log.write('< ObjConfiguration >\n')
    for _, dic in vars(objConfiguration).items():
        for config, value in dic.items():
            log.write(config + " : " + str(value) + '\n')
    log.write('<Number of Survived Kfirms>\n')
    log.write(str(numSurvivedKfirm[0]))

def setSaveDir(args):

    dirName = "iter" + str(args.numIter)

    if args.mode == "policyExperiment":
        dirName += "_" + args.policy + str(args.numPolicyOptions)

    elif args.mode == 'policyExperiment_joint':
        dirName += "_" + 'DSR and r_' + str(args.numPolicyOptions)
    elif args.mode == 'firmLevelAnalysis':
        dirName += "_" + args.policy + str(args.lstPolicyValues)

    lstDir = ['Result', args.date, args.mode, dirName]

    saveDir = makeAndSetDir(lstDir)

    return saveDir

def makeAndSetDir(lstDir):

    saveDir = lstDir[0]
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)

    for i in lstDir[1:]:
        saveDir = os.path.join(saveDir, i)
        if not os.path.isdir(saveDir):
            os.mkdir(saveDir)

    return saveDir

def ConvertToDF_joint(saveDir, option_dsr_r, GrowthRate_avg, HHIResult_avg, laborShareResult_avg):

    dsr = np.array([t[0] for t in option_dsr_r])  # Extract x values from tuples
    r = np.array([t[1] for t in option_dsr_r])  # Extract x values from tuples
    GrowthRate_avg = np.ravel(GrowthRate_avg)
    HHIResult_avg = np.ravel(HHIResult_avg)
    laborShareResult_avg = np.ravel(laborShareResult_avg)

    df = pd.DataFrame({'DSR':dsr, 'r':r,'GrowthRate': GrowthRate_avg,'HHI': HHIResult_avg,'LaborShare': laborShareResult_avg})

    df.to_csv(os.path.join(saveDir, 'df.csv'))
    return df

def plot_jointHeatmap(df, saveDir, window_size=3):
    lst = ['HHI', 'LaborShare', 'GrowthRate']

    for l in lst:
        x = df["DSR"]
        y = df["r"]
        z = df[l]

        hist, xedges, yedges = np.histogram2d(x, y, bins=50, weights=z)
        counts, _, _ = np.histogram2d(x, y, bins=50)

        average = np.divide(hist, counts, where=counts != 0)

        overall_mean = np.nanmean(average)

        def replace_with_neighbors(values):
            center_idx = (window_size ** 2) // 2
            center = values[center_idx]

            if center < overall_mean-100:
                neighbors = np.delete(values, center_idx)
                neighbors_mean = np.nanmean(neighbors)
                return neighbors_mean
            return center

        replaced_average = generic_filter(
            average, replace_with_neighbors, size=window_size, mode="constant", cval=np.nan
        )

        x_range = xedges[-1] - xedges[0]
        y_range = yedges[-1] - yedges[0]
        aspect_ratio = x_range / y_range

        plt.figure(figsize=(12, 8))
        plt.imshow(replaced_average.T, origin="lower", cmap="viridis",
                   extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], aspect=aspect_ratio)
        cbar = plt.colorbar(label=f"Average {l} (Processed)")
        plt.xlabel("DSR")
        plt.ylabel("r")
        plt.title(f"Processed Heatmap of {l}")

        file_path = os.path.join(saveDir, f"{l}_processed_heatmap.png")
        plt.savefig(file_path, dpi=300)
        plt.close()

def saveCSV(dict, filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        for k, v in dict.items():
            writer.writerow([k, v])

def calculateHHI(policy_value,dict_mktshare, policy):

    HHI = 0
    txt_HHI = ''

    for share in dict_mktshare:
        HHI += (pow(share*100,2))
    txt_HHI += '\n HHI at ' + policy + str(policy_value) + ' : '+ str(HHI)

    return txt_HHI

def runCurveFitting(saveDir, file, policy):
    plot_eq = pd.read_csv(os.path.join(saveDir,file), header=None)

    policy_values = plot_eq[plot_eq[0] == policy].iloc[0, 1:].dropna().values
    gdp_growth_values = plot_eq[plot_eq[0] == 'GDP growth rate'].iloc[0, 1:].dropna().values
    hhi_consumption = plot_eq[plot_eq[0] == 'HHI consumption'].iloc[0, 1:].dropna().values
    labor_share = plot_eq[plot_eq[0] == 'Labor share'].iloc[0, 1:].dropna().values

    data = {policy: policy_values, 'GDP growth rate': gdp_growth_values, 'HHI consumption': hhi_consumption, 'Labor share': labor_share}
    df = pd.DataFrame(data)

    df[policy] = pd.to_numeric(df[policy], errors='coerce')
    df['GDP growth rate'] = pd.to_numeric(df['GDP growth rate'], errors='coerce')
    df['HHI consumption'] = pd.to_numeric(df['HHI consumption'], errors='coerce')
    df['Labor share'] = pd.to_numeric(df['Labor share'], errors='coerce')

    policy_data = df[policy]
    GDP = df['GDP growth rate']
    HHI = df['HHI consumption']
    Labor = df['Labor share']

    policy_values = policy_data.values.flatten()
    GDP_values = GDP.values.flatten()
    GDP_values *= 100
    HHI_values = HHI.values.flatten()
    Labor_values = Labor.values.flatten()

    model_GDP, r2_GDP, eq_GDP = polyFit(policy_values, GDP_values, 1)
    if policy == 'DSR':
        model_HHI, r2_HHI, eq_HHI = polyFit(policy_values, HHI_values, 2)
    elif policy == 'r':
        model_HHI, r2_HHI, eq_HHI = polyFit(policy_values, HHI_values, 1)
    model_LS, r2_LS, eq_LS = polyFit(policy_values, Labor_values, 1)

    plot(policy_values, GDP_values, model_GDP, eq_GDP, r2_GDP, policy, 'Growth', saveDir)
    plot(policy_values, HHI_values, model_HHI, eq_HHI, r2_HHI, policy, 'HHI', saveDir)
    plot(policy_values, Labor_values, model_LS, eq_LS, r2_LS, policy, 'Labor Share', saveDir)

def polyFit(x_values, y_values, order):

    if order == 1:
        X = sm.add_constant(x_values)
        model = sm.OLS(y_values, X)
        results = model.fit()
        intercept, slope = results.params
        r2 = results.rsquared
        r2 = round(r2, 4)
        equation = f"y = {round(slope, 3)}x + {round(intercept, 3)}"

    elif order == 2:
        X = np.column_stack((x_values, x_values**2))
        X = sm.add_constant(X)
        model = sm.OLS(y_values, X)
        results = model.fit()
        intercept, coef_x, coef_x2 = results.params
        r2 = results.rsquared
        r2 = round(r2,4)
        equation = f"y = {round(coef_x2, 3)}x^2 + {round(coef_x, 3)}x + {round(intercept, 3)}"

    elif order == 3:
        X = np.column_stack((x_values, x_values ** 2, x_values ** 3))
        X = sm.add_constant(X)
        model = sm.OLS(y_values, X)
        results = model.fit()
        intercept, coef_x, coef_x2, coef_x3 = results.params
        r2 = results.rsquared
        r2 = round(r2, 4)
        equation = f"y = {round(coef_x3, 3)}x^3 + {round(coef_x2, 3)}x^2 +  {round(coef_x, 3)}x + {round(intercept, 3)}"

    return model, r2, equation

def plot(x_values, y_values, model, equation, r2, xlabel, ylabel, saveDir):

    polyline = np.linspace(min(x_values), max(x_values), 100)

    results = model.fit()
    num_features = len(results.params) - 1
    poly_features = np.column_stack([polyline ** d for d in range(1, num_features + 1)])
    polyline_reg = sm.add_constant(poly_features)

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, label='Data')
    plt.plot(polyline, results.predict(polyline_reg), '--', linewidth=3,
             label=equation + f'\n$R^2$ = {r2:.3f}')

    if ylabel == 'Growth':
        ylabel = 'GDP Growth Rate (%)'
        figName = xlabel + '_Growth'
    elif ylabel == 'Labor Share':
        ylabel = 'Labor Share (%)'
        figName = xlabel + '_LaborShare'
    elif ylabel == 'HHI':
        ylabel = 'Herfindahl-Hirschman Index (HHI)'
        figName = xlabel + '_HHI'
    else:
        figName = xlabel + '_' + ylabel

    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.tight_layout()

    plt.savefig(os.path.join(saveDir, figName + '.png'), dpi=300)
    plt.clf()

def regression_analysis_joint(data, output_path, dependent_variable, poly_degree_dsr, poly_degree_r):
    """
    Perform OLS regression on specified dependent and independent variables with polynomial features.

    Parameters:
        input_csv (str): Path to the input CSV file.
        output_path (str): Path to save the output table.
        dependent_variable (str): The dependent variable ('HHI', 'GrowthRate', or 'LaborShare').
        poly_degree_dsr (int): The highest degree of polynomial terms for 'DSR' to include as an independent variable.
        poly_degree_r (int): The highest degree of polynomial terms for 'r' to include as an independent variable.

    Output:
        Saves a table with coefficients, standardized coefficients, R^2, adjusted R^2, and significance levels to the output path.
    """

    # Extract variables
    if dependent_variable not in ['HHI', 'GrowthRate', 'LaborShare']:
        raise ValueError("dependent_variable must be one of 'HHI', 'GrowthRate', or 'LaborShare'")

    y = data[dependent_variable]
    X = data[['DSR', 'r']]

    # Generate polynomial features for DSR
    for degree in range(2, poly_degree_dsr + 1):
        X[f'DSR^{degree}'] = X['DSR'] ** degree

    # Generate polynomial features for r
    for degree in range(2, poly_degree_r + 1):
        X[f'r^{degree}'] = X['r'] ** degree

    # Add a constant for the regression
    X = sm.add_constant(X)

    # Fit the model
    model = sm.OLS(y, X).fit()

    # Calculate standardized coefficients
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.drop(columns=['const']))
    y_scaled = (y - y.mean()) / y.std()
    std_model = sm.OLS(y_scaled, X_scaled).fit()
    standardized_coefficients = std_model.params

    # Create the output table
    results_table = pd.DataFrame({
        "Variable": model.params.index,
        "Coefficient": model.params.values,
        "Standardized Coefficient": [np.nan] + list(standardized_coefficients),
        "P-Value": model.pvalues.values,
        "Significance (1%)": model.pvalues < 0.01,
        "Significance (5%)": model.pvalues < 0.05,
        "Significance (10%)": model.pvalues < 0.10
    })

    # Add R^2 and Adjusted R^2 as separate rows
    r2 = model.rsquared
    adj_r2 = model.rsquared_adj

    r2_row = pd.DataFrame({
        "Variable": ["R^2"],
        "Coefficient": [r2],
        "Standardized Coefficient": [np.nan],
        "P-Value": [np.nan],
        "Significance (1%)": [np.nan],
        "Significance (5%)": [np.nan],
        "Significance (10%)": [np.nan]
    })

    adj_r2_row = pd.DataFrame({
        "Variable": ["Adjusted R^2"],
        "Coefficient": [adj_r2],
        "Standardized Coefficient": [np.nan],
        "P-Value": [np.nan],
        "Significance (1%)": [np.nan],
        "Significance (5%)": [np.nan],
        "Significance (10%)": [np.nan]
    })

    # Combine all rows
    results_table = pd.concat([results_table, r2_row, adj_r2_row], ignore_index=True)

    # Save the results to a CSV file
    results_table.to_csv(output_path, index=False)

def plotConvergence(dictTarget_mktShare, saveDir):
    numFirms = dictTarget_mktShare.shape[0]
    colors = cm.viridis(np.linspace(0, 1, numFirms))

    for i in range(numFirms):
        plt.plot(dictTarget_mktShare[i], color=colors[i])

    norm = mcolors.Normalize(vmin=1, vmax=(numFirms))
    sm = plt.cm.ScalarMappable(cmap='viridis_r', norm=norm)
    sm.set_array([])
    plt.xlim(0, dictTarget_mktShare.shape[-1]+1)
    plt.ylabel('Market Share')
    plt.xlabel('Timestep')
    plt.legend(fontsize='small', loc='best')
    plt.savefig(os.path.join(saveDir, "Convergence_indiv.png"), transparent=True, dpi=600)
    plt.clf()

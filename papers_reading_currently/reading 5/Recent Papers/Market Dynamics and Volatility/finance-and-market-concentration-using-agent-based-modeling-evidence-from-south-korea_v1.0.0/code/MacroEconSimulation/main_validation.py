import os
import numpy as np
from utils import simulationExecution, plotConvergence, extractSimulInfo_ConsumptionGoodFirm, extractSimulInfo_Household, extractRealData, plotValidation,calcMAPE, recordArgsMAPE
from multiprocessing import Pool
from itertools import repeat

def runValidation(args, objConfiguration, saveDir, T):

    # Settings
    realData = os.path.join('InputData', 'validation.csv')
    startTime = T-120  # 120 timesteps = 30years

    # Replicate the simulation and save the results
    with Pool(processes=4) as pool:
        numSurvivedKfirm = pool.starmap(simulationExecution, zip(repeat(objConfiguration), range(0, args.numIter)))

    # Extract the key information from the simulation results
    totalProduction, totalInvestment, totalWage, totalEmploymentRate = extractSimulInfo_Household(args.numIter,
                                                                                                  startTime, T,
                                                                                                  saveDir,
                                                                                                  args.mode)
    dict_guide = {'mktShare': 8}  # guides of number for the targets
    dictTarget = extractSimulInfo_ConsumptionGoodFirm(dict_guide, args.numIter, saveDir, startTime, T)

    for key in dictTarget.keys():
        dictTarget[key] = dictTarget[key][-1] # (#C-firms, #timestep)

    plotConvergence(dictTarget['mktShare'],saveDir)

    avgTotalProduction = np.mean(totalProduction, axis=0)
    stdTotalProduction = np.std(totalProduction, axis=0)
    avgTotalInvestment = np.mean(totalInvestment, axis=0)
    stdTotalInvestment = np.std(totalInvestment, axis=0)
    avgTotalWage = np.mean(totalWage, axis=0)
    stdTotalWage = np.std(totalWage, axis=0)
    avgTotalEmploymentRate = np.mean(totalEmploymentRate, axis=0)
    stdTotalEmploymentRate = np.std(totalEmploymentRate, axis=0)

    # Extract the necessary information from the real-world data
    logRealGDP, realInvestment, realWage, realEmployment, realHiring = extractRealData(realData, avgTotalInvestment,
                                                                                       avgTotalWage)

    # Save the plots and MAPEs that compare the simulation results and the real world data
    plotValidation(saveDir, 'Log Real GDP', logRealGDP, None, avgTotalProduction, stdTotalProduction, T,
                   startTime)
    plotValidation(saveDir, 'Investment', realInvestment, None, avgTotalInvestment, stdTotalInvestment, T,
                   startTime)
    plotValidation(saveDir, 'Wage', realWage, None, avgTotalWage, stdTotalWage, T,
                   startTime)
    plotValidation(saveDir, 'Employment Rate', realEmployment, realHiring, avgTotalEmploymentRate,
                   stdTotalEmploymentRate, T,
                   startTime)

    lstMAPE_logRealGDP, strAvgMAPE_logRealGDP = calcMAPE(args.numIter, logRealGDP, None, totalProduction,
                                                         'logRealGDP')
    lstMAPE_investment, strAvgMAPE_investment = calcMAPE(args.numIter, realInvestment, None, totalInvestment,
                                                         'investment')
    lstMAPE_wage, strAvgMAPE_wage = calcMAPE(args.numIter, realWage, None, totalWage, 'wage')
    lstMAPE_employmentRate, strAvgMAPE_employmentRate = calcMAPE(args.numIter, realEmployment, realHiring,
                                                                 totalEmploymentRate, 'employment rate')

    lstAvgMAPE = [strAvgMAPE_logRealGDP, strAvgMAPE_investment, strAvgMAPE_wage, strAvgMAPE_employmentRate]
    recordArgsMAPE(saveDir, args, objConfiguration, numSurvivedKfirm, lstAvgMAPE)
from utils import getPolicyOptions, simulationExecution, extractSimulInfo_Household, plot_log_policyExperiment, recordArgsMAPE, extractSimulInfo_ConsumptionGoodFirm, saveCSV
import numpy as np
from multiprocessing import Pool
from itertools import repeat
import os


def runPolicyExperiment(args, objConfiguration, saveDir, T):
    # Settings
    startTime = T - 120

    # For every option, replicate the simulation
    option = getPolicyOptions(args, args.policy, args.numPolicyOptions)

    # ------------------------ #

    GrowthRate_avg = np.zeros(len(option))
    HHIResult_avg = np.zeros(len(option))
    laborShareResult_avg = np.zeros(len(option))

    dict_recordFirms = {}

    for p in range(len(option)):
        print('< now in simulation for policy case #' + str(p) + ': ' + args.policy + ' ' + str(option[p]) + ' >')
        objConfiguration.addConfiguration(args.policy, option[p])

        with Pool(processes=4) as pool:
            pool.starmap(simulationExecution, zip(repeat(objConfiguration), range(0, args.numIter)))

        # Extract the key information from the simulation results

        tempGrowth, tempHHI, tempLaborShare = extractSimulInfo_Household(
            args.numIter, startTime, T, saveDir, args.mode)
        dict_guide = {'debt': 3, 'mktShare': 8, 'production': 13,'investment': 14}  # guides of number for the targets
        dictTarget = extractSimulInfo_ConsumptionGoodFirm(dict_guide, args.numIter, saveDir, startTime, T)

        for key in dictTarget.keys():
            dictTarget[key] = dictTarget[key][0]
            dictTarget[key] = dictTarget[key][:,-1]
        dict_recordFirms[option[p]] = dictTarget

        iter = args.numIter
        step = int(len(tempGrowth) / args.numIter)

        GrowthRate_avg[p] = np.mean(np.array(tempGrowth).reshape(iter, step)[:, -1])
        HHIResult_avg[p] = np.mean(np.array(tempHHI).reshape(iter, step)[:, -1])
        laborShareResult_avg[p] = np.mean(np.array(tempLaborShare).reshape(iter, step)[:, -1])
    
    saveCSV(dict_recordFirms, os.path.join(saveDir, 'dict_recordFirms.csv'))

    # Save the plots
    dict_policyExp = {"GDP Growth Rate": GrowthRate_avg, "Herfindal-Hershman Index": HHIResult_avg,
                      "Labor Share (%)": laborShareResult_avg}

    plot_log_policyExperiment(saveDir, args.policy, option, dict_policyExp)
    recordArgsMAPE(saveDir, args, objConfiguration)

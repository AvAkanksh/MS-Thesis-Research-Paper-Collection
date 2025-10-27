from utils import simulationExecution, extractSimulInfo_Household, plot_jointHeatmap, getPolicyOptions_joint,ConvertToDF_joint
import numpy as np
from multiprocessing import Pool
from itertools import repeat
import os
from utils import regression_analysis_joint

def runPolicyExperiment_joint(args, objConfiguration, saveDir, T):
    # Settings
    if args.policy == 'DSR':
        startTime = T-120
    elif args.policy == 'r':
        startTime = T-120


    GrowthRate_avg = np.zeros((args.numPolicyOptions**2))
    HHIResult_avg = np.zeros((args.numPolicyOptions**2))
    laborShareResult_avg = np.zeros((args.numPolicyOptions**2))

    option_dsr_r = getPolicyOptions_joint(args.numPolicyOptions)

    for idx, (dsr, r) in enumerate(option_dsr_r):
        try:
            print('< now in simulation for case #' + str(idx)+' : ' + 'DSR ' + str(
                dsr) + ' and r ' + str(r) + ' >')
            objConfiguration.addConfiguration('DSR', dsr)
            objConfiguration.addConfiguration('r', r)

            with Pool(processes=4) as pool:
                pool.starmap(simulationExecution, zip(repeat(objConfiguration), range(0, args.numIter)))

            tempGrowth, tempHHI, tempLaborShare = extractSimulInfo_Household(args.numIter, startTime, T, saveDir, args.mode)

            iter = args.numIter
            step = int(len(tempGrowth) / args.numIter)
            GrowthRate_avg[idx] = np.mean(np.array(tempGrowth).reshape(iter, step)[:, -1])
            HHIResult_avg[idx] = np.mean(np.array(tempHHI).reshape(iter, step)[:, -1])
            laborShareResult_avg[idx] = np.mean(np.array(tempLaborShare).reshape(iter, step)[:, -1])

        except Exception as e:
            print('Error!!')
            continue

    df = ConvertToDF_joint(saveDir, option_dsr_r, GrowthRate_avg, HHIResult_avg, laborShareResult_avg)

    poly_degree_dsr = args.dsrDegree
    poly_degree_r = args.rDegree
    plot_jointHeatmap(df, saveDir)
    output_path = os.path.join(saveDir, 'regression_HHI.csv')
    regression_analysis_joint(df, output_path, 'HHI', poly_degree_dsr, poly_degree_r)
    output_path = os.path.join(saveDir, 'regression_GrowthRate.csv')
    regression_analysis_joint(df, output_path, 'GrowthRate', poly_degree_dsr, poly_degree_r)
    output_path = os.path.join(saveDir, 'regression_LaborShare.csv')
    regression_analysis_joint(df, output_path, 'LaborShare', poly_degree_dsr, poly_degree_r)
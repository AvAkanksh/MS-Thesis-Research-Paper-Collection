import argparse
import time
import sys
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))

from SimulationEngine.Utility.Configurator import Configurator
from utils import setStaticParameters, setSaveDir
from main_validation import runValidation
from main_policyExperiment import runPolicyExperiment
from main_policyExperiment_joint import runPolicyExperiment_joint

def parser():

    parser = argparse.ArgumentParser(description='MacroEconSimulation')
    parser.add_argument('--date', type=str, default='250322', help='date of running the code')
    parser.add_argument('--mode', type=str, default='policyExperiment', help='running purpose', choices=['validation', 'policyExperiment', 'policyExperiment_joint'])
    parser.add_argument('--numIter', type=int, default=2, help='number of simulation replications')
    parser.add_argument('--numBin', type=int, default=20)
    parser.add_argument('--logging', type=bool, default=True, help='log or not')
    parser.add_argument('--policy', type=str, default='DSR', help='type of policies', choices=['DSR', 'r'])
    parser.add_argument('--numPolicyOptions', type=int, default=50, help='number of policy options for the policy experiment')
    parser.add_argument('--dsrDegree', type=int, default=2, help='degree of DSR regression')
    parser.add_argument('--rDegree', type=int, default=2, help='degree of r regression')
    parser.add_argument('--dsrRange', type=list, default=[1,8], help='maximum value for DSR')
    parser.add_argument('--rRange', type=list, default=[0.01, 1], help='maximum value for r')

    return parser.parse_args()

def main():

    # ---------- Timing ---------- #

    time_start = time.time()

    # ---------- Basic Settings ---------- #

    args = parser()
    objConfiguration = Configurator()

    # ---------- Saving Directories ---------- #

    saveDir = setSaveDir(args)
    objConfiguration.addConfiguration('saveDir', saveDir)

    # ---------- Set the static parameters ---------- #

    staticVariableFilename = 'Static_parameter.csv'

    setStaticParameters(objConfiguration, staticVariableFilename)
    T = objConfiguration.getConfiguration("T") #170

    # ---------- Run Validation or PolicyExperiment or FirmLevelAnalysis ---------- #

    if args.mode == 'validation':
        runValidation(args, objConfiguration, saveDir, T)

    elif args.mode == 'policyExperiment':
        runPolicyExperiment(args, objConfiguration, saveDir, T)

    elif args.mode == 'policyExperiment_joint':
        runPolicyExperiment_joint(args, objConfiguration, saveDir, T)

    else:
        print('Error : Type the mode again!')

    # ---------- Print Running Time ---------- #

    time_end = time.time()

    print('Time for ' + args.mode + ' : %f sec' % (time_end - time_start))

if __name__ == '__main__':

    main()
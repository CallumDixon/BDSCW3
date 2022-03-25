import sys

raw = open("./conf/epos.properties", "r+")
contents = raw.read().split("\n")
raw.seek(0)                    
raw.truncate()
iterations = sys.argv[1]
children = sys.argv[2]
stratergy = sys.argv[3]
alpha = sys.argv[4]
beta = sys.argv[5]
raw.write("dataset=energy\nnumSimulations=1\nnumIterations="+str(iterations)+"\nnumAgents=1000\nnumPlans=10\nnumChildren="+str(children)+"\nplanDim=100\nshuffle=0\nshuffle_file=\"permutation.csv\"\nnumberOfWeights = 2\nweightsString = \""+ alpha +","+ beta +"\"\nstrategy=" + str(stratergy) + "\nperiodically.reorganizationPeriod=3\nconvergence.memorizationOffset=5\nglobalCost.reductionThreshold=0.5\nstrategy.reorganizationSeed=0\ngoalSignalPath=default\nglobalCostFunction=VAR\nscaling=\"MIN-MAX\"\nlocalCostFunction=\"INDEX\"\nlogger.GlobalCostLogger = true\nlogger.LocalCostMultiObjectiveLogger = true\nlogger.TerminationLogger = true\nlogger.SelectedPlanLogger = true\nlogger.GlobalResponseVectorLogger = true\nlogger.PlanFrequencyLogger = true\nlogger.UnfairnessLogger = true\nlogger.GlobalComplexCostLogger = true\nlogger.WeightsLogger = true\nlogger.ReorganizationLogger = true\nlogger.VisualizerLogger = true\nlogLevel=\"SEVERE\"\n")
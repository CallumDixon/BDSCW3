
declare -a arr1=("5" "30" "50") #iterations
declare -a arr2=("3" "5" "10") #children
declare -a arr3=("periodically" "convergence" "globalCostReduction" "never") #stratergy
declare -a arr4=("0.01" "0.2" "0.5") #alpha
declare -a arr5=("0.01" "0.2" "0.5") #beta

# declare -a arr1=("5" "30") #iterations
# declare -a arr2=("3" "5") #children
# declare -a arr3=("periodically") #stratergy
# declare -a arr4=("0.01") #alpha
# declare -a arr5=("0.01") #beta

for i in "${arr1[@]}"
do
    for j in "${arr2[@]}"
    do
        for k in "${arr3[@]}"
        do
            for l in "${arr4[@]}"
            do
                for m in "${arr5[@]}"
                do
                    echo "run"
                    python3 config.py $i $j $k $l $m
                    java -jar IEPOS-Tutorial.jar
                done
            done
        done
    done
done

declare -a arr1=("5" "30" "50") #iterations
declare -a arr2=("3" "5" "10") #children

for i in "${arr1[@]}"
do
    for j in "${arr2[@]}"
        do
            echo "run"
            python3 config.py $i $j
            java -jar IEPOS-Tutorial.jar
        done
done
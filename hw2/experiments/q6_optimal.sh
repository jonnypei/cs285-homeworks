for seed in $(seq 1 5); 
do
    python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v4 -n 100 \
    --exp_name pendulum_optimal_s$seed \
    --use_baseline -na \
    --batch_size 3000 \
    --seed $seed
done
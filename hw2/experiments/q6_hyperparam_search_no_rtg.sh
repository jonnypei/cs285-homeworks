for discount in 0.99; do
    for n_layers in 2 4 8; do
        for batch_size in 1000 3000 5000 10000; do
            for seed in $(seq 1 5); do
                python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v4 -n 100 \
                    --exp_name pendulum_batchsz{$batch_size}_s{$seed}_discnt{$discount}_nlayers{$n_layers}_nortg \
                    --use_baseline -na \
                    --batch_size $batch_size \
                    --seed $seed \
                    --discount $discount \
                    --n_layers $n_layers
            done

            for lambda in 0.95 0.99; do
                for seed in $(seq 1 5); do
                    python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v4 -n 100 \
                        --exp_name pendulum_batchsz{$batch_size}_s{$seed}_discnt{$discount}_nlayers{$n_layers}_gaelambda{$lambda}_nortg \
                        --use_baseline -na \
                        --batch_size $batch_size \
                        --seed $seed \
                        --discount $discount \
                        --n_layers $n_layers \
                        --gae_lambda $lambda
                done
            done
        done
    done
done
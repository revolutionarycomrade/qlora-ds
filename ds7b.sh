deepspeed qlora-ds.py \
    --model_name_or_path /mnt/c/models/daryl149_llama-2-7b-chat-hf \
    --output_dir ./output/llama-2-guanaco-7b \
    --logging_steps 1 \
    --save_strategy steps \
    --data_seed 42 \
    --save_steps 500 \
    --save_total_limit 40 \
    --max_new_tokens 32 \
    --dataloader_num_workers 1 \
    --group_by_length \
    --logging_strategy steps \
    --remove_unused_columns False \
    --do_train \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_modules all \
    --double_quant \
    --quant_type nf4 \
    --bf16 \
    --bits 4 \
    --warmup_ratio 0.03 \
    --lr_scheduler_type constant \
    --gradient_checkpointing \
    --dataset oasst1 \
    --source_max_len 16 \
    --target_max_len 512 \
    --gradient_accumulation_steps 16 \
    --max_steps 1875 \
    --learning_rate 0.0002 \
    --adam_beta2 0.999 \
    --max_grad_norm 0.3 \
    --lora_dropout 0.1 \
    --weight_decay 0.0 \
    --seed 0 \
    --ddp_find_unused_parameters False

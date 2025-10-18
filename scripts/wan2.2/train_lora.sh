#!/bin/bash
#SBATCH --job-name=wan22-train
#SBATCH --partition=dgx-b200
#SBATCH --gres=gpu:8
#SBATCH --cpus-per-task=16
#SBATCH --mem=512G
#SBATCH --time=2-00:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err

source /vast/home/l/liyiqian/anaconda3/etc/profile.d/conda.sh
conda activate vx

export NCCL_DEBUG=INFO
export NCCL_IB_DISABLE=1
export NCCL_P2P_DISABLE=1

cd /vast/projects/jgu32/lab/yiqian/VideoX-Fun

export MODEL_NAME="/vast/projects/jgu32/lab/yiqian/VideoX-Fun/models/Diffusion_Transformer/Wan2.2-TI2V-5B"
export DATASET_NAME="/vast/projects/jgu32/lab/yiqian/VideoX-Fun"
export DATASET_META_NAME="/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/json_of_internal_datasets.json"

accelerate launch --mixed_precision="bf16" scripts/wan2.2/train_lora_custom.py \
  --config_path="/vast/projects/jgu32/lab/yiqian/VideoX-Fun/config/wan2.2/wan_civitai_5b.yaml" \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$DATASET_NAME \
  --train_data_meta=$DATASET_META_NAME \
  --image_sample_size=1024 \
  --video_sample_size=256 \
  --token_sample_size=512 \
  --video_sample_stride=2 \
  --video_sample_n_frames=81 \
  --train_batch_size=4 \
  --video_repeat=1 \
  --gradient_accumulation_steps=1 \
  --dataloader_num_workers=8 \
  --num_train_epochs=5 \
  --checkpointing_steps=50 \
  --learning_rate=1e-04 \
  --seed=42 \
  --output_dir="/vast/projects/jgu32/lab/yiqian/VideoX-Fun/output_dir" \
  --gradient_checkpointing \
  --mixed_precision="bf16" \
  --adam_weight_decay=3e-2 \
  --adam_epsilon=1e-10 \
  --vae_mini_batch=1 \
  --max_grad_norm=0.05 \
  --random_hw_adapt \
  --training_with_video_token_length \
  --enable_bucket \
  --uniform_sampling \
  --boundary_type="full" \
  --train_mode="ti2v" \
  --low_vram

